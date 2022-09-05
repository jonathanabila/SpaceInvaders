from settings.constants import DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session


class DB:
    def __init__(self) -> None:
        self._install_generic_sqlalchemy_db_and_session()

    def _install_generic_sqlalchemy_db_and_session(self) -> None:
        self.engine = create_engine(DATABASE_URI)
        self.declarative_base = DeclarativeBase()

        session_factory = sessionmaker(bind=self.engine)
        self.declarative_base.metadata.bind = self.engine

        self.app_session = scoped_session(session_factory)
