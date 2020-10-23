from app.util.Connection import Connection


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

    def fetch_all_customers(self):
        """
        Method to return all the customers in the database
        Returns
        -------
        list of customer records present in the database
        """
        try:
            self.conn = Connection().get_db_connection()
            cursor = self.conn.cursor()
            customer_records = cursor.execute("SELECT * FROM customer;").fetchall()
            self.conn.close()
            return [dict(row) for row in customer_records]
        except Exception as e:
            return "The customers cannot be fetched because of {}".format(str(e))

    def fetch_customers_by_phone_number(self, search_phone_number):
        """
        Method to search customers by phone number
        Parameters
        ----------
        search_phone_number : number to be searched

        Returns
        -------
        If found a list of customers whose phone numbers are matching the search string provided.
        """
        try:
            self.conn = Connection().get_db_connection()
            search_str = search_phone_number + "%"
            cursor = self.conn.cursor()
            customer_records = cursor.execute("SELECT * FROM customer WHERE phone_number LIKE (?) order by "
                                              "customer_name", (search_str,)).fetchall()
            self.conn.close()
            if len(customer_records):
                return [dict(row) for row in customer_records]
            else:
                return "No customers present with the given number"
        except Exception as e:
            return "The customers cannot be fetched because of {}".format(str(e))

    def insertManyCustomers(self, file_content):
        """
        Method to insert multiple customer records at once.
        Parameters
        ----------
        file_content :  List of customer records

        Returns
        -------
        Operation status : String
        """
        try:
            self.conn = Connection().get_db_connection()
            self.conn.executemany("INSERT INTO customer(phone_number, customer_name) VALUES (?, ?)",
                                  file_content)
            self.conn.commit()
            self.conn.close()
            return "{} customer records inserted into the database successfully".format(len(file_content))
        except Exception as e:
            return "The customers could not be created because of {}".format(str(e))
