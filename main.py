from flask import Flask, jsonify
from flask import request
from controllers.CustomerController import CustomerController

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)


# sanity check route
@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to Customer Management System'


@app.route('/customer/create', methods=['POST'])
def createCustomerRecord():
    request_payload = request.get_json()
    result = CustomerController().create_customer(request_payload)
    return jsonify(result)


@app.route('/customer/search', methods=['POST'])
def searchCustomer():
    return jsonify('hello!')


@app.route('/customer/showAll', methods=['GET'])
def showAllCustomers():
    result = CustomerController().fetchAllCustomers()
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=DEBUG)
