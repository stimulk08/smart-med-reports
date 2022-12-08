from pydantic import BaseModel


class PatientCreateDto(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
