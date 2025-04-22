# Python - More Classes and Objects

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/OOP-Advanced-green.svg" alt="OOP Advanced">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project explores advanced Object-Oriented Programming concepts in Python, building upon basic OOP principles. Through progressive implementation of a Rectangle class, we delve into special methods, class attributes, static and class methods, and apply these concepts to solve real problems like the N-Queens puzzle.

## Learning Objectives

* Strengthen understanding of Object-Oriented Programming
* Master Python's special methods and their applications
* Distinguish between class and instance attributes
* Implement property decorators for attribute control
* Create string representations of objects
* Track class instances with class attributes
* Use destructors for proper resource management
* Apply static and class methods for specific functionality
* Create factory methods for alternative construction patterns
* Solve complex problems with OOP principles

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*
* All files must have documentation

## Project Tasks

<details>
<summary><strong>Basic Class Implementation</strong></summary>

* **Task 0**: [0-rectangle.py](./0-rectangle.py)
  * Empty class Rectangle definition
  * Introduction to class creation

* **Task 1**: [1-rectangle.py](./1-rectangle.py)
  * Add private width and height attributes
  * Implement property getters and setters
  * Add validation for attribute values

* **Task 2**: [2-rectangle.py](./2-rectangle.py)
  * Add area and perimeter calculation methods
  * Handle special cases (zero dimensions)
</details>

<details>
<summary><strong>Object Representation</strong></summary>

* **Task 3**: [3-rectangle.py](./3-rectangle.py)
  * Implement __str__ method for printing rectangle
  * Represent rectangle with # characters

* **Task 4**: [4-rectangle.py](./4-rectangle.py)
  * Add __repr__ method for string representation
  * Enable recreation of objects with eval()

* **Task 5**: [5-rectangle.py](./5-rectangle.py)
  * Implement __del__ method for object deletion
  * Display message when rectangle is deleted
</details>

<details>
<summary><strong>Class Attributes & Methods</strong></summary>

* **Task 6**: [6-rectangle.py](./6-rectangle.py)
  * Add class attribute to count instances
  * Update counter on creation and deletion

* **Task 7**: [7-rectangle.py](./7-rectangle.py)
  * Add print_symbol class attribute
  * Customize string representation character

* **Task 8**: [8-rectangle.py](./8-rectangle.py)
  * Implement static method bigger_or_equal
  * Compare rectangles based on area

* **Task 9**: [9-rectangle.py](./9-rectangle.py)
  * Add class method square for square creation
  * Factory method demonstration
</details>

<details>
<summary><strong>Advanced Application</strong></summary>

* **Task 10**: [101-nqueens.py](./101-nqueens.py)
  * Solve the N-Queens chess problem
  * Apply OOP concepts to algorithm implementation
</details>

## Special Methods in Python

Python's special methods (magic methods) allow classes to emulate built-in types or implement operator overloading:

```python
class Example:
    def __init__(self, value):
        """Constructor - Called when creating an instance"""
        self.value = value
        
    def __str__(self):
        """String representation - Called by str() and print()"""
        return f"Example with value: {self.value}"
        
    def __repr__(self):
        """Official string representation - Called by repr()"""
        return f"Example({self.value})"
        
    def __del__(self):
        """Destructor - Called when object is garbage collected"""
        print(f"Example with value {self.value} is being destroyed")
```

## Class vs Instance Attributes

```python
class Rectangle:
    # Class attribute - shared by all instances
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width=0, height=0):
        # Instance attributes - unique to each instance
        self.width = width
        self.height = height
        # Update class attribute
        Rectangle.number_of_instances += 1
```

## Property Decorators

Properties provide controlled access to attributes:

```python
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width  # Calls the setter
        self.height = height  # Calls the setter
        
    @property
    def width(self):
        """Getter for width"""
        return self.__width
        
    @width.setter
    def width(self, value):
        """Setter for width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
```

## Static and Class Methods

```python
class Rectangle:
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method - doesn't access instance attributes"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
        
    @classmethod
    def square(cls, size=0):
        """Class method - can create new instances of the class"""
        return cls(size, size)  # cls refers to Rectangle
```

## N-Queens Problem

The N-Queens problem involves placing N chess queens on an N×N chessboard so that no queens threaten each other:

* No two queens share the same row, column, or diagonal
* Solution requires backtracking algorithm
* Implementation demonstrates:
  * Problem decomposition
  * State representation
  * Solution validation
  * Algorithm optimization

## Resources

* [Python Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
* [Python Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)
* [Class vs Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [N-Queens Problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle)

---

*Project by ALX Higher Level Programming*
