from datetime import datetime

import sqlalchemy
from database import space_invaders_db


class Step(space_invaders_db.declarative_base):
    __tablename__ = "steps"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), default=datetime.now, nullable=False)

    lives = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    score = sqlalchemy.column(sqlalchemy.Integer, nullable=False)

    game_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("games.id"), ondelete="CASCADE"
    )

    # --------------------------------------- Relationships -------------------------------------- #

    game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id], back_populates="steps")
