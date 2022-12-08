from pydantic import BaseModel


class QuizzesCreateDto(BaseModel):
    pass

    class Config:
        orm_mode = True
