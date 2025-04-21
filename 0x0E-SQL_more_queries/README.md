# 0x0E. SQL - More Queries

This project builds on the foundations of SQL by exploring more advanced query techniques, user management, permissions, and table relationships. The focus is on MySQL database management and complex data retrieval operations.

## Learning Objectives

By completing this project, you'll be able to:

- Create new MySQL users and manage privileges
- Understand the concepts of PRIMARY KEY and FOREIGN KEY
- Use constraints like NOT NULL and UNIQUE
- Retrieve data from multiple tables using JOIN and UNION
- Create and use subqueries effectively
- Handle database relationships: one-to-one, one-to-many, and many-to-many
- Apply advanced query techniques to filter and aggregate data

## MySQL User Management

### Creating Users and Granting Privileges

MySQL allows for the creation of users with specific access privileges:

```sql
-- Create a new user
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

-- Grant specific privileges
GRANT SELECT, INSERT ON database_name.table_name TO 'username'@'host';

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'username'@'host';

-- Apply changes
FLUSH PRIVILEGES;
```

### Viewing User Privileges

```sql
-- View privileges for a specific user
SHOW GRANTS FOR 'username'@'host';
```

## Database and Table Design

### Constraints in MySQL Tables

Constraints are rules applied to data columns to enforce data integrity:

- **NOT NULL**: Ensures a column cannot have NULL value
- **UNIQUE**: Ensures all values in a column are different
- **PRIMARY KEY**: Uniquely identifies each record in a table
- **FOREIGN KEY**: Links data between tables, maintaining referential integrity
- **DEFAULT**: Sets a default value for a column
- **AUTO_INCREMENT**: Automatically assigns a unique number

### Creating Tables with Constraints

```sql
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    unique_column VARCHAR(100) UNIQUE,
    status ENUM('active', 'inactive') DEFAULT 'active',
    foreign_id INT,
    FOREIGN KEY (foreign_id) REFERENCES other_table(id)
);
```

## Advanced Query Techniques

### Joining Tables

Joins combine rows from multiple tables based on related columns:

```sql
-- INNER JOIN: Returns matching records from both tables
SELECT cities.name, states.name 
FROM cities 
INNER JOIN states ON cities.state_id = states.id;

-- LEFT JOIN: Returns all records from left table and matching from right
SELECT shows.title, genres.name 
FROM shows 
LEFT JOIN show_genres ON shows.id = show_genres.show_id 
LEFT JOIN genres ON show_genres.genre_id = genres.id;
```

### Subqueries

Subqueries are queries nested inside another query:

```sql
-- Find cities in California using a subquery
SELECT name FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
```

### Aggregating Data

```sql
-- Count shows by genre
SELECT genres.name, COUNT(show_genres.show_id) AS number_of_shows
FROM genres
JOIN show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
```

## Project Files

This directory contains SQL scripts demonstrating various MySQL operations:

| File | Description |
|------|-------------|
| 0-privileges.sql | Lists privileges of MySQL users |
| 1-create_user.sql | Creates a MySQL server user with all privileges |
| 2-create_read_user.sql | Creates a database and user with SELECT privilege |
| 3-force_name.sql | Creates a table with a NOT NULL constraint |
| 4-never_empty.sql | Creates a table with a default value |
| 5-unique_id.sql | Creates a table with a UNIQUE constraint |
| 6-states.sql | Creates a database and table using AUTO_INCREMENT |
| 7-cities.sql | Creates a table with a FOREIGN KEY constraint |
| 8-cities_of_california_subquery.sql | Uses a subquery to list cities |
| 9-cities_by_state_join.sql | Lists cities with their states using INNER JOIN |
| 10-genre_id_by_show.sql | Lists shows with at least one genre linked |
| 11-genre_id_all_shows.sql | Lists all shows with their linked genres using LEFT JOIN |
| 12-no_genre.sql | Lists shows without a linked genre |
| 13-count_shows_by_genre.sql | Lists genres with the number of shows linked to them |
| 14-my_genres.sql | Lists genres of a specific show |
| 15-comedy_only.sql | Lists comedy shows |
| 16-shows_by_genre.sql | Lists all shows and their genres |
| 100-not_a_comedy.sql | Lists shows that are not comedies |
| 101-not_a_comedy.sql | Lists shows without the comedy genre |
| 102-rating_shows.sql | Lists shows by their rating |
| 103-rating_genres.sql | Lists genres by their rating |

## Usage Examples

### Listing User Privileges

```bash
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

### Creating a Database and Tables

```bash
$ cat 6-states.sql | mysql -hlocalhost -uroot -p
```

### Running Complex Queries

```bash
$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

## Requirements

- All scripts should be executed on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
- All files must end with a new line and start with a comment describing the task
- Scripts should not contain SET statements

## Debugging SQL Scripts

If your SQL script isn't working as expected:

1. Use the MySQL command-line client to test queries interactively
2. Check for syntax errors by running the script in verbose mode
3. Verify that the database and tables exist before querying them
4. Ensure proper permissions for the user executing the queries
5. Test complex queries part by part to isolate issues

```bash
# Interactive mode for testing
mysql -hlocalhost -uroot -p

# Check for syntax errors
mysql -hlocalhost -uroot -p --verbose < your_script.sql
```

## Resources

- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL Joins Explained](https://www.w3schools.com/sql/sql_join.asp)
- [MySQL Constraints](https://dev.mysql.com/doc/refman/8.0/en/constraints.html)
- [Subqueries in SQL](https://www.mysqltutorial.org/mysql-subquery/)
- [MySQL User Management](https://dev.mysql.com/doc/refman/8.0/en/user-account-management.html)
