# Project Manifest: Python Almost a Circle

## Project Identity
- **Name**: Python Almost a Circle
- **Type**: Educational
- **Scope**: Object-Oriented Programming in Python
- **Status**: Completed

## Technology Signature
- **Core**: Python 3
- **Libraries**: json, csv, unittest, turtle (for visualization)
- **Development Approach**: Test-Driven Development (TDD)
- **Data Formats**: JSON, CSV
- **Testing**: unittest framework

## Demonstrated Competencies
- Object-Oriented Programming (Classes, Objects, Inheritance)
- Data Validation and Encapsulation
- JSON & CSV Serialization/Deserialization
- File I/O Operations
- Unit Testing with Python's unittest framework
- Method Overriding and Polymorphism
- Static and Class Methods
- Args and Kwargs Usage
- Pythonic Programming Practices

## System Context
This project implements geometric shapes (Rectangle and Square) as Python classes with a common Base class. It serves as a comprehensive review of Python OOP concepts and prepares for future projects involving more complex object relationships and database integration.

## Architecture
- **Base Class**: Foundation class with common functionality
  - ID Management
  - JSON/CSV Serialization and Deserialization
  - Instance Creation from Dictionaries
  - Drawing Capabilities (using turtle module)

- **Rectangle Class**: Extends Base
  - Width, Height, Position (x, y) Properties
  - Area Calculation
  - Display Method
  - Dictionary Representation

- **Square Class**: Extends Rectangle
  - Special Case of Rectangle (width = height = size)
  - Simplified Interface

## Development Requirements
- Python 3.8.5 or later
- PEP 8 style compliance
- Properly documented modules and classes
- Comprehensive test suite

## Development Workflow
1. Create test cases for each feature
2. Implement features to pass tests (TDD approach)
3. Validate implementation against requirements
4. Document code with docstrings
5. Verify PEP 8 compliance

## Maintenance Notes
- Code is fully documented with docstrings
- All methods include input validation
- Tests cover edge cases and normal operation
- JSON and CSV serialization provide data persistence
- Class design follows SOLID principles

## Implementation Specifics

### Base Class
- **ID Management**: Automatic or manual ID assignment
- **JSON Serialization**: Convert objects to/from JSON strings
- **File Operations**: Save/load objects to/from files
- **CSV Support**: Alternative serialization format
- **Visualization**: Draw shapes using turtle module

### Rectangle Class
- **Properties**: Width, height, x, y with validation
- **Area Calculation**: Returns width * height
- **Display**: Print the rectangle using # characters
- **Dictionary Conversion**: Convert instance to dictionary
- **Update Method**: Flexible attribute updating with args/kwargs

### Square Class
- **Simplified Interface**: Single size property (width = height)
- **Inheritance**: Leverages Rectangle implementation
- **Specialization**: Overrides methods for square-specific behavior

### Testing Framework
- **Unit Tests**: Comprehensive test suite for all classes
- **Test Cases**: Cover normal operation and edge cases
- **Validation**: Ensures all requirements are met