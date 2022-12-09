from sqlalchemy import Column, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship

from app.db.database import Database
from app.db.patient_quiz import patient_quiz_table

doctor_quiz_table = Table(
    "doctor_quiz",
    Database.metadata,
    Column("quiz_id", ForeignKey("quiz.id")),
    Column("doctor_id", ForeignKey("doctor.id")),
)


class Quiz(Database):
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True)
    doctors = relationship("Doctor", secondary=doctor_quiz_table, back_populates='quizzes')
    patients = relationship("Patient", secondary=patient_quiz_table, back_populates='quizzes')
