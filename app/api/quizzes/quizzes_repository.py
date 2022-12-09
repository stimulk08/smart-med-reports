from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Database
# from app.models.user import patient_quizzes_table



    # patients = relationship("Patient", secondary=patient_quizzes_table, back_populates="quizzes")

