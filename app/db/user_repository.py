from sqlalchemy.orm import Session

from app.models.schemas import PatientCreate
from app.models.user import Patient


# from app.models.schemas import Patient


def create_user(db: Session, user: PatientCreate):
    db_user = Patient(**user.__dict__)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_patients(db: Session):
    return db.query(Patient).all()

