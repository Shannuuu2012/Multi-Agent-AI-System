import os
import json
from agents.classifier_agent import classify_and_route
from utils import read_pdf_text  # ✅ if utils is a file, not a folder

def print_result(title, result):
    print(f"\n>> {title}")
    print("=== Output ===")
    for key, value in result.items():
        print(f"{key}: {value}")
    print()

# Test JSON
with open("samples/sample_invoice.json", "r") as f:
    json_data = json.load(f)
    result = classify_and_route(json_data, source_id="json_sample_001")
    print_result("JSON Sample", result)

# Test Email
with open("samples/sample_email.txt", "r") as f:
    email_text = f.read()
    result = classify_and_route(email_text, source_id="email_sample_001")
    print_result("Email Sample", result)

# Test PDF
pdf_path = "samples/sample_regulation.pdf"
if os.path.exists(pdf_path):
    pdf_text = read_pdf_text(pdf_path)
    result = classify_and_route(pdf_text, source_id="pdf_sample_001")
    print_result("PDF Sample", result)
else:
    print("[!] PDF file not found at:", pdf_path)
