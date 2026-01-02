from src.db import get_connection

def save_redistribution_results(suggestions):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO redistribution_results
    (priority, source_hospital, target_hospital, medicine, distance_km, quantity, cost_saved)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    for s in suggestions:
        cursor.execute(query, (
            s["priority"],
            s["from"],
            s["to"],
            s["medicine"],
            s["distance_km"],
            s["quantity"],
            s["cost_saved_inr"]
        ))

    conn.commit()
    conn.close()

def save_impact_summary(impact):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO impact_summary
    (total_cost_saved, total_units_saved, patients_helped)
    VALUES (%s,%s,%s)
    """

    cursor.execute(query, (
        impact["total_cost_saved_inr"],
        impact["total_units_saved"],
        impact["patients_helped_est"]
    ))

    conn.commit()
    conn.close()
