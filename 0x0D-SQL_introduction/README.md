mysql -uroot or mysql -uroot -p or mysql -ujuk -p -hlocalhost
SHOW DATABASES;
USE your_database;
SHOW TABLES; or DESCRIBE;
EXIT; or \q

Users:
    SELECT user, host FROM mysql.user;
    SELECT * FROM mysql.user WHERE user = 'root' AND host = 'localhost';
    SHOW GRANTS
    SELECT CURRENT_USER();
    DROP USER 'username'@'localhost';
    REVOKE ALL PRIVILEGES ON *.* FROM 'username'@'host';
    REVOKE permission ON database_name.table_name FROM 'username'@'host';
-- Always flush privileges
    FLUSH PRIVILEGES;


Constraints:
    NOT NULL
    UNIQUE
    PRIMARY KEY
    FOREIGN KEY
    ENUM
    SET

GRANT
    CREATE USER
    GRANT privilege [,privilege],.. 
    ON privilege_level 
    TO account_name;
    example (global privilege):
        GRANT SELECT 
        ON *.* 
        TO bob@localhost;
    global privilege = *.*, DATABASE.*, DATABASE.TABLES
    column =    SELECT (employeeNumner,lastName, firstName,email), 
                UPDATE(lastName)
                ON TABLES
    Stored routine =    GRANT EXECUTE 
                        ON PROCEDURE CheckCredit
                        TO bob@localhost;
    Proxy user =    GRANT PROXY 
                    ON root
                    TO alice@localhost;
