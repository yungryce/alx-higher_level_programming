# SQL Introduction

This project introduces the fundamentals of SQL (Structured Query Language) and relational databases, focusing on MySQL. Through a series of increasingly complex exercises, you'll learn how to create, manipulate, and query databases using standard SQL commands.

## What is SQL?

SQL (Structured Query Language) is a standardized programming language specifically designed for managing and manipulating relational databases. It allows you to:

- Create, modify, and delete database structures
- Insert, update, and delete data
- Query data with powerful filtering and sorting capabilities
- Control access to data through security measures

## What is MySQL?

MySQL is an open-source relational database management system (RDBMS) that uses SQL. It's known for its:

- Reliability and performance
- Ease of use and flexibility
- Strong community support
- Cross-platform compatibility
- Widespread adoption in web applications

## Learning Objectives

By the end of this project, you will be able to:

- Create and delete databases
- Create tables with constraints
- Select data from tables with filtering
- Insert, update, and delete records
- Use basic SQL functions and subqueries
- Sort and filter query results
- Work with NULL values appropriately
- Import and export data
- Manage database character sets

## Requirements

- MySQL 8.0 (install using `sudo apt install mysql-server`)
- All SQL queries should be executable on MySQL 8.0
- SQL files should:
  - Start with a comment describing the task
  - End with a new line
  - Have the `.sql` extension
  - Contain only SQL code (no DDL statements like `-- MySQL dump`)
  - Follow standard SQL syntax

## Getting Started with MySQL

### Installation (Ubuntu)

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ sudo mysql_secure_installation
```

### Starting MySQL

```bash
$ sudo service mysql start
```

### Connecting to MySQL

```bash
$ mysql -u root -p
```

## Basic MySQL Commands Reference

### Login Commands

```sql
-- Connect as root with password
mysql -u root -p

-- Connect to specific database
mysql -u username -p database_name
```

### Database Operations

```sql
-- List all databases
SHOW DATABASES;

-- Create a database
CREATE DATABASE database_name;

-- Select a database to use
USE database_name;

-- Delete a database
DROP DATABASE database_name;
```

### Table Operations

```sql
-- List all tables in current database
SHOW TABLES;

-- Show table structure
DESCRIBE table_name;
SHOW CREATE TABLE table_name;

-- Create a table
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);

-- Delete a table
DROP TABLE table_name;

-- Modify table structure
ALTER TABLE table_name ADD column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;
```

### Data Manipulation

```sql
-- Insert data
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);

-- Update data
UPDATE table_name SET column1 = value1 WHERE condition;

-- Delete data
DELETE FROM table_name WHERE condition;

-- Select data
SELECT column1, column2, ... FROM table_name WHERE condition;

-- Sorting results
SELECT * FROM table_name ORDER BY column1 [ASC|DESC];

-- Limiting results
SELECT * FROM table_name LIMIT number;

-- Filtering with conditions
SELECT * FROM table_name WHERE column_name = value;
SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2;
SELECT * FROM table_name WHERE column_name IN (value1, value2, ...);
SELECT * FROM table_name WHERE column_name LIKE 'pattern%';
```

### Aggregate Functions

```sql
-- Count rows
SELECT COUNT(*) FROM table_name;

-- Sum values
SELECT SUM(column_name) FROM table_name;

-- Average value
SELECT AVG(column_name) FROM table_name;

-- Maximum value
SELECT MAX(column_name) FROM table_name;

-- Minimum value
SELECT MIN(column_name) FROM table_name;

-- Group results
SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;
```

### User Management

```sql
-- Create user
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'host';
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'host';

-- Apply privileges
FLUSH PRIVILEGES;

-- Remove privileges
REVOKE privilege ON database_name.* FROM 'username'@'host';

-- Delete user
DROP USER 'username'@'host';
```

### Constraints

```sql
-- Primary Key
CREATE TABLE table_name (
    id INT NOT NULL,
    name VARCHAR(100),
    PRIMARY KEY (id)
);

-- Foreign Key
CREATE TABLE orders (
    id INT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Unique
CREATE TABLE users (
    id INT,
    email VARCHAR(100) UNIQUE
);

-- Not Null
CREATE TABLE users (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL
);

-- Default Value
CREATE TABLE products (
    id INT,
    name VARCHAR(100),
    in_stock BOOLEAN DEFAULT true
);
```

### Import/Export

```sql
-- Import from SQL file
mysql -u username -p database_name < file.sql

-- Export to SQL file
mysqldump -u username -p database_name > file.sql
```

## Project Tasks

The tasks in this project gradually introduce core SQL concepts:

1. **Database listing**: View all available databases
2. **Database creation**: Create new databases
3. **Table management**: Create, list, and describe tables
4. **Data manipulation**: Insert, update, and delete records
5. **Queries**: Select records with various filtering and sorting options
6. **Functions**: Use aggregate functions like COUNT, AVG, SUM
7. **Advanced topics**: Work with character sets, constraints, and data analysis

## Common Data Types in MySQL

### Numeric Types
- `INT`: Standard integer
- `BIGINT`: Large integer
- `FLOAT`: Single-precision floating point
- `DOUBLE`: Double-precision floating point
- `DECIMAL(M,D)`: Fixed-point decimal (M digits, D after decimal)

### String Types
- `CHAR(size)`: Fixed-length string
- `VARCHAR(size)`: Variable-length string
- `TEXT`: Large text field
- `ENUM`: String with limited possible values

### Date/Time Types
- `DATE`: Date in YYYY-MM-DD format
- `TIME`: Time in HH:MM:SS format
- `DATETIME`: Date and time combined
- `TIMESTAMP`: Timestamp (often for tracking changes)

### Other Types
- `BOOLEAN`: True/false values
- `BLOB`: Binary Large Object (binary data)
- `JSON`: Native JSON data type (MySQL 5.7+)

## Best Practices

1. **Use appropriate data types**: Choose the most suitable type for your data
2. **Add indexes**: Improve query performance with proper indexing
3. **Use constraints**: Enforce data integrity with PRIMARY KEY, FOREIGN KEY, etc.
4. **Name conventions**: Use consistent naming for databases, tables, and columns
5. **Comment your SQL**: Add comments to explain complex queries
6. **Backup regularly**: Always have a backup strategy for your databases
7. **Use transactions**: Ensure data consistency for multiple operations
8. **Normalize data**: Organize data to reduce redundancy (up to 3NF)
9. **Secure your installation**: Set strong passwords and limit remote access
10. **Keep MySQL updated**: Apply security patches and updates regularly

## Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [DB-Engines Ranking](https://db-engines.com/en/ranking)
