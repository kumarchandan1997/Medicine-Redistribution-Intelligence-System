import pandas as pd
import os
from datetime import datetime

def generate_csv_report(suggestions):
    if not suggestions:
        return None

    os.makedirs("reports", exist_ok=True)

    df = pd.DataFrame(suggestions)

    filename = f"reports/redistribution_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)

    return filename
