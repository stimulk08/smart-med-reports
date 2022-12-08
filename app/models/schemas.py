from pydantic import BaseModel


class PatientCreate(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str


class Patient(BaseModel):
    id: int
    login: str
    password: str
