#from typing import Optional
#from uuid import UUID

from pydantic import BaseModel

import pydantic
print("pydantic version : "+pydantic.__version__)


class HealthResponse(BaseModel):
    status: str


class Feedback(BaseModel):
    id:int
    email:str
    rating: int

    class Config:
        #orm_mode=True
        from_attributes = True

class CreateFeedback(BaseModel):
    email:str
    rating: int

    class Config:
        orm_mode=True
        #from_attributes = True


class DeleteFeedbackResponse(BaseModel):
    detail: str

class DeleteFeedback(BaseModel):
    id:int

    class Config:
        orm_mode=True
        #from_attributes = True


class UpdateFeedback(BaseModel):
    id:int
    email:str
    rating: int

    class Config:
        orm_mode=True
        #from_attributes = True
