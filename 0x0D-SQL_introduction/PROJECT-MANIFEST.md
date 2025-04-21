# Project Manifest: SQL Introduction

## Project Identity
- **Name**: Introduction to SQL
- **Type**: Educational
- **Scope**: Database Fundamentals
- **Status**: Completed

## Technology Signature
- **Core**: MySQL 8.0
- **Query Language**: SQL
- **Client**: MySQL CLI
- **Data Types**: Numeric, String, Date/Time
- **Operations**: DDL, DML, DQL

## Demonstrated Competencies
- Database Creation and Management
- Table Definition and Alteration
- Basic Data Manipulation (CRUD operations)
- Query Construction and Execution
- Result Filtering and Sorting
- Aggregate Functions
- Database Administration Basics
- Data Import/Export
- Character Set and Collation Management

## System Context
This module serves as the foundation for all database-related work in the curriculum, establishing core SQL concepts that will be expanded upon in subsequent modules covering more advanced queries, database design, and ORM implementation.

## Development Requirements
- MySQL Server 8.0 or higher
- MySQL Command Line Client
- Terminal/Command Prompt access
- Text Editor for SQL script creation

## Development Workflow
1. Understand the SQL concept being taught
2. Write SQL scripts according to task requirements
3. Test scripts in MySQL environment
4. Verify results match expected output
5. Document approach and key learnings

## Maintenance Notes
- SQL scripts follow standard SQL syntax with MySQL-specific extensions where necessary
- Each script focuses on a single concept or operation
- Scripts include comments where helpful for clarity
- All scripts have been tested with MySQL 8.0

## Implementation Specifics

### Database Administration
- **Database Listing**: [0-list_databases.sql](./0-list_databases.sql)
- **Database Creation**: [1-create_database_if_missing.sql](./1-create_database_if_missing.sql)
- **Database Deletion**: [2-remove_database.sql](./2-remove_database.sql)

### Table Operations
- **Table Listing**: [3-list_tables.sql](./3-list_tables.sql)
- **Table Creation**: [4-first_table.sql](./4-first_table.sql)
- **Table Description**: [5-full_table.sql](./5-full_table.sql)

### Data Manipulation
- **Record Insertion**: [7-insert_value.sql](./7-insert_value.sql)
- **Data Counting**: [8-count_89.sql](./8-count_89.sql)

### Queries and Filtering
- **Ordered Retrieval**: [10-top_score.sql](./10-top_score.sql)
- **Filtered Retrieval**: [11-best_score.sql](./11-best_score.sql)
- **Data Updates**: [12-no_cheating.sql](./12-no_cheating.sql)
- **Conditional Deletion**: [13-change_class.sql](./13-change_class.sql)

### Aggregate Functions
- **Averaging Values**: [14-average.sql](./14-average.sql)
- **Grouping and Counting**: [16-no_link.sql](./16-no_link.sql)

### Advanced Operations
- **Character Set Conversion**: [100-move_to_utf8.sql](./100-move_to_utf8.sql)
- **Temperature Analysis**: [101-avg_temperatures.sql](./101-avg_temperatures.sql), [102-top_city.sql](./102-top_city.sql), [103-max_state.sql](./103-max_state.sql)

## Conceptual Architecture

```
[User] --> [MySQL Client] --> [MySQL Server] --> [Storage Engine] --> [Database Files]
    |           |                  |
    v           v                  v
[SQL Scripts] [Query Results] [Database Objects]
```

This architecture represents the flow from user-written SQL scripts through the database system, highlighting the separation between client, server, and storage components that is fundamental to understanding database operations.