from sqlalchemy import Column, Integer, String
from backend.db import Base

class Person(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    num_tel = Column(Integer)
