from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = None
db_session = None
Base = declarative_base()

from .access import Access
from .page import Page
from .user import User

def init_engine(uri, **kwargs):
    global engine
    global db_session
    engine = create_engine(uri, **kwargs)
    Base.metadata.create_all(engine)
    db_session = sessionmaker(bind=engine, autocommit=False)
    return engine

def get_session():
    return db_session()