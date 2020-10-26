import os
from flask import Flask, jsonify
from flask import request
from app.controllers.CustomerController import CustomerController

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
DATA_FILE_PATH = "data/customer_information.csv"

# sanity check route
@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to Customer Management System'


# End Point to create a customer record
@app.route('/customer/create', methods=['POST'])
def create_customer_record():
    request_payload = request.get_json()
    result = CustomerController.create_customer(request_payload)
    return jsonify(result)


# End Point to search customer records by phone_number
@app.route('/customer/search', methods=['GET'])
def search_customer():
    search_phone_number = request.args.get('phone')
    result = CustomerController.search_customer_by_phone(search_phone_number)
    return jsonify(result)


# End Point to retrieve all customer records in the Database
@app.route('/customer/showAll', methods=['GET'])
def show_all_customers():
    result = CustomerController.fetchAllCustomers()
    return jsonify(result)


# End Point to retrieve all customer records in the Database
@app.route('/customer/importCsv', methods=['GET'])
def import_customer_csv_data_into_database():
    path_to_file = os.path.join(os.getcwd(), DATA_FILE_PATH)
    result = CustomerController.import_customer_csv(path_to_file)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=DEBUG)
