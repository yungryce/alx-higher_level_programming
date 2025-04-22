# Python - Test-Driven Development

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/TDD-Testing-green.svg" alt="TDD Testing">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project introduces Test-Driven Development (TDD) in Python, a methodology where tests are written before implementing the actual code. The project covers both doctest and unittest frameworks, focusing on creating comprehensive test cases and writing well-documented, robust code.

## Learning Objectives

* Understand the importance of tests in programming
* Learn the Test-Driven Development approach
* Master doctest for creating interactive tests in docstrings
* Implement unittest for more structured testing
* Write comprehensive documentation with examples
* Identify and test edge cases
* Validate function behavior through tests

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*
* All files must have documentation

## Project Tasks

<details>
<summary><strong>Integer Operations</strong></summary>

* **Task 0**: [0-add_integer.py](./0-add_integer.py) & [tests/0-add_integer.txt](./tests/0-add_integer.txt)
  * Function that adds two integers
  * Validates input types and handles type conversion
  * Tested with doctest
</details>

<details>
<summary><strong>Matrix Operations</strong></summary>

* **Task 1**: [2-matrix_divided.py](./2-matrix_divided.py) & [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * Function that divides all elements of a matrix
  * Validates matrix structure and divisor
  * Returns a new matrix with results

* **Task 6**: [100-matrix_mul.py](./100-matrix_mul.py) & [tests/100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * Function that multiplies two matrices
  * Validates matrix dimensions for multiplication
  * Performs matrix multiplication algorithm

* **Task 7**: [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py) & [tests/101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)
  * Matrix multiplication using NumPy
  * More efficient implementation with validation
</details>

<details>
<summary><strong>String Operations</strong></summary>

* **Task 2**: [3-say_my_name.py](./3-say_my_name.py) & [tests/3-say_my_name.txt](./tests/3-say_my_name.txt)
  * Function that prints a formatted name string
  * Validates input types for first and last name

* **Task 4**: [5-text_indentation.py](./5-text_indentation.py) & [tests/5-text_indentation.txt](./tests/5-text_indentation.txt)
  * Function that adds line breaks after certain punctuation
  * Formats text with proper spacing and indentation
</details>

<details>
<summary><strong>Geometric Operations</strong></summary>

* **Task 3**: [4-print_square.py](./4-print_square.py) & [tests/4-print_square.txt](./tests/4-print_square.txt)
  * Function that prints a square using # characters
  * Validates size input is a positive integer
</details>

<details>
<summary><strong>List Operations</strong></summary>

* **Task 5**: [6-max_integer.py](./6-max_integer.py) & [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)
  * Function that finds the maximum integer in a list
  * Tested with unittest instead of doctest
</details>

<details>
<summary><strong>C/Python Integration</strong></summary>

* **Task 8**: [102-python.c](./102-python.c)
  * C function that prints Python string information
  * Demonstrates integration of C with Python
</details>

## Testing Frameworks

### Doctest

Doctest allows embedding tests directly in function docstrings:

```python
def add(a, b):
    """
    Add two numbers and return the result.
    
    >>> add(1, 2)
    3
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b
```

Run with:
```
python3 -m doctest -v ./tests/0-add_integer.txt
```

### Unittest

Unittest provides a more structured framework for testing:

```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
        
    def test_zero(self):
        self.assertEqual(add(0, 0), 0)
        
    def test_type_error(self):
        with self.assertRaises(TypeError):
            add("a", 2)
```

Run with:
```
python3 -m unittest tests/6-max_integer_test.py
```

## The TDD Process

1. **Write Test**: Define expected behavior through test cases
2. **Run Test**: Ensure it fails (proves test is valid)
3. **Write Code**: Implement minimum code to pass the test
4. **Run Test Again**: Verify implementation passes
5. **Refactor**: Clean up code while keeping tests passing
6. **Repeat**: Add more tests for additional features/edge cases

## Test Categories

* **Functionality Tests**: Verify the code does what it should
* **Edge Case Tests**: Check behavior with boundary values
* **Error Tests**: Validate proper error handling
* **Performance Tests**: Ensure efficient operation (when applicable)

## Resources

* [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
* [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
* [Test-Driven Development with Python](https://www.obeythetestinggoat.com/pages/book.html)

---

*Project by ALX Higher Level Programming*