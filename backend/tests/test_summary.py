from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)


def test_summary():
    resp = client.get("/summary")
    assert resp.status_code == 200
    data = resp.json()
    assert "total_events" in data
    assert "high" in data
    assert "medium" in data
    assert "low" in data
