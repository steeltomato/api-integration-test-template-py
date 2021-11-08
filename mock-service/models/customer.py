from typing import Optional

from pydantic.main import BaseModel


class Customer(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[str]


class CustomerRequest(BaseModel):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]
