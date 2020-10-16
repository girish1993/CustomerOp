import re

class CustomerController:

    def __init__(self, payload):
        self.payload = payload
        self.flag = False
        self.CUSTOMER_NAME = "customer_name"
        self.PHONE_NUMBER = "phone_number"

    def check_payload_compliance_for_keys(self):

        if not len(self.payload):
            raise BaseException("Customer details cannot be empty")

        if type(self.payload) == dict and (
                (self.CUSTOMER_NAME not in self.payload) or (self.PHONE_NUMBER not in self.payload)):
            raise KeyError("Customer information should have customer_name and phone_number")

        if type(self.payload) == list:
            if not (all(self.CUSTOMER_NAME in each_customer for each_customer in self.payload)) \
                    and (all(self.PHONE_NUMBER in each_customer for each_customer in self.payload)):
                raise KeyError("When provided with a list of customers, each customer should have customer name and "
                               "phone number")

        print("The provided Customer has the necessary information")
        self.flag = True





