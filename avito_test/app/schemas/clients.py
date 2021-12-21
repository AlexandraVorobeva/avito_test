from pydantic import BaseModel
from decimal import Decimal


class ClientBase(BaseModel):
    first_name: str
    last_name: str



class Client(ClientBase):
    id: int
    balance: float

    class Config:
        orm_mode = True


class ClientCreate(ClientBase):
    balance: float = 0.0
    pass