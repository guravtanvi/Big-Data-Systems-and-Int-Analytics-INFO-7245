## Big Data Systems and Int Analytics

## Labs

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 4 - SQL Alchemy

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=183kIAkFW17W4uYY-511ylLhZttSelI7q383qufLBMYc#0

## About

**This lab demonstrates how to leverage SQL concepts through a traditional Object-Oriented Programming approach with the help of SQLAlchemy.**

![sqlalchemy](https://user-images.githubusercontent.com/59846364/109201435-d72c1e00-776f-11eb-99b1-8b8571d925ef.jpg)


**What is SQLAlchemy?** 

SQLAlchemy is the Python-SQL toolkit and Object Relational Mapper that gives application developers the flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

SQLAlchemy Architecture:

![sqlalchemy-arch](https://user-images.githubusercontent.com/59846364/109200103-31c47a80-776e-11eb-86b1-b66a0d25a866.jpg)


## Requirements

**1. Configuring Python on system**

For Ubuntu/Linux:

```
sudo apt install python3
sudo apt install python3-pip
```

For Windows:

https://www.python.org/downloads/


**2. Configuring SQLAlchemy**

```
pip install sqlalchemy
pip install psycopg2-binary
```

**3. Setting up the relational PostgreSQL database**

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

## Use Cases and Test Results

#### Contents

- `customer.py` - A sample Python classes containing 5 attributes that we'd like to be converted to a table
- `main.py` - Insert data using the newly created class
- `queries.py` - Querying the table
- `base.py` contains the connection params to connect to the instance

**Enter the connection parameters to connect to the PostgreSQL server instance**

`postgresql://username:password@host:port/database`

Once the engine is created and data is inserted using `main.py` program, login to pgadmin console to verify the inserted data:


![sqlalchmey-pgadmin](https://user-images.githubusercontent.com/59846364/109202149-a8627780-7770-11eb-9e02-f18275a5bdeb.PNG)


Further, the `update_record()` function for updates a record into the database with updated name from **‘Jane Doe’** to **‘Ryan Gosling’**


![sqlalchmey-pgadmin-updated](https://user-images.githubusercontent.com/59846364/109203025-a947d900-7771-11eb-955a-ac28da0542aa.PNG)



