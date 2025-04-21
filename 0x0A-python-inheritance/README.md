# Python Inheritance

This project explores inheritance in Python as a powerful mechanism for code reuse and building relationships between classes.

## Learning Objectives

By the end of this project, you will be able to:

- Explain why Python programming is awesome
- Understand inheritance as a fundamental OOP concept
- Define and use superclass, baseclass, or parentclass
- Create a subclass that inherits from another class
- List all attributes and methods of a class or instance
- Determine when an instance can have new attributes
- Inherit a class from another class
- Define a class with multiple base classes
- Understand the default class every class inherits from
- Override methods or attributes inherited from the base class
- Access attributes or methods available by heritage to subclasses
- Identify the purpose of inheritance in OOP design
- Use `isinstance()`, `issubclass()`, `type()` and `super()` built-in functions effectively

## Project Structure

### Basic Inheritance Operations

* **[0-lookup.py](./0-lookup.py)**: Function that returns the list of available attributes and methods of an object
* **[1-my_list.py](./1-my_list.py)**: Class `MyList` that inherits from `list` with method to print sorted list
* **[2-is_same_class.py](./2-is_same_class.py)**: Function to check if an object is exactly an instance of a specific class
* **[3-is_kind_of_class.py](./3-is_kind_of_class.py)**: Function to check if object is an instance of, or inherited from, a class
* **[4-inherits_from.py](./4-inherits_from.py)**: Function to check if object is an instance of a class that inherited from a specified class

### Geometric Shapes Inheritance Hierarchy

* **[5-base_geometry.py](./5-base_geometry.py)**: Empty class `BaseGeometry`
* **[6-base_geometry.py](./6-base_geometry.py)**: `BaseGeometry` with public method `area()` that raises an exception
* **[7-base_geometry.py](./7-base_geometry.py)**: `BaseGeometry` with additional method `integer_validator()`
* **[8-rectangle.py](./8-rectangle.py)**: Class `Rectangle` that inherits from `BaseGeometry`
* **[9-rectangle.py](./9-rectangle.py)**: `Rectangle` with area implementation and string representation
* **[10-square.py](./10-square.py)**: Class `Square` that inherits from `Rectangle`
* **[11-square.py](./11-square.py)**: `Square` with proper string representation

### Advanced Inheritance Concepts

* **[100-my_int.py](./100-my_int.py)**: Class `MyInt` that inherits from `int` with inverted `==` and `!=` operators
* **[101-add_attribute.py](./101-add_attribute.py)**: Function to add a new attribute to an object if possible

## Inheritance in Python

Inheritance is a powerful object-oriented programming concept that allows classes to inherit attributes and methods from other classes. This promotes code reuse and establishes a relationship between a parent class (base class) and a child class (derived class).

### Key Concepts

#### Types of Inheritance

1. **Single Inheritance**: A subclass inherits from one parent class
   ```python
   class Parent:
       def method_a(self):
           return "Method A from Parent"
   
   class Child(Parent):
       def method_b(self):
           return "Method B from Child"
   ```

2. **Multiple Inheritance**: A subclass inherits from more than one parent class
   ```python
   class ParentA:
       def method_a(self):
           return "Method A from ParentA"
   
   class ParentB:
       def method_b(self):
           return "Method B from ParentB"
   
   class Child(ParentA, ParentB):
       def method_c(self):
           return "Method C from Child"
   ```

#### Method Resolution Order (MRO)

Python uses the C3 Linearization algorithm to determine the method resolution order, which defines the search path for methods and attributes.

```python
class Child(ParentA, ParentB):
    pass

print(Child.__mro__)  # Shows the resolution order
```

#### Method Overriding

Child classes can redefine methods inherited from parent classes:

```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Overriding the greet method
        return "Hello from Child"
```

#### Using `super()`

The `super()` function allows you to call methods from the parent class:

```python
class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()
        return f"{parent_greeting}, and hello from Child"
```

### Type Checking with Python Built-ins

- **`isinstance(obj, class)`**: Checks if an object is an instance of a class or a subclass thereof
- **`issubclass(subclass, class)`**: Checks if a class is a subclass of another class
- **`type(obj)`**: Returns the type of an object (not inheritance-aware)

## Testing

The `tests/` directory contains test files for each implementation:

- [tests/1-my_list.txt](./tests/1-my_list.txt): Tests for the `MyList` class
- [tests/7-base_geometry.txt](./tests/7-base_geometry.txt): Tests for the `BaseGeometry` class

## Requirements

- Python 3.8.5
- pycodestyle 2.8.* (for code style validation)
- All files must be executable
- All modules, classes, and functions must have documentation
- Tests must be runnable with: `python3 -m doctest ./tests/*`

## Usage Examples

### Using `MyList` to Sort a List

```python
MyList = __import__('1-my_list').MyList

my_list = MyList([3, 1, 2])
my_list.print_sorted()  # Prints: [1, 2, 3]
print(my_list)  # Prints: [3, 1, 2] (original list unchanged)
```

### Geometry Hierarchy Example

```python
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)
print(r.area())  # Prints: 15
print(r)  # Prints: [Rectangle] 3/5
```

```python
Square = __import__('11-square').Square

s = Square(5)
print(s.area())  # Prints: 25
print(s)  # Prints: [Square] 5/5
```

## Author

[Your Name]
