from src.expiry_checker import find_expiring_medicines
from src.redistribution_engine import suggest_redistribution
from src.impact_metrics import calculate_impact
from src.data_loader import load_inventory, load_hospitals
from src.db_writer import save_redistribution_results, save_impact_summary

# Load from MySQL
inventory = load_inventory()
hospitals = load_hospitals()

# Business logic
expiring = find_expiring_medicines(inventory)
suggestions = suggest_redistribution(expiring, inventory, hospitals)

impact = calculate_impact(suggestions)

# Save to MySQL
save_redistribution_results(suggestions)
save_impact_summary(impact)

print("\n📊 NATIONAL MEDICINE IMPACT REPORT (MYSQL)\n")
print("₹ Total Cost Saved:", impact['total_cost_saved_inr'])
print("Total Units Saved:", impact['total_units_saved'])
print("Estimated Patients Helped:", impact['patients_helped_est'])
