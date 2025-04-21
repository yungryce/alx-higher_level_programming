# Project Manifest: Python Inheritance

## Project Identity
- **Name**: Python Inheritance
- **Type**: Educational
- **Scope**: Object-Oriented Programming Concepts
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8+
- **Testing Framework**: Unittest
- **Documentation**: Docstrings (Google style)
- **Style Guide**: PEP 8

## Demonstrated Competencies
- Object-Oriented Programming Principles
- Inheritance Hierarchies and Implementation
- Method Overriding and Extension
- Multiple Inheritance Management
- Type Checking and Verification
- Abstract Base Classes
- Test-Driven Development
- Python Built-in Functions for OOP
- Documentation Standards

## System Context
This component builds upon previous object-oriented programming modules, focusing specifically on inheritance as a mechanism for code reuse and hierarchical design. It introduces advanced OOP concepts that will be utilized in subsequent Python modules that deal with more complex object models and serialization.

## Development Requirements
- Python 3.8+ Interpreter
- Unittest Framework
- PEP 8 Compliant Code Style
- Comprehensive Docstrings
- Test Files for Each Implementation

## Development Workflow
1. Understand the inheritance concept to be implemented
2. Write test cases that validate expected behavior (TDD approach)
3. Implement the required class structure and inheritance hierarchy
4. Validate implementation against test cases
5. Document classes and methods with appropriate docstrings
6. Ensure code style compliance with PEP 8

## Maintenance Notes
- All classes follow Python naming conventions (CamelCase for classes)
- Method overrides are clearly documented
- Multiple inheritance is used sparingly and with clear purpose
- Tests cover both normal operation and edge cases
- Docstrings provide comprehensive information about class hierarchies

## Implementation Specifics

### Basic Inheritance Concepts
- **Type Testing**: [0-lookup.py](./0-lookup.py), [2-is_same_class.py](./2-is_same_class.py), [3-is_kind_of_class.py](./3-is_kind_of_class.py), [4-inherits_from.py](./4-inherits_from.py)
- **Simple Inheritance**: [1-my_list.py](./1-my_list.py), [5-base_geometry.py](./5-base_geometry.py), [6-base_geometry.py](./6-base_geometry.py)

### Method Implementation and Overriding
- **Method Implementation**: [7-base_geometry.py](./7-base_geometry.py)
- **Method Inheritance**: [8-rectangle.py](./8-rectangle.py), [9-rectangle.py](./9-rectangle.py)
- **Method Override**: [10-square.py](./10-square.py), [11-square.py](./11-square.py)

### Advanced Inheritance Concepts
- **Multiple Inheritance**: [100-my_int.py](./100-my_int.py)
- **Attribute Addition**: [101-add_attribute.py](./101-add_attribute.py)

### Testing
- **Test Files**: Tests for each implementation in [tests/](./tests/) directory

## Learning Path Integration
- **Builds On**: Classes and Objects (0x06), Everything is Object (0x09)
- **Leads To**: File I/O and Serialization (0x0B), Almost a Circle project (0x0C)

## Assessment Criteria
- Correct implementation of inheritance hierarchies
- Proper use of Python's built-in functions for type checking
- Comprehensive test coverage
- Clear and informative docstrings
- PEP 8 compliant code style
- Handling of edge cases and invalid inputs