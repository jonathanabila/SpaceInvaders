from database.db import DB as SpaceInvadersDB

space_invaders_db = SpaceInvadersDB()


def init_models() -> None:
    from models.game import Game

    model_classes = [Game]

    def noop(*args) -> None:
        return None

    for model_class in model_classes:
        noop(model_class)
