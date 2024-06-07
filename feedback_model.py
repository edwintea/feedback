from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    email:str
    rating: int