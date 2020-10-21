from daos.CustomerDao import CustomerDao

"""
Service Layer for the Customer DAO
"""


class CustomerServices:

    def __init__(self):
        """
        Constructor for CustomerServices class
        """
        self.customer_info = None

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
        return CustomerDao().insertCustomer(self.customer_info)

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
        return CustomerDao().fetch_customers_by_phone_number(search_phone_number)
