from util.ComplianceChecks import ComplianceChecks
from services.CustomerServices import CustomerServices


class CustomerController:

    def __init__(self):
        self.payload = None
        self.compliance_tool = None

    def create_customer(self, payload):
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
        return CustomerServices().fetchAllCustomers()
