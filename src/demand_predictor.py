def predict_demand(row, days=60):
    return row['daily_consumption'] * days
