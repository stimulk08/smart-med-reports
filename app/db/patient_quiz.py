from sqlalchemy import Column, ForeignKey, Table, Integer

from app.db.database import Database

patient_quiz_table = Table(
    "patient_quiz",
    Database.metadata,
    Column("quiz_id", ForeignKey("quiz.id")),
    Column("patient_id", ForeignKey("patient.id")),
)
