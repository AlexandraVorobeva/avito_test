from datetime import date
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = "income"
    OUTCOME = "outcome"


class OperationBase(BaseModel):
    user_id: int
    date: date
    kind: OperationKind
    amount: float
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationCreate(OperationBase):
    pass
