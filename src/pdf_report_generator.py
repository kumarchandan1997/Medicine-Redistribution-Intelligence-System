from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime
import os

def generate_pdf_report(suggestions, impact):
    if not suggestions:
        return None

    os.makedirs("reports", exist_ok=True)

    file_name = f"reports/Medicine_Impact_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>National Medicine Redistribution Impact Report</b>", styles["Title"]))
    elements.append(Paragraph(f"Generated On: {datetime.now()}", styles["Normal"]))
    elements.append(Paragraph("<br/>", styles["Normal"]))

    # Impact Summary
    summary_data = [
        ["Metric", "Value"],
        ["Total Cost Saved (₹)", impact["total_cost_saved_inr"]],
        ["Total Units Saved", impact["total_units_saved"]],
        ["Patients Helped (Estimated)", impact["patients_helped_est"]],
    ]

    summary_table = Table(summary_data)
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
    ]))

    elements.append(summary_table)
    elements.append(Paragraph("<br/>", styles["Normal"]))

    # Redistribution Table
    table_data = [["From", "To", "Medicine", "Qty", "Distance (KM)", "Cost Saved (₹)"]]

    for s in suggestions:
        table_data.append([
            s["from"],
            s["to"],
            s["medicine"],
            s["quantity"],
            s["distance_km"],
            s["cost_saved_inr"]
        ])

    data_table = Table(table_data, repeatRows=1)
    data_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("GRID", (0,0), (-1,-1), 0.5, colors.black),
        ("ALIGN", (3,1), (-1,-1), "CENTER"),
    ]))

    elements.append(data_table)

    doc.build(elements)
    return file_name
