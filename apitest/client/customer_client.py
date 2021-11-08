from typing import Optional

from apiritif.http import HTTPResponse

from .base_client import BaseClient


class Customer(object):
    id: Optional[int]
    name: Optional[str]
    email: Optional[str]

    def __init__(self, name: str, email: str = None):
        self.name = name
        if email is not None:
            self.email = email


class CustomerClient(BaseClient):
    def __init__(self, config):
        super().__init__(config)

    def listCustomers(self) -> HTTPResponse:
        return self.api.get("/customer")

    def getCustomer(self, id: int) -> HTTPResponse:
        return self.api.get(f"/customer/{id}")

    def createCustomer(self, customer: Customer) -> HTTPResponse:
        return self.api.put("/customer", json=vars(customer))

    def updateCustomer(self, id: int, customer: Customer) -> HTTPResponse:
        return self.api.patch(f"/customer/{id}", json=vars(customer))

    def deleteCustomer(self, id: int) -> HTTPResponse:
        return self.api.delete(f"/customer/{id}")
