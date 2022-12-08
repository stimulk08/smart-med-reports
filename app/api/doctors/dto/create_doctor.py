from pydantic import BaseModel


class DoctorCreateDto(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True
