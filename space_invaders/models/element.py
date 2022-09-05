from datetime import datetime
from enum import Enum
from typing import Tuple

import sqlalchemy
from database import space_invaders_db
from sqlalchemy.ext.hybrid import hybrid_property


class ElementType(Enum):
    ASTEROID = "ASTEROID"
    INVADER = "INVADER"


ElementTypeEnum = sqlalchemy.Enum(ElementType)


class Element(space_invaders_db.declarative_base):
    __tablename__ = "elements"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), default=datetime.now, nullable=False)

    x = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    y = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    type = sqlalchemy.Column(ElementTypeEnum, nullable=False)

    lives = sqlalchemy.column(sqlalchemy.Integer, nullable=True)

    game_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey("games.id"), ondelete="CASCADE"
    )

    # --------------------------------------- Relationships -------------------------------------- #

    game = sqlalchemy.orm.relationship("Game", foreign_keys=[game_id], back_populates="score")

    @hybrid_property
    def position(self) -> Tuple[int, int]:
        return self.x, self.y
