# Project Manifest: Python Classes and Objects

## Project Identity
- **Name**: Python - Classes and Objects
- **Type**: Educational
- **Scope**: Object-Oriented Programming Fundamentals
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5
- **Environment**: Ubuntu 20.04 LTS
- **Testing Tools**: Python Interpreter

## Demonstrated Competencies
- Object-Oriented Programming Principles
- Class and Instance Creation
- Private Attribute Management
- Method Implementation
- Property Decorators (Getters and Setters)
- Data Validation
- Operator Overloading
- String Representation of Objects
- Comparison Method Implementation
- Linked List Data Structure
- Docstring Documentation

## System Context
This component introduces the fundamental concepts of Object-Oriented Programming in Python. Classes and objects are essential for modeling real-world entities, organizing code into logical units, and implementing reusable components. These concepts form the foundation for more advanced programming techniques and are critical for modern software development.

## Development Requirements
- Python 3.8.5+
- pycodestyle 2.8.* (PEP8)
- Text Editor or IDE

## Development Workflow
1. Define class structure with appropriate attributes and methods
2. Implement initialization logic with proper validation
3. Add methods to provide class behavior
4. Create property decorators for controlled attribute access
5. Implement special methods for enhanced functionality
6. Test class behavior with various inputs
7. Document class and methods with docstrings

## Maintenance Notes
- All Python files begin with the shebang line `#!/usr/bin/python3`
- Python code follows PEP8 style guidelines
- Classes, methods, and functions have descriptive docstrings
- Private attributes are properly protected with double underscore prefix
- Data validation is implemented for all setters
- Special methods follow Python's conventions

## Implementation Specifics

### Class Fundamentals
- **Empty Class**: [0-square.py](./0-square.py) - Define a basic Square class
- **Simple Class with Private Attribute**: [1-square.py](./1-square.py) - Square with private size attribute
- **Input Validation**: [2-square.py](./2-square.py) - Square with validation for size attribute

### Methods and Properties
- **Instance Methods**: [3-square.py](./3-square.py) - Add area calculation method
- **Properties**: [4-square.py](./4-square.py) - Implement getter and setter for size
- **Printing Objects**: [5-square.py](./5-square.py) - Add method to print the square
- **Position Attribute**: [6-square.py](./6-square.py) - Add position attribute with validation

### Advanced Class Features
- **String Representation**: [101-square.py](./101-square.py) - Implement __str__ method
- **Comparison Operators**: [102-square.py](./102-square.py) - Implement comparison methods

### Data Structures
- **Linked List**: [100-singly_linked_list.py](./100-singly_linked_list.py) - Implement a singly linked list

## Class Design Patterns

### Square Class Evolution
1. **Basic Definition**: Empty class definition
2. **Private Attributes**: Add private size attribute
3. **Validation**: Add type and value checking
4. **Functionality**: Add area calculation method
5. **Access Control**: Add property getter and setter
6. **Visual Representation**: Add printing method
7. **Positioning**: Add position attribute
8. **String Conversion**: Implement __str__ for string representation
9. **Comparability**: Add comparison operators

### Node and SinglyLinkedList Classes
1. **Node Definition**: Data storage with next node reference
2. **Attribute Control**: Properties for data and next_node
3. **Validation**: Type checking for both attributes
4. **List Management**: Methods for insertion and traversal
5. **Ordered Insertion**: Algorithm for maintaining sorted order
6. **String Representation**: String conversion for printing

## OOP Concepts Demonstrated

### Encapsulation
- Private attributes with double underscore prefix (`__size`)
- Controlled access through property decorators
- Input validation in setters

### Abstraction
- Methods that hide implementation details (area, my_print)
- Clear interfaces for interacting with objects

### Object State
- Instance attributes that maintain object state
- Methods that operate on and modify that state

### Special Methods
- `__init__` for object initialization
- `__str__` for string representation
- Comparison methods (`__eq__`, `__ne__`, `__lt__`, etc.)

## Testing Approach
- Each class is tested with various inputs
- Validation errors are verified with appropriate inputs
- Methods are tested for correct behavior
- Edge cases are considered (zero size, empty lists, etc.)
- Special method behaviors are verified

## Documentation Guidelines
- Module docstrings explain the purpose of the file
- Class docstrings describe what the class represents
- Method docstrings include:
  - Purpose of the method
  - Parameters with types
  - Return values
  - Possible exceptions