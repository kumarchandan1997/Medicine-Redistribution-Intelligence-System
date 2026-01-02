import pandas as pd

def generate_csv_report(suggestions):
    df = pd.DataFrame(suggestions)
    df.to_csv("reports/redistribution_report.csv", index=False)
