DROP TABLE IF EXISTS customer;

CREATE TABLE customer(
    phone_number TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL
);