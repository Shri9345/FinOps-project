import boto3
import sqlite3
from datetime import datetime, timedelta

# Set date range
end = datetime.utcnow().date()
start = end - timedelta(days=1)

client = boto3.client('ce')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start.strftime('%Y-%m-%d'),
        'End': end.strftime('%Y-%m-%d')
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
    ]
)

# Setup SQLite
conn = sqlite3.connect('costs.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS costs (date TEXT, service TEXT, amount REAL)''')

# Save data
for group in response['ResultsByTime'][0]['Groups']:
    service = group['Keys'][0]
    amount = float(group['Metrics']['UnblendedCost']['Amount'])
    c.execute("INSERT INTO costs VALUES (?, ?, ?)", (start.strftime('%Y-%m-%d'), service, amount))

conn.commit()
conn.close()
print("Data saved to SQLite!")
