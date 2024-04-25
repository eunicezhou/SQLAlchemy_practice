from sqlalchemy import create_engine, Column, String, Integer, Table,MetaData
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///data.db", echo = True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    sex = Column(String)


Base.metadata.create_all(engine)