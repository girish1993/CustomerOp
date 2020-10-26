from app.services.CustomerServices import CustomerServices
from app.controllers.CustomerController import CustomerController

PHONE_NUMBER = "1111"


def get_payload():
    return {"customer_name": "girish bhatta", "phone_number": "11111111111"}


def test_create_customer_successfully(mocker):
    mocker.patch.object(CustomerServices, 'createCustomer', return_value="Customer record created successfully")
    result = CustomerController.create_customer(get_payload())
    assert "Customer record created successfully" == result


def test_show_all_customers_when_records_are_present(mocker):
    mocker.patch.object(CustomerServices, 'fetchAllCustomers', return_value=[get_payload()])
    result = CustomerController.fetchAllCustomers()
    assert [get_payload()] == result


def test_search_customer_by_phone_number(mocker):
    mocker.patch.object(CustomerServices, 'get_customers_by_phone_number', return_value=[get_payload()])
    result = CustomerController.search_customer_by_phone(PHONE_NUMBER)
    assert [get_payload()] == result


def test_import_customer_information_successfully(mocker):
    mocker.patch.object(CustomerServices, 'readCsv_and_insert_into_database', return_value="Customer records imported "
                                                                                           "successfully")
    result = CustomerController.import_customer_csv(PHONE_NUMBER)
    assert "Customer records imported successfully" == result
