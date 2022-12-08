from sqlalchemy.orm import Session
from typing import TypeVar, Generic, List

T = TypeVar('T')


class BaseRepository(Generic[T]):
    @staticmethod
    def get_all(db: Session):
        return db.query(T).all()

    @staticmethod
    def get_by_id(db: Session, _id: int):
        pass

    @staticmethod
    def create(db: Session, model: T) -> T:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    @staticmethod
    def delete(db: Session, _id: int):
        pass

    @staticmethod
    def update(db: Session, _id: int, updates):
        pass