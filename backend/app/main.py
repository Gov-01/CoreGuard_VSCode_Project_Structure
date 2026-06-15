from fastapi import FastAPI

from app.database import engine
from app.models import Base
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.event_routes import router as event_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(event_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "CoreGuard"}
