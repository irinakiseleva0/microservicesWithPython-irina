from sqlalchemy.orm import Session

from app import repository
from app.schemas import GameCreate, GameList, GameOut
from app.infrastructure.cache import set_game_summary

def add_game(db: Session, data: GameCreate) -> GameOut:
    game = repository.create_game(db, data)

    set_game_summary(
        game.id,
        {
            "id": game.id,
            "title": game.title,
            "genre": game.genre,
            "platform": game.platform,
            "cover_url": game.cover_url,
        },
    )

    return GameOut.model_validate(game)


def fetch_game(db: Session, game_id: str) -> GameOut:
    game = repository.get_game(db, game_id)
    if game is None:
        raise ValueError("Game not found")
    return GameOut.model_validate(game)


def fetch_all_games(db: Session, limit: int, offset: int) -> GameList:
    items, total = repository.list_games(db, limit, offset)
    return GameList(
        items=[GameOut.model_validate(item) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )


def find_games(db: Session, q: str, limit: int, offset: int) -> GameList:
    items, total = repository.search_games(db, q, limit, offset)
    return GameList(
        items=[GameOut.model_validate(item) for item in items],
        total=total,
        limit=limit,
        offset=offset,
    )