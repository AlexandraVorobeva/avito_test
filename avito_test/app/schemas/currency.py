from enum import Enum
from pydantic import BaseModel


class CurrencyKind(str, Enum):
    RUB = "RUB"
    USD = "USD"
    EUR = "EUR"
    CNY = "CNY"
