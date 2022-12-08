from app.db.database import Database

from sqlalchemy import Column, String, DATETIME, Integer


class Message(Database):
    __tablename__ = "messages"
    text: Column(String)
    creation_date: Column(DATETIME)
    sender_id: Column(Integer)  # Relation with users


class Chat(Database):
    __tablename__ = "patients"
    # messages:
