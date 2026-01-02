from src.expiry_checker import find_expiring_medicines
from src.redistribution_engine import suggest_redistribution
from src.impact_metrics import calculate_impact
from src.data_loader import load_inventory, load_hospitals
from src.db_writer import save_redistribution_results, save_impact_summary
from src.report_generator import generate_csv_report
from src.pdf_report_generator import generate_pdf_report
from src.graph_generator import generate_graphs

inventory = load_inventory()
hospitals = load_hospitals()

expiring = find_expiring_medicines(inventory)
suggestions = suggest_redistribution(expiring, inventory, hospitals)

impact = calculate_impact(suggestions)

save_redistribution_results(suggestions)
save_impact_summary(impact)

csv_file = generate_csv_report(suggestions)
pdf_file = generate_pdf_report(suggestions, impact)

generate_graphs(suggestions)

print("\n📊 NATIONAL MEDICINE IMPACT REPORT\n")
print("₹ Total Cost Saved:", impact["total_cost_saved_inr"])
print("Total Units Saved:", impact["total_units_saved"])
print("Estimated Patients Helped:", impact["patients_helped_est"])
print("📄 CSV Report:", csv_file)
print("📕 PDF Report:", pdf_file)
