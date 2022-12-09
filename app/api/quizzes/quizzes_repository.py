from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Session

from app.db.database import Database


class QuizCreateDto:
    pass


def create_quiz(db: Session, dt: QuizCreateDto):
    pass
