def process_email(email_text):
    # Dummy extraction logic for example
    sender = None
    urgency = None
    lines = email_text.splitlines()
    for line in lines:
        if line.startswith("From:"):
            sender = line[5:].strip()
        if "urgent" in line.lower():
            urgency = "High"
    # Simple intent placeholder (actual intent comes from classifier)
    return {
        "sender": sender or "unknown",
        "urgency": urgency or "Normal",
        "content_snippet": email_text[:100]
    }
