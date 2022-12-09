from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Database
from app.db.patient_quiz import patient_quiz_table

tag_patient_table = Table(
    "tag_patient",
    Database.metadata,
    Column("patient_id", ForeignKey("patient.id")),
    Column("tag_id", ForeignKey("tag.id")),
)


class Tag(Database):
    __tablename__ = "tag"
    id = Column(Integer, primary_key=True, index=True)
    patients = relationship("Patient", secondary=patient_quiz_table, back_populates="tags")
    doctor = relationship("Doctor", secondary=patient_quiz_table, back_populates="tags")
