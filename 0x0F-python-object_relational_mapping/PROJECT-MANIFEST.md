# Project Manifest: Python Object-Relational Mapping

## Project Identity
- **Name**: Python - Object-Relational Mapping (ORM)
- **Type**: Educational
- **Scope**: Database Connectivity with Python
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5, MySQL 8.0
- **Libraries**: MySQLdb 2.0.x, SQLAlchemy 1.4.x
- **Environment**: Ubuntu 20.04 LTS
- **Testing Tools**: Python Interpreter, MySQL Command Line Client

## Demonstrated Competencies
- Database Connections from Python
- Raw SQL Query Execution via MySQLdb
- Object-Relational Mapping with SQLAlchemy
- Database Schema Representation as Python Classes
- Python Virtual Environment Management
- SQL Injection Prevention Techniques
- ORM Relationships (One-to-Many, Many-to-Many)
- CRUD Operations via ORM

## System Context
This component bridges the gap between Python applications and relational databases, demonstrating both direct database access using MySQLdb and the abstraction layer provided by SQLAlchemy ORM. It serves as a foundation for developing database-driven applications in Python without writing raw SQL queries, treating database tables as Python objects instead.

## Development Requirements
- Python 3.8.5+
- MySQL Server 8.0+
- MySQLdb Module 2.0.x
- SQLAlchemy Module 1.4.x
- Python Virtual Environment
- Text Editor or IDE

## Development Workflow
1. Set up Python virtual environment
2. Install required dependencies (MySQLdb, SQLAlchemy)
3. Create database connection scripts using MySQLdb
4. Define database schema using SQLAlchemy models
5. Implement query operations using ORM methods
6. Test scripts against sample databases
7. Document code and approach

## Maintenance Notes
- All scripts follow PEP 8 style guidelines
- Module, class, and function documentation provided
- SQL injection prevention implemented in all database operations
- Connection resources properly closed after use
- Error handling for database operations

## Implementation Specifics

### Direct Database Access with MySQLdb
- **Basic Queries**: [0-select_states.py](./0-select_states.py)
- **Filtered Queries**: [1-filter_states.py](./1-filter_states.py), [2-my_filter_states.py](./2-my_filter_states.py)
- **SQL Injection Prevention**: [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)
- **JOIN Operations**: [4-cities_by_state.py](./4-cities_by_state.py), [5-filter_cities.py](./5-filter_cities.py)

### Object-Relational Mapping with SQLAlchemy
- **Table Models**: [model_state.py](./model_state.py), [model_city.py](./model_city.py)
- **Creating Tables**: [6-model_state.py](./6-model_state.py)
- **Basic Queries**: [7-model_state_fetch_all.py](./7-model_state_fetch_all.py), [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)
- **Filtered Queries**: [9-model_state_filter_a.py](./9-model_state_filter_a.py), [10-model_state_my_get.py](./10-model_state_my_get.py)
- **Insert Operations**: [11-model_state_insert.py](./11-model_state_insert.py)
- **Update Operations**: [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)
- **Delete Operations**: [13-model_state_delete_a.py](./13-model_state_delete_a.py)
- **Relationships**: [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)

### Advanced Relationships
- **Many-to-One Models**: [relationship_city.py](./relationship_city.py), [relationship_state.py](./relationship_state.py)
- **Creating Related Records**: [100-relationship_states_cities.py](./100-relationship_states_cities.py)
- **Querying Related Data**: [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py), [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py)

## Database Schema
- **States Table**: id (PK), name
- **Cities Table**: id (PK), state_id (FK), name

## Error Handling
- Scripts handle database connection errors gracefully
- Protection against SQL injection implemented
- Proper exception handling for database operations
- Input validation for command-line arguments