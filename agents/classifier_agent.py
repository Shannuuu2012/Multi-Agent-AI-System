import json
from transformers import pipeline
from agents.email_agent import process_email
from agents.json_agent import process_json
from memory.shared_memory import save_to_memory

# Load zero-shot classifier (local model)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

LABELS = ["Invoice", "RFQ", "Complaint", "Regulation", "Other"]

def classify_and_route(input_data, source_id=None):
    # Determine format
    if isinstance(input_data, dict):
        text = json.dumps(input_data)
        format_type = "JSON"
    else:
        text = input_data
        format_type = "Email" if "From:" in text else "PDF"

    # Classify intent
    prediction = classifier(text, LABELS)
    intent = prediction["labels"][0]

    # Route to agent
    if format_type == "Email":
        result = process_email(input_data)
    elif format_type == "JSON":
        result = process_json(input_data)
    else:
        # For PDF, just stub (implement PDF agent if needed)
        result = {"text": input_data[:200]}

    # Save to Redis memory
    memory_entry = {
        "source_id": source_id,
        "format": format_type,
        "intent": intent,
        "result": result
    }
    save_to_memory(memory_entry)

    return memory_entry
