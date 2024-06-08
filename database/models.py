#import uuid

from sqlalchemy import Column, String,Integer
#from sqlalchemy.dialects.postgresql import UUID

from database.connection import Base, engine

class Feedbacks(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True,autoincrement=True)
    email = Column(String, unique=True)
    rating = Column(Integer,default=0)


Base.metadata.create_all(engine)
