from app.models.schemas import PatientCreate
from app.db.database import Database

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Session


class Patient(Database):
    __tablename__ = "patients"
    login = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    # illness = relationship("Illness", secondary=association_table, back_populates='patients')
    # doctors = relationship("Doctor", secondary=association_table, back_populates='patients')
    # visits = relationship("Visit", secondary=association_table, back_populates='patients')


def create_patient(db: Session, dto: PatientCreate):
    db_user = Patient(**dto.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_patients(db: Session):
    return db.query(Patient).all()
