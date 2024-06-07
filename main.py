from typing import Union

from fastapi import FastAPI
from feedback_model import Feedback
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

db_connection = "postgresql://postgres:sa@localhost/postgres"
engine = create_engine(db_connection)


@app.get("/")
def read_root():
    return {"status":"ok","data": ["edwin","warming","gunawan"],"message":"Data ok"}


@app.post("/users")
def write_user():

    return  {"status":"ok","data": ["edwin","warming","gunawan"],"message":"User was created"}

@app.post("/rating")
def update_rating():

    return  {"status":"ok","data": ["edwin","warming","gunawan"],"message":"Rating was updated."}