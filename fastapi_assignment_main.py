from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# -------------------
# Part 1 - GET requests
# -------------------

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """
    GET /items/{item_id}
    Path parameter: item_id (int)
    Optional query parameter: q (str)
    """
    return {"item_id": item_id, "q": q}

# -------------------
# Part 2 - PUT request
# -------------------

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: Optional[float] = None

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    PUT /items/{item_id}
    Path parameter: item_id (int)
    Request body: Item (Pydantic model)
    """
    return {"item_id": item_id, "item": item}