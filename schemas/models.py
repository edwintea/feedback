#from typing import Optional
#from uuid import UUID

from pydantic import BaseModel

import pydantic
print("pydantic version : "+pydantic.__version__)


class HealthResponse(BaseModel):
    status: str


class Feedback(BaseModel):
    email:str
    rating: int

    class Config:
        orm_mode=True
        #from_attributes = True


class DeleteFeedbackResponse(BaseModel):
    detail: str


class UpdateFeedback(BaseModel):
    email:str
    rating: int

    class Config:
        orm_mode=True
        #from_attributes = True
