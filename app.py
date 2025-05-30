from fastapi import FastAPI, Request
from agents.classifier_agent import classify_and_route

app = FastAPI()

@app.post("/process")
async def process_input(request: Request):
    body = await request.json()
    source_id = body.get("source_id", "unknown")
    input_data = body.get("data")
    
    result = classify_and_route(input_data, source_id)
    return {"result": result}
