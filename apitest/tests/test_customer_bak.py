import pytest
from apitest.client.customer_client import Customer, CustomerClient
from apitest.config import config
from apitest.tests.test_suite import TestSuite


@pytest.fixture(scope="class")
def customerClient():
    yield CustomerClient(config)


class TestCustomer(TestSuite):
    @pytest.mark.stable
    def test_list_customers(self, customerClient):
        response = customerClient.listCustomers()
        response.assert_ok()

    @pytest.mark.stable
    def test_get_customer(self, customerClient):
        response = customerClient.getCustomer(1)
        response.assert_ok()
        response.assert_jsonpath("customer.name", expected_value="bob")

    @pytest.mark.stable
    def test_crud(self, customerClient: CustomerClient):
        createRes = customerClient.createCustomer(Customer(name="Jane", email="jane@test.com"))
        createRes.assert_ok()
        createRes.assert_jsonpath("customer.name", expected_value="Jane")

        updateRes = customerClient.updateCustomer(createRes.json()["customer"]["id"], Customer(name="Janet"))
        updateRes.assert_ok()
        updateRes.assert_jsonpath("customer.name", expected_value="Janet")

        getRes = customerClient.getCustomer(updateRes.json()["customer"]["id"])
        getRes.assert_ok()
        getRes.assert_jsonpath("customer.name", expected_value="Janet")

        deleteRes = customerClient.deleteCustomer(getRes.json()["customer"]["id"])
        deleteRes.assert_ok()
