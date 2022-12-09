from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.db.database import Database
from app.models.user import association_table_2


class Quizzes(Database):
    __tablename__ = "quizzes_table"

    id = Column(Integer, primary_key=True)
    doctors = relationship("Doctor", back_populates='reports')
    patient = relationship("Patient", secondary=association_table_2, back_populates="reports")

