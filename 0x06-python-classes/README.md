# Python - Classes and Objects

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/OOP-Principles-green.svg" alt="OOP Principles">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project introduces Object-Oriented Programming (OOP) in Python through classes and objects. It demonstrates creating classes, attributes, methods, properties, and special methods to build reusable, encapsulated code.

## Learning Objectives

* Understand Object-Oriented Programming concepts
* Learn about classes, objects, and instances
* Master attributes and methods with proper encapsulation
* Implement properties with getters and setters
* Use special methods for custom behavior
* Create data structures using OOP principles

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*

## Project Tasks

<details>
<summary><strong>Class Fundamentals</strong></summary>

* **Task 0**: [0-square.py](./0-square.py)
  * Create an empty class Square

* **Task 1**: [1-square.py](./1-square.py)
  * Create a Square class with a private size attribute

* **Task 2**: [2-square.py](./2-square.py)
  * Add validation to the size attribute
</details>

<details>
<summary><strong>Methods and Properties</strong></summary>

* **Task 3**: [3-square.py](./3-square.py)
  * Add an area method to calculate square area

* **Task 4**: [4-square.py](./4-square.py)
  * Add property getter/setter for size

* **Task 5**: [5-square.py](./5-square.py)
  * Add method to print the square with # character

* **Task 6**: [6-square.py](./6-square.py)
  * Add position attribute and adjust printing
</details>

<details>
<summary><strong>Advanced Features</strong></summary>

* **Task 7**: [100-singly_linked_list.py](./100-singly_linked_list.py)
  * Implement a singly linked list with Node and SinglyLinkedList classes

* **Task 8**: [101-square.py](./101-square.py)
  * Add string representation to the Square class

* **Task 9**: [102-square.py](./102-square.py)
  * Make squares comparable with operators (<, >, ==, etc.)
</details>

## Key OOP Concepts

### Classes and Objects
```python
# Class definition
class MyClass:
    """Class docstring explains the purpose"""
    
    def __init__(self, parameter):
        """Constructor method initializes object state"""
        self.attribute = parameter
        
# Creating an instance (object)
my_object = MyClass("value")
```

### Private Attributes
```python
class PrivateExample:
    def __init__(self):
        # Private attribute (name mangling)
        self.__private = "Hidden"
        
        # Protected attribute (convention)
        self._protected = "Limited access"
        
        # Public attribute
        self.public = "Open access"
```

### Properties
```python
class Square:
    def __init__(self, size=0):
        # Private attribute
        self.__size = size
    
    @property
    def size(self):
        """Getter method for size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```

### Special Methods
```python
class Comparable:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        """String representation"""
        return f"Comparable({self.value})"
        
    def __eq__(self, other):
        """Equality comparison (==)"""
        return self.value == other.value
        
    def __lt__(self, other):
        """Less than comparison (<)"""
        return self.value < other.value
```

## Accessing Documentation

Python provides ways to access docstrings programmatically:

* **Module docstring**: `python3 -c 'print(__import__("my_module").__doc__)'`
* **Class docstring**: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
* **Method docstring**: `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

## Best Practices

1. **Encapsulation**: Use private attributes with public interfaces
2. **Validation**: Validate inputs in setters to maintain object integrity
3. **Documentation**: Write clear docstrings for classes and methods
4. **Consistency**: Follow naming conventions for methods and attributes
5. **Readability**: Use properties instead of direct attribute access for complex logic

## Resources

* [Python Documentation - Classes](https://docs.python.org/3/tutorial/classes.html)
* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9: Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)

---

*Project by ALX Higher Level Programming*
