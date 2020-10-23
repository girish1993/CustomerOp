from app.daos.CustomerDao import CustomerDao
from app.util.ComplianceChecks import ComplianceChecks
from app.util.FileOperations import FileOperations
"""
Service Layer for the Customer DAO
"""


class CustomerServices:

    def __init__(self):
        """
        Constructor for CustomerServices class
        """
        self.customer_info = None
        self.compliance_tool = None

    def createCustomer(self, payload):
        """
        Service Method to create a customer
        Parameters
        ----------
        payload : the customer payload

        Returns
        -------
        Message : String
            the status of the insertion operation
        """

        self.customer_info = payload
        self.compliance_tool = ComplianceChecks(self.customer_info)
        try:
            if self.compliance_tool.check_payload_compliance_for_keys() \
                    and self.compliance_tool.check_payload_compliance_for_values():
                return CustomerDao().insertCustomer(self.customer_info)
            else:
                return "The customer information is not compliant to the business rules."
        except BaseException as b:
            return "Customer could not be created because {}".format(str(b))
        except KeyError as k:
            return "Customer could not be created because {}".format(str(k))

    @staticmethod
    def fetchAllCustomers():
        """
        Method to fetch all the customer records in the database
        Returns
        -------
        A list of dictionaries where each dictionary is a customer record
        """
        return CustomerDao().fetch_all_customers()

    @staticmethod
    def get_customers_by_phone_number(search_phone_number):
        """
        Pattern searching for customers by their phone number
        Parameters
        ----------
        search_phone_number :

        Returns
        -------

        """
        return CustomerDao().fetch_customers_by_phone_number(search_phone_number)

    @staticmethod
    def readCsv_and_insert_into_database(path_to_file):
        """
        Method to read the csv file and grab the records in the csv
        Parameters
        ----------
        path_to_file : String
            path to the file

        Returns
        -------
        The database operation message.
        """
        try:
            file_content = FileOperations(path_to_file=path_to_file).read_file_content_and_return_records()
            return CustomerDao().insertManyCustomers(file_content)
        except FileNotFoundError as f:
            return "The import didn't work because {}".format(str(f))
