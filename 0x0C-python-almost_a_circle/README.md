# Python Almost a Circle

This project implements a hierarchy of geometric classes (Base, Rectangle, and Square) using Python's object-oriented programming features. It serves as a comprehensive review of Python OOP concepts including inheritance, encapsulation, serialization, and unit testing.

## Project Overview

The "Almost a Circle" project constructs a robust framework for managing geometric shapes with the following class hierarchy:

1. **Base**: Foundation class for all shapes
   - Manages object IDs
   - Handles serialization/deserialization (JSON & CSV)
   - Provides utility methods for all derived classes

2. **Rectangle**: First-level derived class
   - Extends Base
   - Manages width, height, and position (x, y)
   - Implements area calculation and display methods
   - Supports attribute updates through multiple approaches

3. **Square**: Second-level derived class
   - Extends Rectangle
   - Specializes Rectangle with width = height

## Core Features

### Object-Oriented Programming
- **Inheritance**: Multi-level class hierarchy
- **Encapsulation**: Private attributes with getters/setters
- **Property Decorators**: For attribute validation
- **Method Overriding**: Customized behavior in derived classes

### Data Management
- **JSON Serialization**: Convert objects to/from JSON format
- **CSV Serialization**: Alternative data format support
- **File I/O**: Save and load objects from files
- **Dictionary Representation**: Convert objects to dictionaries

### Validation & Error Handling
- **Type Checking**: Ensure attributes have correct types
- **Value Validation**: Enforce valid ranges for attributes
- **Comprehensive Error Messages**: Clear feedback on validation failures

### Testing
- **Unit Tests**: Thorough test suite using unittest framework
- **Test-Driven Development**: Tests created before implementation
- **Edge Case Coverage**: Tests for normal operation and boundary conditions

## Technical Implementation

### Base Class
```python
class Base:
    """Base class for all shapes in the project"""
    __nb_objects = 0  # Private class attribute for ID management
    
    def __init__(self, id=None):
        """Initialize a new Base instance
        
        Args:
            id (int, optional): The identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        # Implementation details...
    
    # Additional methods for serialization/deserialization
    # and instance creation
```

### Rectangle Class
```python
class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int, optional): X-coordinate position
            y (int, optional): Y-coordinate position
            id (int, optional): Identity of the new Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
    # Property getters and setters with validation
    # Area calculation and display methods
    # Update method supporting both args and kwargs
```

### Square Class
```python
class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance
        
        Args:
            size (int): Size of the square (width and height)
            x (int, optional): X-coordinate position
            y (int, optional): Y-coordinate position
            id (int, optional): Identity of the new Square
        """
        super().__init__(size, size, x, y, id)
        
    # Property getter and setter for size
    # Override methods to maintain square behavior
    # Update method supporting both args and kwargs
```

## Usage Examples

### Creating Instances
```python
# Create a Base instance
b = Base(1)
print(b.id)  # Output: 1

# Create a Rectangle instance
r = Rectangle(10, 5, 2, 1, 3)
print(r.width, r.height, r.x, r.y, r.id)  # Output: 10 5 2 1 3

# Create a Square instance
s = Square(5, 2, 3, 4)
print(s.size, s.x, s.y, s.id)  # Output: 5 2 3 4
```

### Area Calculation
```python
r = Rectangle(3, 4)
print(r.area())  # Output: 12

s = Square(5)
print(s.area())  # Output: 25
```

### JSON Serialization
```python
r1 = Rectangle(10, 7, 2, 8, 1)
r2 = Rectangle(2, 4, 0, 0, 2)
list_rectangles = [r1, r2]

# Serialize to JSON string
json_str = Rectangle.to_json_string([r.to_dictionary() for r in list_rectangles])
print(json_str)

# Save to file
Rectangle.save_to_file(list_rectangles)

# Load from file
loaded_rectangles = Rectangle.load_from_file()
```

## Testing

The project follows a test-driven development approach with comprehensive unit tests for all classes and methods:

```python
# Example test case for the Rectangle class
class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""
    
    def test_init(self):
        """Test Rectangle initialization"""
        r = Rectangle(10, 5, 2, 1, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 3)
        
    def test_validation(self):
        """Test attribute validation"""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        # Additional validation tests
```

To run the tests:
```bash
python -m unittest discover tests
```

## Requirements

- Python 3.8.5 or later
- PEP 8 style (version 2.8.*)
- All files must be executable
- All modules, classes, and methods must be documented

## Project Structure

```
0x0C-python-almost_a_circle/
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
├── tests/
│   ├── __init__.py
│   └── test_models/
│       ├── __init__.py
│       ├── test_base.py
│       ├── test_rectangle.py
│       └── test_square.py
├── README.md
└── PROJECT-MANIFEST.md
```

## Learning Objectives

After completing this project, you should be able to explain:

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a class
- How to write and read a JSON file
- What are `*args` and `**kwargs` and how to use them
- How to handle named arguments in a function
- How to implement proper attribute encapsulation
- How to use inheritance to create related classes
- How to override methods from a parent class
- How to use the unittest module to test your code

## Conclusion

The "Almost a Circle" project demonstrates a comprehensive implementation of Python's OOP features. It provides a solid foundation for working with geometric shapes and can be extended to more complex scenarios. The project's focus on proper testing, validation, and serialization makes it a robust example of Python application design.
