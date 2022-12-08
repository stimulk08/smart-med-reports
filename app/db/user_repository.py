from sqlalchemy.orm import Session

from app.models.user import Patient


# from app.models.schemas import Patient


def create_user(db: Session, user: Patient):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_patients(db: Session):
    return db.query(Patient).all()

