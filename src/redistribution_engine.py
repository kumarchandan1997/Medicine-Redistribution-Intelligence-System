from src.demand_predictor import predict_demand
from src.distance_calculator import calculate_distance
from src.cost_calculator import calculate_cost_saved

MAX_DISTANCE_KM = 50

def suggest_redistribution(expiring_df, inventory_df, hospitals_df):
    suggestions = []

    for _, source in expiring_df.iterrows():
        source_hospital = hospitals_df[hospitals_df['hospital_id'] == source['hospital_id']].iloc[0]

        for _, target in inventory_df.iterrows():
            if source['medicine_name'] != target['medicine_name']:
                continue

            if source['hospital_id'] == target['hospital_id']:
                continue

            required = predict_demand(target)
            if target['quantity'] >= required:
                continue

            target_hospital = hospitals_df[hospitals_df['hospital_id'] == target['hospital_id']].iloc[0]

            distance = calculate_distance(
                source_hospital['latitude'], source_hospital['longitude'],
                target_hospital['latitude'], target_hospital['longitude']
            )

            if distance > MAX_DISTANCE_KM:
                continue

            cost_saved = calculate_cost_saved(source['quantity'])

            suggestions.append({
                "priority": round(source['priority_score'], 2),
                "from": source_hospital['hospital_name'],
                "to": target_hospital['hospital_name'],
                "medicine": source['medicine_name'],
                "distance_km": distance,
                "quantity": source['quantity'],
                "cost_saved_inr": cost_saved
            })


    return suggestions
