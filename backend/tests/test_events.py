import os
from fastapi.testclient import TestClient
import pytest

from app import main

client = TestClient(main.app)


def setup_module(module):
    # Remove existing DB so tests start clean
    db_path = os.path.join(os.path.dirname(__file__), '..', 'risk.db')
    db_path = os.path.abspath(db_path)
    if os.path.exists(db_path):
        os.remove(db_path)
    # import seed to populate
    from backend import seed as seed_module  # original seed.py at backend/seed.py


def test_get_events():
    resp = client.get("/events")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_event_by_id():
    resp = client.get("/events/1")
    assert resp.status_code == 200
    data = resp.json()
    assert "id" in data
    assert "supplier" in data
