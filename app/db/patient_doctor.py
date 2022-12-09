from sqlalchemy import Table, Column, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, relationship

from app.db.database import Database
from app.db.doctor_quiz import doctor_quiz_table
from app.db.patient_quiz import patient_quiz_table
from app.db.tag_doctor import tag_doctor_table
from app.db.tag_patient import tag_patient_table

patient_doctor_table = Table(
    "patient_doctor",
    Database.metadata,
    Column("patient_id", ForeignKey("patient.id")),
    Column("doctor_id", ForeignKey("doctor.id")),
)


class Doctor(Database):
    __tablename__ = "doctor"

    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    patients = relationship("Patient", secondary=patient_doctor_table, back_populates="doctors")
    quizzes = relationship("Quiz", secondary=doctor_quiz_table, back_populates="doctors")
    tags = relationship("Tag", secondary=tag_doctor_table, back_populates='doctors')


class Patient(Database):
    __tablename__ = "patient"
    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    quizzes = relationship("Quiz", secondary=patient_quiz_table, back_populates="patients")
    doctors = relationship("Doctor", secondary=patient_doctor_table, back_populates='patients')
    tags = relationship("Tag", secondary=tag_patient_table, back_populates='patients')
