from datetime import datetime
import uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.infrastructure.rabbitmq_publisher import publish_activity_event
import httpx

app = FastAPI(title="Activity Service")

activities = []


class ActivityCreate(BaseModel):
    user_id: str
    game_id: str
    action: str


class ActivityOut(BaseModel):
    id: str
    user_id: str
    game_id: str
    action: str
    created_at: datetime
    game: dict | None = None


async def validate_user(user_id: str):
    url = f"http://localhost:8001/v1/users/{user_id}"

    for attempt in range(3):
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(url)

            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="User not found")

            response.raise_for_status()
            return response.json()

        except httpx.RequestError:
            if attempt == 2:
                raise HTTPException(
                    status_code=503, detail="User service unavailable")


async def fetch_game(game_id: str):
    url = f"http://localhost:8002/v1/games/{game_id}"

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)

        if response.status_code != 200:
            return None

        return response.json()

    except Exception:
        return None


@app.get("/health")
def health():
    return {"status": "ok", "service": "activity-service"}


@app.post("/v1/activities", response_model=ActivityOut)
@app.post("/v1/activities", response_model=ActivityOut)
async def create_activity(activity: ActivityCreate):
    await validate_user(activity.user_id)

    game = await fetch_game(activity.game_id)

    saved = {
        "id": str(uuid.uuid4()),
        "user_id": activity.user_id,
        "game_id": activity.game_id,
        "action": activity.action,
        "created_at": datetime.utcnow(),
    }

    activities.append(saved)

    game_title = game["title"] if game else None

    await publish_activity_event(
        user_id=saved["user_id"],
        game_id=saved["game_id"],
        action=saved["action"],
        game_title=game_title,
    )

    return {**saved, "game": game}


@app.get("/v1/activities")
def list_activities():
    return activities
