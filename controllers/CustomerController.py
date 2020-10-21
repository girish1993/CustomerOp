from util.ComplianceChecks import ComplianceChecks
from services.CustomerServices import CustomerServices


class CustomerController:

    def __init__(self):
        """
        Constructor for the Customer Controller class
        """
        self.payload = None
        self.compliance_tool = None

    def create_customer(self, payload):
        """
        Method to create customer record in the database
        Parameters
        ----------
        payload : The customer information object

        Returns
        -------
        Message : String
            Message to indicate the status of the message
        """
        # TODO : This has to be moved to the service layer
        self.payload = payload
        self.compliance_tool = ComplianceChecks(self.payload)
        try:
            if self.compliance_tool.check_payload_compliance_for_keys() \
                    and self.compliance_tool.check_payload_compliance_for_values():
                return CustomerServices().createCustomer(self.payload)
            else:
                return "The customer information is not compliant to the business rules."
        except BaseException as b:
            return str(b)
        except KeyError as k:
            return str(k)

    @staticmethod
    def fetchAllCustomers():
        """
        Method to fetch all customer records from the database
        Returns
        -------
        List of user records as list of Dictionaries.
        """
        return CustomerServices().fetchAllCustomers()

    @staticmethod
    def search_customer_by_phone(search_phone_number):
        """
        Method to search customers in the database by phone number
        Returns
        -------
        A list of customer records with phone number matching the provided query string
        """
        return CustomerServices().get_customers_by_phone_number(search_phone_number)