from util.Connection import Connection


class CustomerDao:
    def __init__(self):
        self.conn = None

    def insertCustomer(self, customer_info):
        """
        Method to insert Customer record into the database
        Parameters
        ----------
        customer_info : the customer information payload

        Returns
        -------
        None
        """
        try:
            self.conn = Connection().get_db_connection()
            customer_name = customer_info.get("customer_name")
            phone_number = customer_info.get("phone_number")
            self.conn.execute("INSERT INTO customer(phone_number, customer_name) VALUES (?, ?)",
                              (phone_number, customer_name))
            self.conn.commit()
            self.conn.close()
            return "Customer information Inserted Successfully"
        except Exception as e:
            return "The customer wasn't created because of {}".format(str(e))

    def fetchAllCustomers(self):
        try:
            self.conn = Connection().get_db_connection()
            cursor = self.conn.cursor()
            customer_records = cursor.execute("SELECT * FROM customer;").fetchall()
            return [dict(row) for row in customer_records]
        except Exception as e:
            return "The customers cannot be fetched because of {}".format(str(e))
