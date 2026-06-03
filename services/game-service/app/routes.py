from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import GameCreate, GameList, GameOut
from app.service import add_game, fetch_all_games, fetch_game, find_games

router = APIRouter(prefix="/v1/games", tags=["games"])


@router.post("/", response_model=GameOut, status_code=status.HTTP_201_CREATED)
def create_game(data: GameCreate, db: Session = Depends(get_db)) -> GameOut:
    return add_game(db, data)


@router.get("/", response_model=GameList)
def list_games(
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> GameList:
    return fetch_all_games(db, limit, offset)


@router.get("/search", response_model=GameList)
def search_games(
    q: str = Query(min_length=1),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> GameList:
    return find_games(db, q, limit, offset)


@router.get("/{game_id}", response_model=GameOut)
def get_game(game_id: str, db: Session = Depends(get_db)) -> GameOut:
    try:
        return fetch_game(db, game_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc