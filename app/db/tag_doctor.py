from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Database
from app.db.patient_quiz import patient_quiz_table

tag_doctor_table = Table(
    "tag_doctor",
    Database.metadata,
    Column("doctor_id", ForeignKey("doctor.id")),
    Column("tag_id", ForeignKey("tag.id")),
)
