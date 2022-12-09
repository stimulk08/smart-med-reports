from sqlalchemy import Column, Integer, Enum, String, ARRAY
from sqlalchemy.orm import relationship

from app.db.database import Database


class TextField(Database):
    __tablename__ = "text_field"
    id = Column(Integer, primary_key=True)
    value = Column(String)
    quizzes = relationship("Quiz", back_populates="text_fields")


class NumberField(Database):
    __tablename__ = "number_field"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    quizzes = relationship("Quiz", back_populates="number_fields")


class ChoiceField(Database):
    __tablename__ = "choice_field"
    id = Column(Integer, primary_key=True)
    value = Column(ARRAY(String))
    quizzes = relationship("Quiz", back_populates="choice_fields")
