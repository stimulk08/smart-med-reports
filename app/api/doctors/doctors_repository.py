from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship, Session

from app.api.doctors.dto.create_doctor import DoctorCreateDto
from app.db.database import Database
from app.models.user import association_table


class Doctor(Database):
    __tablename__ = "doctor"

    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True)
    patients = relationship("Patient", secondary=association_table, back_populates="doctors")
    # reports = relationship("Report", secondary=association_table, back_populates="owner_id")
    # specialization = relationship("Specialization", secondary=association_table, back_populates="doctors")


def create_doctor(db: Session, dto: DoctorCreateDto):
    db_user = Doctor(**dto.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
