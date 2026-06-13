from fastapi import FastAPI

from app.database import init_db
from app.routes import router

app = FastAPI(title="game-service", version="1.0.0")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok", "service": "game-service"}


app.include_router(router)