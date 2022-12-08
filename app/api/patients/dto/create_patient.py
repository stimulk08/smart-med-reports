from pydantic import BaseModel


class PatientCreateDto(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    # doctors: Doctor[]

    class Config:
        orm_mode = True


