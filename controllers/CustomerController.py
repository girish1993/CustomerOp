from util.ComplianceChecks import ComplianceChecks


class CustomerController:

    def __init__(self, payload):
        self.payload = payload
        self.compliance_tool = ComplianceChecks(self.payload)

    def create_customer(self):
        try:
            if self.compliance_tool.check_payload_compliance_for_keys() \
                    and self.compliance_tool.check_payload_compliance_for_values():
                return "Customer Created"
            else:
                return "something wrong here"
        except BaseException as b:
            return str(b)
        except KeyError as k:
            return str(k)




