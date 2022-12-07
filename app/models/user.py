import enum
from sqlalchemy import Column, Integer, String, Table, ForeignKey, ARRAY, Enum
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from ..core.config import Database

association_table = Table(
    "association_table",
    Database.metadata,
    Column("left_id", ForeignKey("left_table.id")),
    Column("right_id", ForeignKey("right_table.id")),
)


class FieldType(enum.Enum):
    yesNo = 1
    text = 2
    number = 3
    range = 4


class Field(Database):
    __tablename__ = "field"
    id = Column(Integer, primary_key=True)
    type = Column(Enum(FieldType))
    value = Column(JSON)


class User(Database):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)


class ReportTemplate(Database):
    __tablename__ = "report_template"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("doctor.id"))
    fields = ARRAY()


class Report(Database):
    __tablename__ = "report"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("doctor.id"))
    parent = relationship("Doctor", back_populates="children")


class Doctor(Database):
    __tablename__ = "doctor"
    id = Column(Integer, primary_key=True)
    patients = relationship("Patient", secondary=association_table)
    reports = relationship("doctor", back_populates="report")
    specialization = None


class Patient(Database):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True)
    illness = None
    doctors = None
    visits = None