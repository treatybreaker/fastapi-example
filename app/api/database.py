from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .application import application

app = application.app


class Database:

    def __init__(self, database_url: str, sqlite: bool = False):
        self.url = database_url
        if sqlite:
            self.engine = create_engine(database_url, connect_args={"check_same_thread": False})
        else:
            self.engine = create_engine(database_url)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.base = declarative_base()


database = Database("sqlite:///../database/db.sqlite3")
