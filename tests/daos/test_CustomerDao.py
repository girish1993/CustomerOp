import sqlite3
from app.util.Connection import Connection
from app.daos.CustomerDao import CustomerDao
import pandas as pd
import os


def get_Connection():
    database = "app.db"
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    return conn


def create_customer():
    return {"customer_name": "John Doe", "phone_number": "12345678901"}


def test_insertCustomer_errors_out(mocker):
    mocker.patch.object(Connection, 'get_db_connection', return_value=get_Connection())
    result = CustomerDao().insertCustomer(create_customer())
    assert "Customer information Inserted Successfully" == result


def test_fetch_all_customers(mocker):
    mocker.patch.object(Connection, 'get_db_connection', return_value=get_Connection())
    result = CustomerDao().fetch_all_customers()
    assert [{'customer_name': 'John Doe', 'phone_number': '12345678901'}] == result


def test_search_customer_by_phone(mocker):
    mocker.patch.object(Connection, 'get_db_connection', return_value=get_Connection())
    result = CustomerDao().fetch_customers_by_phone_number("123")
    assert [{'customer_name': 'John Doe', 'phone_number': '12345678901'}] == result


def test_insert_many_customers(mocker):
    path_to_file = os.path.join(os.getcwd(), "tests/daos/test_customer_data.csv")
    test_data = pd.read_csv(path_to_file)
    test_data["phone_number"] = test_data["phone_number"].apply(str)
    test_data_records = list(test_data.to_records(index=False))
    mocker.patch.object(Connection, 'get_db_connection', return_value=get_Connection())
    result = CustomerDao().insertManyCustomers(test_data_records)
    assert "{} customer records inserted into the database successfully".format(len(test_data_records)) == result
