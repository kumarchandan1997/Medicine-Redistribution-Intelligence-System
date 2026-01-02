import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

sns.set_theme(style="whitegrid")

def generate_graphs(suggestions):
    if not suggestions:
        return

    os.makedirs("dashboard/static/graphs", exist_ok=True)

    df = pd.DataFrame(suggestions)

    # ------------------------------
    # 1. Medicine-wise Cost Saved
    # ------------------------------
    plt.figure()
    sns.barplot(data=df, x="medicine", y="cost_saved_inr")
    plt.title("Medicine-wise Cost Saved (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("dashboard/static/graphs/medicine_cost.png")
    plt.close()

    # ------------------------------
    # 2. Hospital-wise Units Saved
    # ------------------------------
    plt.figure()
    hospital_units = df.groupby("from")["quantity"].sum().reset_index()
    sns.barplot(data=hospital_units, x="from", y="quantity")
    plt.title("Hospital-wise Units Saved")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("dashboard/static/graphs/hospital_units.png")
    plt.close()

    # ------------------------------
    # 3. Medicine Distribution
    # ------------------------------
    plt.figure()
    df["medicine"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Medicine Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("dashboard/static/graphs/medicine_distribution.png")
    plt.close()
