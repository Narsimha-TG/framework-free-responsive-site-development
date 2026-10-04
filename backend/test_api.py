import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_analytics():
    response = client.get("/api/analytics")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "title" in data[0]

def test_submit_contact_valid():
    payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "message": "Hello, this is a test inquiry."
    }
    response = client.post("/api/contact", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Form submitted successfully"
    assert response.json()["received"] == "john@example.com"