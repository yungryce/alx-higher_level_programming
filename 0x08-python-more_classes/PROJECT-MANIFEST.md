# Project Manifest: Python More Classes and Objects

## Project Identity
- **Name**: Python - More Classes and Objects
- **Type**: Educational
- **Scope**: Advanced Object-Oriented Programming Concepts
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5
- **Environment**: Ubuntu 20.04 LTS
- **Style Guide**: PEP8
- **Paradigm**: Object-Oriented Programming

## Demonstrated Competencies
- Advanced Object-Oriented Programming
- Special Methods Implementation
- Class and Instance Attribute Management
- Property Decorators and Attribute Access Control
- String Representation of Objects
- Operator Overloading
- Instance Tracking and Management
- Memory Management with Destructors
- Static and Class Methods
- Class Factory Methods
- Algorithm Implementation with OOP
- N-Queens Problem Solving

## System Context
This component builds upon basic OOP concepts, providing a deeper understanding of Python's class mechanisms and special methods. The Rectangle class serves as a model to explore class attributes, instance tracking, operator overloading, and custom string representations. Advanced concepts like static and class methods are introduced, culminating in the application of these principles to solve the N-Queens problem.

## Development Requirements
- Python 3.8.5+
- pycodestyle 2.8.* (PEP8)
- Text Editor or IDE

## Development Workflow
1. Define basic class structure with private attributes and properties
2. Implement area and perimeter calculation methods
3. Add string representation methods (__str__, __repr__)
4. Implement instance cleanup with __del__
5. Add class attributes for instance tracking
6. Implement class customization (print_symbol)
7. Add static methods for object comparison
8. Implement class methods for alternative constructors
9. Apply OOP principles to solve the N-Queens problem

## Maintenance Notes
- All Python files begin with the shebang line `#!/usr/bin/python3`
- Python code follows PEP8 style guidelines
- Classes, methods, and functions have descriptive docstrings
- Private attributes are properly protected with double underscore prefix
- Input validation is implemented for all setters
- Special methods follow Python's conventions
- __repr__ method should enable recreation of objects

## Implementation Specifics

### Basic Class Structure
- **Empty Class**: [0-rectangle.py](./0-rectangle.py) - Define a basic Rectangle class
- **Private Attributes**: [1-rectangle.py](./1-rectangle.py) - Rectangle with width and height properties
- **Area & Perimeter**: [2-rectangle.py](./2-rectangle.py) - Add calculation methods

### String Representation
- **String Output**: [3-rectangle.py](./3-rectangle.py) - Implement __str__ method for printing
- **Eval Support**: [4-rectangle.py](./4-rectangle.py) - Add __repr__ for object recreation
- **Instance Deletion**: [5-rectangle.py](./5-rectangle.py) - Add __del__ method

### Class Features
- **Instance Counter**: [6-rectangle.py](./6-rectangle.py) - Track number of instances
- **Print Symbol**: [7-rectangle.py](./7-rectangle.py) - Customizable string representation
- **Static Methods**: [8-rectangle.py](./8-rectangle.py) - Rectangle comparison
- **Class Methods**: [9-rectangle.py](./9-rectangle.py) - Square factory method

### Problem Solving
- **N-Queens Solution**: [101-nqueens.py](./101-nqueens.py) - Solve the N-Queens chess problem

## Class Evolution

### Rectangle Class Progression
1. **Basic Definition**: Empty class declaration
2. **Attributes**: Private width and height with getters/setters
3. **Functionality**: Area and perimeter calculations
4. **Display**: String representation with # characters
5. **Recreation**: Formal string representation for eval()
6. **Cleanup**: Proper resource management with __del__
7. **Tracking**: Class attribute to count instances
8. **Customization**: Configurable display symbol
9. **Comparison**: Static method to compare rectangles
10. **Factories**: Class method to create squares

## Special Methods Used

### Object Lifecycle
- `__init__`: Initialize Rectangle instances with width and height
- `__del__`: Clean up resources and decrement instance counter

### String Representation
- `__str__`: User-friendly string representation with symbols
- `__repr__`: Developer-friendly string representation for recreation

### Attribute Access
- Property decorators for controlled attribute access
- Getters and setters with validation

### Comparison Operations
- Static method for rectangle comparison based on area

## OOP Concepts Demonstrated

### Encapsulation
- Private attributes with double underscore prefix (`__width`, `__height`)
- Controlled access through property decorators
- Input validation in setters

### Class vs Instance Attributes
- Instance attributes for individual object state
- Class attributes shared across all instances
- Tracking number of active instances

### Method Types
- Instance methods operating on object state
- Static methods for object comparison
- Class methods for alternative constructors

## Algorithm Implementation
- N-Queens algorithm using backtracking
- Representation of chess pieces and board state as objects
- Solution validation and output formatting

## Testing Approach
- Manual testing of each class version
- Validation of all special methods
- Edge case testing (zero dimensions, negative inputs)
- Complete algorithm testing for N-Queens