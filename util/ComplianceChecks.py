import re

"""
A Utility class to provide means to test the validity of keys and values in the received payload.
"""


class ComplianceChecks:

    def __init__(self, payload):
        """
        Constructor for the compliance check class
        Parameters
        ----------
        payload : the customer information payload
        """
        self.payload = payload
        self.CUSTOMER_NAME = "customer_name"
        self.PHONE_NUMBER = "phone_number"
        self.key_flag = True
        self.value_flag = True

    def check_payload_compliance_for_keys(self):
        """
        Method to check the payload for compliance.
        Returns
        -------
        Boolean value to indicate the compliance of keys and values.

        """

        if not len(self.payload):
            self.key_flag = False
            raise BaseException("Customer details cannot be empty")

        if type(self.payload) == dict and (
                (self.CUSTOMER_NAME not in self.payload) or (self.PHONE_NUMBER not in self.payload)):
            self.key_flag = False
            raise KeyError("Customer information should have customer_name and phone_number")

        if type(self.payload) == list:
            if not (all(self.CUSTOMER_NAME in each_customer for each_customer in self.payload)) \
                    and (all(self.PHONE_NUMBER in each_customer for each_customer in self.payload)):
                self.key_flag = False
                raise KeyError("When provided with a list of customers, each customer should have customer name and "
                               "phone number")
        self.key_flag = True
        return self.key_flag

    def check_payload_compliance_for_values(self):
        """
        Method to check for the compliance of the values.
        :return: None
        """
        name_regex = re.compile(r"^[a-z ,.'-]+$", re.IGNORECASE)
        phone_regex = re.compile(r"^[0-9]{11}$")

        if type(self.payload) == list:
            for each_customer in self.payload:
                return self.regex_value_checks(each_customer, name_regex, phone_regex)
        elif type(self.payload) == dict:
            return self.regex_value_checks(self.payload, name_regex, phone_regex)

    def regex_value_checks(self, each_customer, name_regex, phone_regex):
        """
        Method to check the values against the regex
        Parameters
        ----------
        each_customer : customer information object
        name_regex : regex to match the name
        phone_regex : regex to match the phone

        Returns
        -------
        bool
        """

        if (name_regex.match(str(each_customer.get(self.CUSTOMER_NAME)))) and \
                (phone_regex.match(str(each_customer.get(self.PHONE_NUMBER)))):
            return self.value_flag
        else:
            self.value_flag = False
            return self.value_flag
