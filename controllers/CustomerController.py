from util.ComplianceChecks import ComplianceChecks
from services.CustomerServices import CustomerServices


class CustomerController:

    def __init__(self):
        """
        Constructor for the Customer Controller class
        """

    @staticmethod
    def create_customer(payload):
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
        return CustomerServices().createCustomer(payload=payload)

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

    def import_customer_csv(self, path_to_file):
        """
        Method to import csv data and populate the database with records
        Returns
        -------

        """
        return CustomerServices().readCsv_and_insert_into_database(path_to_file)