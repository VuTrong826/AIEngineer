from pydantic import BaseModel, Field
from typing import Literal

class Ticket(BaseModel):
    title :  str = Field(description ="Tiêu đề ngắn gọn của ticket")
    priority : Literal["low","medium","high","urgent"]
    is_bug : bool

