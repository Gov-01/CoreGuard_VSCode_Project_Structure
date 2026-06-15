from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)


def test_add_and_get_notes():
    # add a note to event 1
    resp = client.post("/notes", json={"event_id": 1, "note": "Test note"})
    assert resp.status_code == 200
    assert resp.json().get("message") == "Note Added"

    # fetch notes for event 1
    resp2 = client.get("/events/1/notes")
    assert resp2.status_code == 200
    notes = resp2.json()
    assert any(n["note"] == "Test note" for n in notes)
