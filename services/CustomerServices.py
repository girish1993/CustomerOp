from daos.CustomerDao import CustomerDao


class CustomerServices:

    def __init__(self):
        self.customer_info = None

    def createCustomer(self, payload):
        self.customer_info = payload
        return CustomerDao().insertCustomer(self.customer_info)

    def fetchAllCustomers(self):
        return CustomerDao().fetchAllCustomers()
