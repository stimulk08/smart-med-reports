import enum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.dialects.postgresql import JSON

from app.db.database import Database


#
# patient_quizzes_table = Table(
#     "patient_reports",
#     Database.metadata,
#     Column("patient_id", ForeignKey("patient.id")),
#     Column("quiz_id", ForeignKey("quiz.id")),
# )


# class FieldType(enum.Enum):
#     yesNo = 1
#     text = 2
#     number = 3
#     range = 4

#
# class Field(Database):
#     __tablename__ = "field"
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(FieldType))
#     value = Column(JSON)


# class User(Database):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     login = Column(String)
#     password = Column(String)
#     first_name = Column(String)
#     last_name = Column(String)
#

#
# class ReportTemplate(Database):
#     __tablename__ = "report_template"
#     id = Column(Integer, primary_key=True)
#     owner_id = Column(Integer, ForeignKey("doctor.id"))
#
#
#
# class Report(Database):
#     __tablename__ = "report"
#     id = Column(Integer, primary_key=True)
#     owner_id = Column(Integer, ForeignKey("doctor.id"))
#     parent = relationship("Doctor", back_populates="reports")
#
#
# class Doctor(Database):
#     __tablename__ = "doctor"
#
#     login = Column(String)
#     password = Column(String)
#     first_name = Column(String)
#     last_name = Column(String)
#     id = Column(Integer, primary_key=True)
#     patients = relationship("Patient", secondary=association_table, back_populates="doctors")
#     reports = relationship("Report", secondary=association_table, back_populates="owner_id")
#     specialization = relationship("Specialization", secondary=association_table, back_populates="doctors")



# class Illness(Database):
#     __tablename__ = "illness"
#     id = Column(Integer, primary_key=True)
#     patients = relationship("Patient", secondary=association_table, back_populates='illness')
#     specialization = relationship("Specialization", secondary=association_table, back_populates='illness')
#
#
# class Visit(Database):
#     __tablename__ = "visit"
#     id = Column(Integer, primary_key=True)
#     patients = relationship("Patient", back_populates='illness')
#
#
# class Specialization(Database):
#     __tablename__ = "specialization"
#     id = Column(Integer, primary_key=True)
#     doctors = relationship("Doctor", secondary=association_table, back_populates="specialization")
#     illness = relationship("Specialization", back_populates="specialization")
#
