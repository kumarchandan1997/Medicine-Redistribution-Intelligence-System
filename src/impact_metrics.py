def calculate_impact(suggestions):
    total_cost_saved = sum(s['cost_saved_inr'] for s in suggestions)
    total_units_saved = sum(s['quantity'] for s in suggestions)

    # Assume 1 unit = 1 patient (conservative)
    patients_helped = total_units_saved

    return {
        "total_cost_saved_inr": total_cost_saved,
        "total_units_saved": total_units_saved,
        "patients_helped_est": patients_helped
    }
