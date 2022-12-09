from pydantic import BaseModel


class QuizzesCreateDto(BaseModel):
    doctor_id: int
    fields: list

    class Config:
        orm_mode = True
