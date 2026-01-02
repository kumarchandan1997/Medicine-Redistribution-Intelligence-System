import pandas as pd
from datetime import datetime

def find_expiring_medicines(df, days=120):
    today = datetime.today()
    df['expiry_date'] = pd.to_datetime(df['expiry_date'])
    df['days_left'] = (df['expiry_date'] - today).dt.days

    df = df[df['days_left'] > 0]
    df = df[df['days_left'] <= days]

    # Priority score (lower days_left = higher priority)
    df['priority_score'] = (
        (days - df['days_left']) * 0.6 +
        df['quantity'] * 0.4
    )

    return df.sort_values(by='priority_score', ascending=False)
