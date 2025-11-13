import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add root project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_get_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Spice"
    assert data["breed"] == "Gotland"
    assert data["sex"] == "Female"

def test_add_sheep():
    sheep_data = {
        "id": 2,
        "name": "Clover",
        "breed": "Suffolk",
        "sex": "Male"
    }
    response = client.post("/sheep", json=sheep_data)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Clover"
    assert data["breed"] == "Suffolk"
    assert data["sex"] == "Male"

    # Verify the new sheep exists in the database
    get_response = client.get("/sheep/2")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Clover"