from uuid import UUID

from sqlalchemy.orm import Session

from database.models import Feedbacks
from schemas.models import DeleteFeedbackResponse, Feedback, UpdateFeedback


def feedback_create(db: Session, post: Feedback):
    db_post = Feedbacks(email=post.email,rating=post.rating)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def feedback_get_all(db: Session):
    return db.query(Feedbacks).all()


def feedback_get_one(db: Session, id: UUID):
    return db.query(Feedbacks).filter_by(id=id).one()


def feedback_update(db: Session, post: UpdateFeedback):
    update_query = {Feedbacks.email: post.email,Feedbacks.rating : post.rating}
    db.query(Feedbacks).filter_by(email=post.email).update(update_query)
    db.commit()
    return db.query(Feedbacks).filter_by(email=post.email).one()


def feedback_delete(db: Session, id: UUID):
    post = db.query(Feedbacks).filter_by(id=id).all()
    if not post:
        return DeleteFeedbackResponse(detail="Doesnt Exist")
    db.query(Feedbacks).filter_by(id=id).delete()
    db.commit()
    return DeleteFeedbackResponse(detail="Feedback Deleted")
