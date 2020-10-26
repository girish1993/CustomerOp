import re
import pytest
from app.util.ComplianceChecks import ComplianceChecks

PHONE_REGEX = re.compile(r"^[0-9]{11}$")
NAME_REGEX = re.compile(r"^[a-z ,.'-]+$", re.IGNORECASE)


def test_check_payload_compliance_checks_when_payload_is_empty():
    empty_payload = {}
    with pytest.raises(BaseException, match="Customer details cannot be empty"):
        ComplianceChecks(empty_payload).check_payload_compliance_for_keys()


def test_check_payload_compliance_checks_when_payload_does_not_have_keys():
    payload = {"custo_name": "test user"}
    with pytest.raises(KeyError, match="Customer information should have customer_name and phone_number"):
        ComplianceChecks(payload).check_payload_compliance_for_keys()


def test_check_payload_compliance_checks_when_payload_hasTheCorrectKeys():
    payload = {"customer_name": "test user", "phone_number": "11111111111"}
    result = ComplianceChecks(payload).check_payload_compliance_for_keys()
    assert True == result


def test_check_payload_values_non_compliant_values():
    payload = {"customer_name": "test 3435gddh4545r", "phone_number": "111111"}
    result = ComplianceChecks(payload).check_payload_compliance_for_values()
    assert False == result


def test_check_payload_values_with_compliant_values():
    payload = {"customer_name": "random user", "phone_number": "11111111111"}
    result = ComplianceChecks(payload).check_payload_compliance_for_values()
    assert True == result


def test_check_regex_values_when_name_is_compliant_and_phone_non_compliant():
    payload = {"customer_name": "random user", "phone_number": "111111111"}
    name_regex = NAME_REGEX
    phone_regex = PHONE_REGEX
    result = ComplianceChecks(payload).regex_value_checks(payload, name_regex=name_regex, phone_regex=phone_regex)
    assert False == result


def test_check_regex_values_when_name_is_non_compliant_and_phone_compliant():
    payload = {"customer_name": "randomr6868gsg", "phone_number": "12345678901"}
    name_regex = NAME_REGEX
    phone_regex = PHONE_REGEX
    result = ComplianceChecks(payload).regex_value_checks(payload, name_regex=name_regex, phone_regex=phone_regex)
    assert False == result


def test_check_regex_values_when_name_is_compliant_and_phone_compliant():
    payload = {"customer_name": "john Doe", "phone_number": "12345678901"}
    name_regex = NAME_REGEX
    phone_regex = PHONE_REGEX
    result = ComplianceChecks(payload).regex_value_checks(payload, name_regex=name_regex, phone_regex=phone_regex)
    assert True == result
