# CustomerOp

This application showcases the creation of REST APIs in Python and how we can use Web Programming Frameworks
like FLASK to create quick, reliable and efficient solutions. 


## About 

In this project, we have REST API end points for a Customer management system that serve various different functionality.
The functionality can be broadly classified into 2 categories:
- To create a new customer
- To search a customer

We are dealing with customer information in terms of 2 attributes for now. 
1. customer's phone number
2. customer's name

The aim of the project is to facilitate the aforementioned operations through our application.


## Design Strategy

### Database Layer
With regards to designing the database layer, the following aspects were considered:

- size of the data
- number of attributes
- ease of scaling (introduction of additional attributes and accommodating more volume)
- need for a transactional based database management system. (ACID properties)
- compatibility with the chosen programming framework - **Flask**.

Based on all these considerations, [**SqlLite3**](https://docs.python.org/3/library/sqlite3.html) was chosen as the best candidate to manage the data
of the application.

The following schema was used for the database layer.
---schema

### Code base
The code base has been designed from according _MVC-like_ design patter. In this design pattern, we will be making use of
several layers in the backend which include:
1. controller - The gateway layer which interacts with the client application/external application
2. services - The business logic layer which checks and implements business logic and checks for compliance checks.
3. DAO - The layer closest to the Database layer that houses the methods and functions to operate on the database layer
mostly in the form of CRUD operations.

--- dig

The code base has good coverage in terms of unit tests for each of the layers as well.

### API design
The project basically has 5 API end points to work with
1. `/` -> A Base API end point to show the Home Page of the Application.
2. `/customer/create` -> API end point to create a single customer record. The API expects the payload to be in JSON
format with a simple key value format. For example : `{'customer_name':'John Doe','phone_number':'12345678901'}` is an 
acceptable payload. In case of violation of any of the key and value format, an appropriate error message would be shown.
3. `/customer/showAll` -> API end point to show all the customer records in the database. The response will be shown as a
list/Array of JSON objects where each customer JSON object represents a customer record.
4. `/customer/search?phone=<search_string>` -> API end point to search customer records based on the search string. 
    For instance,  `/customer/search?phone=3455` will fetch all customer records whose phone numbers start with '3455'.
5. `/customer/importCsv` -> API end point that will create many customer records in bulk. The CSV file should have headers
of certain format and has to be placed in certain folder in the project. The expected CSV file is available under `/data/customer_information.csv`.
Also the app expects the CSV file to be of the same name as well. 


## How to run the application.

The app is easy to install and run. The application has a **Dockerized** setup ready.

Steps to run the application:

- Clone the repo using the command `git clone https://github.com/girish1993/CustomerOp.git`
- Navigate to the root directory of the cloned repository on your machine.
- Run the command to start the application 
`docker-compose up -d` <br>
**NOTE:** docker and docker-compose must be installed on the local machine. If not, simply run the script using the command
`sh start.sh` to start the application.

- In case, you want to import a CSV data into the application, input the path of the CSV in `docker-compose.yml` here:

-- image

- Head over to the browser and type `http://localhost:5000/` This should show the message `Welcome to Customer Management System`
indicating the application is up and running.

**NOTE:** except the API end point `/customer/create` , all the other API end points are GET requests. That is, they can be directly used from the browser.
However, to create a customer record using `/customer/create` make use of REST client like POSTMAN to create customers.   

