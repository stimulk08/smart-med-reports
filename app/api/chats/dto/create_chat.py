from pydantic import BaseModel


class CreateChatDto(BaseModel):
    doctor_id: int