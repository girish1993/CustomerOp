from app.services.CustomerServices import CustomerServices
from app.daos.CustomerDao import CustomerDao
from app.util.ComplianceChecks import ComplianceChecks
from app.util.FileOperations import FileOperations
import pandas as pd

INFORMATION_CSV = "/data/customer_information.csv"
PHONE_NUMBER = "1234"


def get_payload():
    return {"customer_name": "girish bhatta", "phone_number": "11111111111"}


def test_create_customer_when_keysInvalid_in_payload(mocker):
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_keys', return_value=False)
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_values', return_value=True)
    result = CustomerServices().createCustomer(get_payload())
    assert "The customer information is not compliant to the business rules." == result


def test_create_customer_whenValuesInvalid_in_payload(mocker):
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_keys', return_value=True)
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_values', return_value=False)
    result = CustomerServices().createCustomer(get_payload())
    assert "The customer information is not compliant to the business rules." == result


def test_create_customer_when_compliance_raisesBaseException(mocker):
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_keys', side_effect=BaseException("Customer "
                                                                                                         "details "
                                                                                                         "cannot be "
                                                                                                         "empty"))
    result = CustomerServices().createCustomer({})
    assert "Customer could not be created because Customer details cannot be empty" == result


def test_create_customer_when_compliance_raises_key_exception(mocker):
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_keys', side_effect=KeyError("Customer "
                                                                                                    "information "
                                                                                                    "should have "
                                                                                                    "customer_name "
                                                                                                    "and "
                                                                                                    "phone_number"))
    result = CustomerServices().createCustomer({})
    assert "Customer could not be created because 'Customer information should have customer_name and phone_number'" \
           == result


def test_create_customer_when_compliant_creation_successful(mocker):
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_keys', return_value=True)
    mocker.patch.object(ComplianceChecks, 'check_payload_compliance_for_values', return_value=True)
    mocker.patch.object(CustomerDao, 'insertCustomer', return_value="Customer created Successfully")

    result = CustomerServices().createCustomer(get_payload())
    assert "Customer created Successfully" == result


def test_show_all_customers_returns_no_records(mocker):
    mocker.patch.object(CustomerDao, 'fetch_all_customers', return_value=[])
    result = CustomerServices.fetchAllCustomers()
    assert [] == result


def test_show_all_customers_returns_single_record(mocker):
    mocker.patch.object(CustomerDao, 'fetch_all_customers', return_value=[get_payload()])
    result = CustomerServices.fetchAllCustomers()
    assert [get_payload()] == result


def test_get_customer_by_phone_number_returns_nothing(mocker):
    mocker.patch.object(CustomerDao, 'fetch_customers_by_phone_number',
                        return_value="No customers present with the given number")
    result = CustomerServices.get_customers_by_phone_number(PHONE_NUMBER)
    assert "No customers present with the given number" == result


def test_get_customer_by_phone_number_returns_records(mocker):
    mocker.patch.object(CustomerDao, 'fetch_customers_by_phone_number',
                        return_value=[get_payload()])
    result = CustomerServices.get_customers_by_phone_number(PHONE_NUMBER)
    assert [get_payload()] == result


def test_readCsv_and_insert_into_database_when_file_isNot_present(mocker):
    mocker.patch.object(FileOperations, 'read_file_content_and_return_records',
                        side_effect=FileNotFoundError("The file 'customer_information.csv' is not found under /data"))
    result = CustomerServices.readCsv_and_insert_into_database(INFORMATION_CSV)
    assert "The import didn't work because The file 'customer_information.csv' is not found under /data" == result


def test_readCsv_and_insert_into_database_file_is_present_succeeds(mocker):
    mocker.patch.object(FileOperations, 'read_file_content_and_return_records',
                        return_value=[get_payload()])
    mocker.patch.object(CustomerDao,'insertManyCustomers', return_value="Customer CSV data imported and created "
                                                                        "successfully")
    result = CustomerServices.readCsv_and_insert_into_database(INFORMATION_CSV)
    assert "Customer CSV data imported and created successfully" == result
