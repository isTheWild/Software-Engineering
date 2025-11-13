from fastapi import FastAPI, HTTPException, status
from models.models import Sheep
from models.db import db

app = FastAPI(title="Sheep Compendium")

@app.get("/sheep/{sheep_id}", response_model=Sheep)
def get_sheep(sheep_id: int):
    sheep = db.get_sheep(sheep_id)
    if not sheep:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep

@app.post("/sheep", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    added_sheep = db.add_sheep(sheep)
    return added_sheep