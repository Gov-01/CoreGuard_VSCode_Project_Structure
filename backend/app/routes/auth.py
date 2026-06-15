from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt

router = APIRouter()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


class LoginRequest(BaseModel):
    username: str
    password: str


USERS = {
    "manager": {
        "password": "manager123",
        "role": "manager"
    },
    "operator": {
        "password": "operator123",
        "role": "operator"
    }
}


@router.post("/login")
def login(data: LoginRequest):

    user = USERS.get(data.username)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {
            "sub": data.username,
            "role": user["role"]
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "role": user["role"]
    }