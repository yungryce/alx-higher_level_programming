# Python - Everything is object

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/Memory-Management-red.svg" alt="Memory Management">
  <img src="https://img.shields.io/badge/Object-Model-green.svg" alt="Object Model">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project explores Python's object model and memory management in depth. In Python, everything is an object - from simple integers to complex data structures. Understanding how Python handles objects, references, and memory is crucial for writing efficient and bug-free code. This project uses a Q&A approach to examine object behavior, variable references, mutability concepts, and memory optimization techniques.

## Learning Objectives

* Understand what objects are in Python
* Differentiate between classes and objects/instances
* Distinguish between immutable and mutable objects
* Comprehend references, assignments, and aliases
* Determine when variables are identical or linked to the same object
* Display and interpret variable identifiers (memory addresses)
* Understand how Python passes variables to functions
* Master object identity versus equality

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*
* Text files with a single line answer

## Project Format

This project is primarily composed of `.txt` files containing answers to questions about Python's object behavior. Each file answers a specific question about how Python handles objects, memory, references, and variable assignment.

## Key Concepts

### Object Identity vs Equality

In Python, identity (`is`) and equality (`==`) are distinct concepts:

```python
# Equality (==) compares values
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True - same values

# Identity (is) compares memory addresses
print(a is b)  # False - different objects in memory
print(id(a), id(b))  # Different memory addresses

# Same object
c = a
print(a is c)  # True - same object in memory
```

### Mutable vs Immutable Types

Python objects can be either mutable (can be changed) or immutable (cannot be changed):

<details>
<summary><strong>Immutable Types</strong></summary>

* int
* float
* bool
* str
* tuple
* frozenset
* None

```python
# String (immutable)
s = "hello"
print(id(s))  # Memory address 1
s += " world"  # Creates a new string object
print(id(s))  # Memory address 2 (different)
```
</details>

<details>
<summary><strong>Mutable Types</strong></summary>

* list
* dict
* set
* custom classes (by default)

```python
# List (mutable)
l = [1, 2, 3]
print(id(l))  # Memory address 1
l.append(4)   # Modifies the existing list
print(id(l))  # Memory address 1 (same)
```
</details>

### Python Memory Optimizations

Python implements several optimizations that affect object identity:

<details>
<summary><strong>Integer Caching</strong></summary>

Python pre-creates and reuses integer objects in the range [-5, 256]:

```python
a = 256
b = 256
print(a is b)  # True - same object due to caching

c = 257
d = 257
print(c is d)  # False - different objects (above caching range)
```
</details>

<details>
<summary><strong>String Interning</strong></summary>

Python may intern (reuse) certain strings:

```python
a = "hello"
b = "hello"
print(a is b)  # True - string interning

c = "hello world"
d = "hello world"
print(c is d)  # May be True or False depending on implementation
```
</details>

### Variable Assignment and References

In Python, variables are references to objects, not containers for values:

```python
# Assignment creates a reference
a = [1, 2, 3]
b = a        # b references the same object as a
b.append(4)  # Modifies the object that both a and b reference
print(a)     # [1, 2, 3, 4] - a sees the change

# Creating a copy creates a new object
c = a.copy()
c.append(5)  # Modifies only c's object
print(a)     # [1, 2, 3, 4] - a is unchanged
print(c)     # [1, 2, 3, 4, 5]
```

### Function Parameter Passing

Python uses "pass by object reference":

```python
def modify(lst, num):
    lst.append(4)    # Modifies the original list object
    num += 1         # Creates a new integer object
    print(f"Inside: lst={lst}, num={num}")

my_list = [1, 2, 3]
my_num = 10
modify(my_list, my_num)
print(f"Outside: my_list={my_list}, my_num={my_num}")
# Outside: my_list=[1, 2, 3, 4], my_num=10
```

## Example Questions & Answers

1. What does `id()` do?
   - Returns the memory address (identity) of an object

2. If `a = 89` and `b = 89`, is `a is b` True or False?
   - True (due to integer caching)

3. If `a = [1, 2, 3]` and `b = [1, 2, 3]`, is `a is b` True or False?
   - False (different list objects with same values)

4. If `a = [1, 2, 3]` and `b = a`, what happens when `a[0] = 'x'`?
   - Both `a` and `b` become `['x', 2, 3]` (they reference the same object)

## Project Tasks

The project contains multiple txt files (0-answer.txt, 1-answer.txt, etc.) each containing a single answer to a specific question about Python's object behavior.

## Advanced Concepts

<details>
<summary><strong>Copy vs. Deepcopy</strong></summary>

```python
import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy (copies outer list, but inner lists are referenced)
shallow = copy.copy(original)
shallow[0][0] = 'X'
print(original)  # [['X', 2, 3], [4, 5, 6]] - inner list modified

# Deep copy (copies everything recursively)
deep = copy.deepcopy(original)
deep[0][0] = 'Y'
print(original)  # [['X', 2, 3], [4, 5, 6]] - no change
```
</details>

<details>
<summary><strong>Garbage Collection</strong></summary>

Python uses reference counting and generational garbage collection:

```python
import gc
import sys

# Reference counting
a = []
print(sys.getrefcount(a) - 1)  # 1 reference

b = a  # Another reference to the same object
print(sys.getrefcount(a) - 1)  # 2 references

# Force garbage collection
gc.collect()
```
</details>

## Resources

* [Python Documentation: Objects, values and types](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
* [Python Tutor - Visualize Python execution](http://pythontutor.com/visualize.html)
* [Understanding Python Variables](https://realpython.com/python-variables/)
* [Python Garbage Collection](https://rushter.com/blog/python-garbage-collector/)
* [Immutable vs Mutable Types](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)

---

*Project by ALX Higher Level Programming*
