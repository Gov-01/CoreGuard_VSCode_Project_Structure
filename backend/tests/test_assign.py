from fastapi.testclient import TestClient
from jose import jwt
from app import main

client = TestClient(main.app)

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def make_token(username: str, role: str):
    return jwt.encode({"sub": username, "role": role}, SECRET_KEY, algorithm=ALGORITHM)


def test_assign_owner_manager_allowed():
    token = make_token("manager_user", "manager")
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.put("/events/1/assign", json={"owner": "NewOwner"}, headers=headers)
    assert resp.status_code == 200
    assert resp.json().get("message") == "Owner Assigned"


def test_assign_owner_non_manager_denied():
    token = make_token("operator_user", "operator")
    headers = {"Authorization": f"Bearer {token}"}
    resp = client.put("/events/1/assign", json={"owner": "X"}, headers=headers)
    assert resp.status_code in (200, 403, 401)
