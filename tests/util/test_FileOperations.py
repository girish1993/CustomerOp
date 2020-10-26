import os

import pandas as pd
import pytest

from app.util.FileOperations import FileOperations

TEST_CUSTOMER_DATA_CORRECT_CSV = "tests/daos/test_customer_data.csv"
TEST_CUSTOMER_DATA_INCORRECT_CSV = "tests/daos/test_customers_info_data.csv"


def test_check_if_file_does_not_exist_returns_False():
    path_to_file = os.path.join(os.getcwd(), TEST_CUSTOMER_DATA_INCORRECT_CSV)
    result = FileOperations(path_to_file=path_to_file).is_file_exists()
    assert False == result


def test_check_if_file_exists_returns_True():
    path_to_file = os.path.join(os.getcwd(), TEST_CUSTOMER_DATA_CORRECT_CSV)
    result = FileOperations(path_to_file=path_to_file).is_file_exists()
    assert True == result


def test_read_file_contents_when_file_doesnt_exist_throws_exception(mocker):
    mocker.patch.object(FileOperations, 'is_file_exists', return_value=False)
    with pytest.raises(FileNotFoundError, match="The file 'customer_information.csv' is not found under /data"):
        FileOperations(TEST_CUSTOMER_DATA_INCORRECT_CSV).read_file_content_and_return_records()


def test_read_file_contents_when_file_exist_gives_list_content(mocker):
    path_to_file = os.path.join(os.getcwd(), TEST_CUSTOMER_DATA_CORRECT_CSV)
    test_data = pd.read_csv(path_to_file)
    test_data["phone_number"] = test_data["phone_number"].apply(str)
    test_data_records = list(test_data.to_records(index=False))
    mocker.patch.object(FileOperations, 'is_file_exists', return_value=True)
    result = FileOperations(path_to_file).read_file_content_and_return_records()
    assert test_data_records == result
