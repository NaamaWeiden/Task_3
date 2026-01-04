from fastapi import FastAPI
from fastapi import HTTPException
import json

app = FastAPI()

FILE_PATH = "titanic.json"

@app.post("/payload_json")
async def payload_json(payload: dict):
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(payload)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=2)

    return {"message": "Payload added"}


@app.get("/get_last_10")
async def get_last_10():
    try:
        with open(FILE_PATH,'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return[]
    
    return data[-10:]


