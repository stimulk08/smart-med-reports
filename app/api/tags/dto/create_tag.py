from pydantic import BaseModel


class TagCreateDto(BaseModel):
    title: str

    class Config:
        orm_mode = True
