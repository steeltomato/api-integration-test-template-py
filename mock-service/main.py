from fastapi import FastAPI
from models.customer import Customer, CustomerRequest
from models.response import (
    CreateCustomerResponse,
    DeleteCustomerResponse,
    GetCustomerResponse,
    GetCustomersResponse,
    UpdateCustomerResponse,
)


app = FastAPI()

# Internal DB for tracking mock state
customers = [
    Customer(id=1, name="bob", email="bob@test.com"),
    Customer(id=2, name="joe", email="joe@test.com"),
    Customer(id=3, name="jim", email="jim@test.com"),
]


@app.get("/customer", response_model=GetCustomersResponse, name="customer:list")
async def getCustomers() -> GetCustomersResponse:
    return GetCustomersResponse(customers=customers)


@app.get("/customer/{id}", response_model=GetCustomerResponse, name="customer:get", response_model_exclude_unset=True)
async def getCustomer(id: int) -> GetCustomerResponse:
    cust = custForId(id)

    if cust is None:
        return GetCustomerResponse(errors=["Failed to find customer with id {id}"])

    return GetCustomerResponse(customer=cust)


@app.put("/customer", response_model=CreateCustomerResponse, name="customer:create")
async def createCustomer(customer: CustomerRequest) -> CreateCustomerResponse:
    print(vars(customer))
    nextId = max([c.id for c in customers]) + 1
    newCustomer = Customer(id=nextId, name=customer.name, email=customer.email)
    customers.append(newCustomer)
    return CreateCustomerResponse(customer=newCustomer)


@app.patch(
    "/customer/{id}", response_model=UpdateCustomerResponse, name="customer:update", response_model_exclude_unset=True
)
async def updateCustomer(id: int, customer: CustomerRequest) -> UpdateCustomerResponse:
    cust = custForId(id)

    if cust is None:
        return UpdateCustomerResponse(errors=["Failed to find customer with id {id}"])

    if customer.name is not None:
        cust.name = customer.name
    if customer.email is not None:
        cust.email = customer.email

    return UpdateCustomerResponse(customer=cust)


@app.delete(
    "/customer/{id}", response_model=DeleteCustomerResponse, name="customer:delete", response_model_exclude_unset=True
)
async def deleteCustomer(id: int) -> DeleteCustomerResponse:
    cust = custForId(id)

    if cust is None:
        return DeleteCustomerResponse(errors=["Failed to find customer with id {id}"])

    customers.remove(cust)

    return DeleteCustomerResponse()


def custForId(id: int):
    return next((c for c in customers if c.id == id), None)
