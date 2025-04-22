# Python Object-Relational Mapping (ORM)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/MySQL-8.0-orange.svg" alt="MySQL 8.0">
  <img src="https://img.shields.io/badge/SQLAlchemy-1.4.x-red.svg" alt="SQLAlchemy 1.4.x">
  <img src="https://img.shields.io/badge/MySQLdb-2.0.x-green.svg" alt="MySQLdb 2.0.x">
</p>

## Introduction
This project connects two amazing worlds: Databases and Python!

In this project, you will learn how to use Object-Relational Mapping (ORM) to bridge the gap between Python objects and relational databases. We'll start with direct database connections using MySQLdb and then move to SQLAlchemy, a powerful ORM that allows you to interact with your database like you would with SQL.

The goal is to abstract the storage layer so you won't have to write SQL queries anymore, but just play with Python objects.

## Learning Objectives
By the end of this project, you should be able to explain:

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

## Requirements

### General
* All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* Files executed with MySQLdb version 2.0.x
* Files executed with SQLAlchemy version 1.4.x
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All files must be executable
* The length of your files will be tested using `wc`
* All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* You are not allowed to use `execute` with sqlalchemy

### Installation

#### Install and activate venv
```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Install MySQLdb
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

#### Install SQLAlchemy
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

## Project Tasks

<details>
<summary><strong>🔍 Direct Database Access with MySQLdb (Tasks 0-5)</strong></summary>

### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`.

### 1. Filter states
Write a script that lists all states with a name starting with N from the database `hbtn_0e_0_usa`.

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table where name matches the argument.

### 3. SQL Injection...
Write a script that takes in arguments and displays all values in the states table where name matches the argument, safe from SQL injection.

### 4. Cities by states
Write a script that lists all cities from the database `hbtn_0e_4_usa`.

### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state.
</details>

<details>
<summary><strong>🔧 Object-Relational Mapping with SQLAlchemy (Tasks 6-14)</strong></summary>

### 6. First state model
Write a python file that contains the class definition of a State and an instance Base = declarative_base().

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database `hbtn_0e_6_usa`.

### 8. First state
Write a script that prints the first State object from the database `hbtn_0e_6_usa`.

### 9. Contains `a`
Write a script that lists all State objects that contain the letter a from the database `hbtn_0e_6_usa`.

### 10. Get a state
Write a script that prints the State object with the name passed as argument from the database `hbtn_0e_6_usa`.

### 11. Add a new state
Write a script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.

### 12. Update a state
Write a script that changes the name of a State object from the database `hbtn_0e_6_usa`.

### 13. Delete states
Write a script that deletes all State objects with a name containing the letter a from the database `hbtn_0e_6_usa`.

### 14. Cities in state
Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
</details>

<details>
<summary><strong>🌟 Advanced Relationships (Tasks 100-102)</strong></summary>

### 100. Relationship states cities
Improve the files model_city.py and model_state.py to work with a relationship.

### 101. List relationship states cities
Write a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa.

### 102. Cities by states
List all City objects from the database hbtn_0e_101_usa, sorted by city id.
</details>

## MySQLdb vs SQLAlchemy: A Comparison

<table>
  <tr>
    <th>Feature</th>
    <th>MySQLdb</th>
    <th>SQLAlchemy</th>
  </tr>
  <tr>
    <td>Abstraction Level</td>
    <td>Low-level database driver</td>
    <td>High-level ORM framework</td>
  </tr>
  <tr>
    <td>Query Style</td>
    <td>Raw SQL strings</td>
    <td>Python objects and methods</td>
  </tr>
  <tr>
    <td>Results Format</td>
    <td>Tuples in a list</td>
    <td>Python objects</td>
  </tr>
  <tr>
    <td>Resource Management</td>
    <td>Manual connection and cursor handling</td>
    <td>Session-based with context management</td>
  </tr>
  <tr>
    <td>SQL Injection Protection</td>
    <td>Manual parameter binding</td>
    <td>Built-in by default</td>
  </tr>
  <tr>
    <td>Database Portability</td>
    <td>MySQL specific</td>
    <td>Multiple database backend support</td>
  </tr>
</table>

### MySQLdb Example
```python
#!/usr/bin/python3
import MySQLdb

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database_name")
cursor = db.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()

# Process results
for row in rows:
    print(row)

# Clean up
cursor.close()
db.close()
```

### SQLAlchemy Example
```python
#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Connect to database
engine = create_engine('mysql+mysqldb://username:password@localhost/database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Query database
states = session.query(State).order_by(State.id).all()

# Process results as Python objects
for state in states:
    print(f"{state.id}: {state.name}")

# Clean up
session.close()
```

## Benefits of Using ORM

1. **Productivity**: Write less code by using Python objects instead of SQL
2. **Maintainability**: Centralized schema definitions make changes easier
3. **DRY Principle**: No need to repeat SQL queries throughout your code
4. **Security**: Built-in protection against SQL injection
5. **Portability**: Switch database backends with minimal code changes
6. **Object-Oriented**: Work with familiar OO concepts rather than tables and rows

## Additional Resources

* [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
* [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
* [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
* [SQL Injection Prevention](https://bobby-tables.com/python)

---

*Remember: "Talk is cheap. Show me the code." - Linus Torvalds*
