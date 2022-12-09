from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.db.database import Database
from app.models.user import patient_quizzes_table


class Quiz(Database):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True)
    doctors = relationship("Doctor", back_populates='quizzes')
    patient = relationship("Patient", secondary=patient_quizzes_table, back_populates="quizzes")

