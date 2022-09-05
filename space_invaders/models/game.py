from datetime import datetime

import sqlalchemy
from database import space_invaders_db


class Game(space_invaders_db.declarative_base):
    __tablename__ = "games"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime(), default=datetime.now, nullable=False)
