from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///taskmanager.db')

class Base(DeclarativeBase):
    pass

Session_local = sessionmaker(bind=engine)