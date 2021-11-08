from typing import Optional

from pydantic.main import BaseModel

from .customer import Customer


class BaseResponse(BaseModel):
    message: str = ""
    errors: list = []


class GetCustomersResponse(BaseResponse):
    customers: Optional[list[Customer]]


class GetCustomerResponse(BaseResponse):
    customer: Optional[Customer]


class CreateCustomerResponse(BaseResponse):
    customer: Optional[Customer]


class UpdateCustomerResponse(BaseResponse):
    customer: Optional[Customer]


class DeleteCustomerResponse(BaseResponse):
    """empty"""
