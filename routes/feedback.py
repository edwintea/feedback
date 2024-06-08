from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from schemas.models import DeleteFeedbackResponse, Feedback, UpdateFeedback,DeleteFeedback
from utils.feedback_crud import (
    feedback_create,
    feedback_delete,
    feedback_get_one,
    feedback_update,
    feedback_get_all,
)

router = APIRouter(tags=["feedback"])


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Feedback)
def create_feedback(post: Feedback, db: Session = Depends(get_db)):
    return feedback_create(db=db, post=post)


@router.get("/list/all", status_code=status.HTTP_200_OK, response_model=List[Feedback])
def get_all_feedback(db: Session = Depends(get_db)):
    return feedback_get_all(db=db)


@router.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=Feedback)
def get_one_feedback(id, db: Session = Depends(get_db)):
    try:
        return feedback_get_one(db=db, id=id)    
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback Not Found"
        )


    

@router.delete("/delete", status_code=status.HTTP_200_OK, response_model=DeleteFeedbackResponse)
def delete_feedback(post: DeleteFeedback, db: Session = Depends(get_db)):
    delete_status = feedback_delete(db=db, post=post)
    if delete_status.detail == "Doesnt Exist":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Feedback Not Found"
        )
    else:
        return delete_status


@router.patch("/update", status_code=status.HTTP_200_OK, response_model=Feedback)
def update_post(post: UpdateFeedback, db: Session = Depends(get_db)):
    return feedback_update(db=db, post=post)
