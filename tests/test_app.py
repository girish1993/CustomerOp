"""
    Test suite to test the routes in the application
"""

import os
from unittest.mock import patch, MagicMock


def test_home_returns_expected_message(client):
    response = client.get('/')
    assert b"Welcome to Customer Management System" == response.data


def test_home_returns_200_status(client):
    response = client.get('/')
    assert "200 OK" == response.status


def test_create_customer_record_whenNonComplaintValues_returnsErrorMessage(client):
    response = client.post('/customer/create', json={"customer_name": "girish bhatta", "phone_number": "111221122"})
    assert b'"The customer information is not compliant to the business rules."\n' == response.data


def test_create_customer_record_whenNonComplaintKeys_returnsErrorMessage(client):
    response = client.post('/customer/create', json={"custame": "girish bhatta", "phone_number": "111221122"})
    assert b'"Customer could not be created because \'Customer information should have customer_name and ' \
           b'phone_number\'"\n' == response.data


def test_create_customer_record_whenCompliant_insertsRecordInDb(client):
    response = client.post('/customer/create', json={"customer_name": "girish bhatta", "phone_number": "11111111111"})
    assert b'"Customer information Inserted Successfully"\n' == response.data
    assert "200 OK" == response.status


def test_create_customer_record_whenDuplicate_record_throwsIntegrity_constraint_error(client):
    response = client.post('/customer/create', json={"customer_name": "girish bhatta", "phone_number": "11111111111"})
    response2 = client.post('/customer/create', json={"customer_name": "girish bhatta", "phone_number": "11111111111"})
    assert b'"The customer wasn\'t created because of UNIQUE constraint failed: customer.phone_number"\n' == response2.data
    assert "200 OK" == response.status


def test_showAll_Customers_whenNo_Customers_Are_Present(client):
    response = client.get('/customer/showAll')
    assert b'[]\n' == response.data


def test_showAll_Customers_when2CustomersAre_Present(client):
    client.post('/customer/create', json={"customer_name": "john doe", "phone_number": "43434343434"})
    client.post('/customer/create', json={"customer_name": "jane doe", "phone_number": "99999999999"})
    show_all_response = client.get('/customer/showAll')
    assert b'[{"customer_name":"john doe","phone_number":"43434343434"},{"customer_name":"jane doe",' \
           b'"phone_number":"99999999999"}]\n' == show_all_response.data


def test_search_customer_with_incorrect_queryparam_throws_error(client):
    response = client.get('/customer/search?pho=1')
    assert b'"The customers cannot be fetched because of unsupported operand type(s) for +: \'NoneType\' and \'str\'"\n' == \
           response.data


def test_search_customer_with_correct_queryparam_shows_no_result(client):
    response = client.get('/customer/search?phone=1')
    assert b'"No customers present with the given number"\n' == response.data


def test_search_customer_when_customers_are_present(client):
    client.post('/customer/create', json={"customer_name": "john doe", "phone_number": "43434343434"})
    client.post('/customer/create', json={"customer_name": "jane doe", "phone_number": "43777777777"})
    search_response = client.get('/customer/search?phone=43')
    assert b'[{"customer_name":"jane doe","phone_number":"43777777777"},{"customer_name":"john doe",' \
           b'"phone_number":"43434343434"}]\n' == search_response.data


def test_importCsv_whenNoFileIsPresent_throwError(client, mocker):
    path_to_file = os.path.join(os.getcwd(), "customer_information.csv")
    mocker.patch('app.main.DATA_FILE_PATH', return_value=os.path.join(os.getcwd(), path_to_file))
    response = client.get('/customer/importCsv')
    assert b'"The import didn\'t work because The file \'customer_information.csv\' is not found under /data"\n' == response.data


def test_importCsv_whenFile_Is_Present_Succeeds(client):
    response = client.get('/customer/importCsv')
    assert b'"100 customer records inserted into the database successfully"\n' == response.data
