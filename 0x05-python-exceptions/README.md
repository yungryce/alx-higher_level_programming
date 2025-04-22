# Python - Exceptions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/Error-Handling-red.svg" alt="Error Handling">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project explores Python's exception handling mechanisms, a critical skill for building robust applications. Proper error handling allows programs to respond gracefully to unexpected conditions, provide meaningful feedback, and continue execution where appropriate rather than crashing.

## Learning Objectives

* Understand the difference between errors and exceptions
* Learn how to use try-except blocks effectively
* Master exception handling with multiple exception types
* Implement resource cleanup with finally clauses
* Raise built-in exceptions with custom messages
* Route error messages to standard error
* Create C functions that handle Python exceptions

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*
* GCC for C functions

## Project Tasks

<details>
<summary><strong>Basic Exception Handling</strong></summary>

* **Task 0**: [0-safe_print_list.py](./0-safe_print_list.py)
  * Function that prints `x` elements of a list
  * Handles IndexError when accessing beyond list bounds
  * Returns the number of elements actually printed

* **Task 1**: [1-safe_print_integer.py](./1-safe_print_integer.py)
  * Function that prints an integer with `"{:d}".format()`
  * Returns True if value is printed correctly (is an integer)
  * Returns False if TypeError or ValueError occurs

* **Task 2**: [2-safe_print_list_integers.py](./2-safe_print_list_integers.py)
  * Function that prints the first `x` integers of a list
  * Skips non-integer elements without errors
  * Returns the number of integers printed
</details>

<details>
<summary><strong>Advanced Exception Techniques</strong></summary>

* **Task 3**: [3-safe_print_division.py](./3-safe_print_division.py)
  * Function that divides two integers and prints the result
  * Uses try-except-finally to handle errors and ensure output
  * Returns division result or None if division fails

* **Task 4**: [4-list_division.py](./4-list_division.py)
  * Function that divides two lists element by element
  * Handles multiple exception types with specific messages
  * Returns a new list with division results
</details>

<details>
<summary><strong>Raising Exceptions</strong></summary>

* **Task 5**: [5-raise_exception.py](./5-raise_exception.py)
  * Function that raises a TypeError exception
  * Demonstrates how to deliberately trigger exceptions

* **Task 6**: [6-raise_exception_msg.py](./6-raise_exception_msg.py)
  * Function that raises a NameError with a custom message
  * Shows how to provide informative error details
</details>

<details>
<summary><strong>System Integration</strong></summary>

* **Task 7**: [100-safe_print_integer_err.py](./100-safe_print_integer_err.py)
  * Function that prints an integer with error handling
  * Sends error messages to stderr using sys.stderr
  * Returns True if successful, False otherwise

* **Task 8**: [101-safe_function.py](./101-safe_function.py)
  * Function that executes another function safely
  * Captures and reports any exceptions to stderr
  * Returns function result or None if exception occurs

* **Task 9**: [102-magic_calculation.py](./102-magic_calculation.py)
  * Python function that matches given Python bytecode
  * Demonstrates exception handling in compiled form
</details>

<details>
<summary><strong>C/Python Integration</strong></summary>

* **Task 10**: [103-python.c](./103-python.c)
  * C functions that print Python objects information
  * Handles bytes, list, and float objects with proper type checking
  * Demonstrates Python/C API exception safety
</details>

## Exception Handling in Python

### Try-Except Structure
```python
try:
    # Code that might raise exceptions
    result = risky_operation()
except ExceptionType:
    # Handle specific exception
    handle_error()
```

### Multiple Exception Types
```python
try:
    value = int(user_input)
except ValueError:
    print("Not a valid integer")
except TypeError:
    print("Expected a string")
```

### Try-Except-Else-Finally
```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
else:
    # Runs only if no exception occurred
    process_content(content)
finally:
    # Always executes, used for cleanup
    if 'file' in locals() and file:
        file.close()
```

### Raising Exceptions
```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
```

### Exception Hierarchy
- **BaseException**: Root of exception hierarchy
  - **Exception**: Base class for most exceptions
    - **TypeError**: Wrong type of argument
    - **ValueError**: Right type but wrong value
    - **ZeroDivisionError**: Division by zero
    - **IndexError**: Index out of range
    - **KeyError**: Key not found in dictionary
    - **FileNotFoundError**: File not found
    - **IOError**: Input/Output error
    - **ImportError**: Module not found

## Best Practices

1. **Be Specific**: Catch specific exceptions rather than bare `except:` clause
2. **Keep it Brief**: Make try blocks as small as needed to isolate errors
3. **Clean Up**: Use finally blocks to ensure resources are properly released
4. **Fail Fast**: Validate inputs early to avoid deep error conditions
5. **Stay Informed**: Capture exception information with `except Exception as e`
6. **Log Properly**: Use sys.stderr for error messages, not print()

## Resources

* [Python Docs - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [Real Python - Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)

---

*Project by ALX Higher Level Programming*
