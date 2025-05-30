def process_json(json_data):
    # Example extraction - check for required fields
    required_fields = ["invoice_number", "amount", "date"]
    missing_fields = [f for f in required_fields if f not in json_data]

    anomalies = bool(missing_fields)

    return {
        "missing_fields": missing_fields,
        "anomalies": anomalies,
        "data": json_data
    }
