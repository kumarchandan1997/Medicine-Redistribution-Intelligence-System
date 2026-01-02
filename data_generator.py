import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# CONFIG
# -----------------------------
NUM_HOSPITALS = 220
NUM_INVENTORY = 1200

states_districts = {
    "Madhya Pradesh": ["Bhopal", "Indore", "Sehore", "Raisen", "Ujjain"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Prayagraj"],
    "Bihar": ["Patna", "Gaya", "Muzaffarpur"],
    "Rajasthan": ["Jaipur", "Kota", "Ajmer"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"]
}

medicines = [
    "Paracetamol",
    "Amoxicillin",
    "Azithromycin",
    "Cough Syrup",
    "ORS",
    "Ibuprofen",
    "Vitamin B-Complex",
    "Metformin",
    "Amlodipine",
    "Insulin"
]

# -----------------------------
# HOSPITAL DATA
# -----------------------------
hospitals = []

for i in range(1, NUM_HOSPITALS + 1):
    state = random.choice(list(states_districts.keys()))
    district = random.choice(states_districts[state])

    hospitals.append({
        "hospital_id": i,
        "hospital_name": f"{district} Hospital {i}",
        "district": district,
        "state": state,
        "latitude": round(random.uniform(22.0, 26.0), 4),
        "longitude": round(random.uniform(75.0, 80.0), 4)
    })

hospitals_df = pd.DataFrame(hospitals)
hospitals_df.to_csv("data/hospitals.csv", index=False)

# -----------------------------
# INVENTORY DATA
# -----------------------------
inventory = []

for i in range(1, NUM_INVENTORY + 1):
    hospital_id = random.randint(1, NUM_HOSPITALS)
    medicine = random.choice(medicines)

    expiry_date = datetime.today() + timedelta(days=random.randint(30, 300))

    inventory.append({
        "inventory_id": i,
        "hospital_id": hospital_id,
        "medicine_name": medicine,
        "batch_no": f"BATCH{random.randint(1000,9999)}",
        "expiry_date": expiry_date.strftime("%Y-%m-%d"),
        "quantity": random.randint(10, 800),
        "daily_consumption": random.randint(1, 10)
    })

inventory_df = pd.DataFrame(inventory)
inventory_df.to_csv("data/inventory.csv", index=False)

print("✅ Generated hospitals.csv and inventory.csv successfully")
