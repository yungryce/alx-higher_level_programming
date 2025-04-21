# Project Manifest: SQL More Queries

## Project Identity
- **Name**: SQL More Queries
- **Type**: Educational
- **Scope**: Advanced SQL Database Operations
- **Status**: Completed

## Technology Signature
- **Core**: MySQL 8.0
- **Query Language**: SQL
- **Environment**: Ubuntu 20.04 LTS
- **Testing Tools**: MySQL Command Line Client

## Demonstrated Competencies
- User Management and Privileges
- Database Constraints (NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY)
- Table Relationships and Database Design
- Complex Query Operations (JOIN, UNION, Subqueries)
- Data Filtering and Aggregation
- Database Schema Planning and Implementation
- Error Handling in SQL

## System Context
This component builds upon basic SQL knowledge to explore more advanced database operations, focusing on creating proper database architecture, implementing relationships between tables, and writing complex queries to extract meaningful data. It serves as a foundation for designing and interacting with relational databases in real-world applications.

## Development Requirements
- MySQL Server 8.0+
- Command-line interface for MySQL
- SQL script editor (text editor)
- Access to create databases, users, and tables

## Development Workflow
1. Design database schema with appropriate constraints
2. Create SQL scripts to implement the schema
3. Develop query scripts to manipulate and retrieve data
4. Test queries against sample data
5. Optimize queries for performance
6. Document approach and SQL techniques used

## Maintenance Notes
- All SQL queries follow standard SQL syntax with keywords in uppercase
- Scripts include appropriate comments explaining their purpose
- Database schemas include proper constraints to maintain data integrity
- Naming conventions follow standard database design practices
- Complex queries are structured for readability and performance

## Implementation Specifics

### User Management and Privileges
- **User Creation**: [1-create_user.sql](./1-create_user.sql)
- **Limited Privileges**: [2-create_read_user.sql](./2-create_read_user.sql)
- **Viewing Privileges**: [0-privileges.sql](./0-privileges.sql)

### Table Constraints
- **NOT NULL Implementation**: [3-force_name.sql](./3-force_name.sql)
- **DEFAULT Values**: [4-never_empty.sql](./4-never_empty.sql)
- **UNIQUE Constraints**: [5-unique_id.sql](./5-unique_id.sql)
- **AUTO_INCREMENT Keys**: [6-states.sql](./6-states.sql)
- **FOREIGN KEY Relationships**: [7-cities.sql](./7-cities.sql)

### Advanced Query Techniques
- **Subqueries**: [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql)
- **INNER JOINs**: [9-cities_by_state_join.sql](./9-cities_by_state_join.sql)
- **LEFT JOINs**: [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql)
- **Filtering JOINs**: [10-genre_id_by_show.sql](./10-genre_id_by_show.sql), [12-no_genre.sql](./12-no_genre.sql)
- **Aggregation**: [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql)
- **Complex Filtering**: [14-my_genres.sql](./14-my_genres.sql), [15-comedy_only.sql](./15-comedy_only.sql)
- **Multi-table Operations**: [16-shows_by_genre.sql](./16-shows_by_genre.sql)

### Advanced Operations (Optional)
- **Exclusion Queries**: [100-not_a_comedy.sql](./100-not_a_comedy.sql), [101-not_a_comedy.sql](./101-not_a_comedy.sql)
- **Rating Analysis**: [102-rating_shows.sql](./102-rating_shows.sql), [103-rating_genres.sql](./103-rating_genres.sql)

## Error Handling
- Scripts include checks for pre-existing objects where necessary
- Database creation includes `IF NOT EXISTS` clauses
- Table creation includes `IF NOT EXISTS` clauses
- Scripts maintain semantic ordering of operations to prevent errors