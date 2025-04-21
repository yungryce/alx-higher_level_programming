# Python Hello World

This directory contains introductory exercises for Python programming, focusing on basic syntax, string manipulation, and output operations.

## Learning Objectives

By completing the exercises in this directory, you will be able to:
- Run Python scripts using various methods (interpreter, shell script)
- Understand and use the Python print function with string formatting
- Work with strings including indexing, slicing, and concatenation
- Utilize Python's built-in functions and libraries for basic operations
- Apply PEP 8 style guidelines to your Python code
- Connect Python with C code through extension modules
- Understand Python's execution environment and interpreter

## What is Python?

Python is a high-level, interpreted programming language known for its readability and versatility. Created by Guido van Rossum and first released in 1991, Python emphasizes code readability with its notable use of significant whitespace.

Key characteristics of Python include:
- **Interpreted**: Python code is executed line by line by the Python interpreter
- **Dynamically Typed**: Variable types are determined at runtime
- **Extensive Standard Library**: Comes with a rich set of modules and packages
- **Multi-Paradigm**: Supports procedural, object-oriented, and functional programming
- **Cross-Platform**: Runs on various operating systems (Windows, macOS, Linux)

## Python vs. Other Languages

Compared to C (covered in previous modules):
- Python uses indentation instead of braces to define code blocks
- No need for semicolons to end statements
- Variable declaration does not require specifying data types
- Memory management is automatic through garbage collection
- Higher level of abstraction from hardware details

## Getting Started with Python

### Python Interpreter

Python uses an interpreter that executes code line-by-line. The interpreter can be used interactively:

```bash
$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> exit()
```

### Running Python Scripts

There are multiple ways to run Python scripts:

1. **Directly through the interpreter**:
   ```bash
   python3 script.py
   ```

2. **Making the script executable**:
   ```bash
   chmod +x script.py
   ./script.py  # First line must be #!/usr/bin/python3
   ```

3. **Using Python's `-c` flag for inline code**:
   ```bash
   python3 -c 'print("Hello, World!")'
   ```

## Basic Python Syntax

### Variables and Data Types

Python's basic data types include:

```python
# Numbers
integer_var = 42
float_var = 3.14

# Strings
single_quoted = 'Hello'
double_quoted = "World"
triple_quoted = """Multiple
line string"""

# Boolean
is_active = True
is_completed = False

# None type (similar to NULL in C)
empty_var = None
```

### String Operations

Strings in Python are immutable sequences of characters with various built-in operations:

```python
# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"

# String repetition
repeated = "Ha" * 3  # "HaHaHa"

# String indexing (0-based)
first_char = full_name[0]  # "J"
last_char = full_name[-1]  # "e"

# String slicing
substring = full_name[0:4]  # "John"

# String length
name_length = len(full_name)  # 8
```

### Print Function

The `print()` function displays output with various formatting options:

```python
# Simple output
print("Hello, World!")

# Multiple arguments
print("Name:", full_name, "Age:", 30)

# Using format specifiers
print("Number: {}, String: {}".format(42, "test"))

# Using f-strings (Python 3.6+)
age = 30
print(f"Name: {full_name}, Age: {age}")

# Controlling end character (default is newline)
print("Hello", end=" ")
print("World")  # Outputs: "Hello World"
```

## The Zen of Python

The Zen of Python is a collection of 19 guiding principles for writing computer programs in Python. View it by running:

```python
import this
```

Key principles include:
- Beautiful is better than ugly
- Explicit is better than implicit
- Simple is better than complex
- Readability counts

## Project Files

### Python Execution
- **[0-run](./0-run)**: Shell script that runs a Python script stored in an environment variable
- **[1-run_inline](./1-run_inline)**: Shell script that runs Python code stored in an environment variable
- **[2-print.py](./2-print.py)**: Python script that prints a specific string

### String Manipulation
- **[3-print_number.py](./3-print_number.py)**: Prints an integer stored in a variable followed by text
- **[4-print_float.py](./4-print_float.py)**: Prints a float with a precision of 2 digits
- **[5-print_string.py](./5-print_string.py)**: Prints a string multiple times, then prints a slice of it
- **[6-concat.py](./6-concat.py)**: Concatenates two strings to form a full sentence
- **[7-edges.py](./7-edges.py)**: Extracts different slices from a string
- **[8-concat_edges.py](./8-concat_edges.py)**: Creates a new string from parts of an existing string

### Advanced Topics
- **[9-easter_egg.py](./9-easter_egg.py)**: Prints "The Zen of Python" by importing the `this` module
- **[10-check_cycle.c](./10-check_cycle.c)**: C function that checks if a linked list has a cycle
- **[100-write.py](./100-write.py)**: Prints to stderr using the `sys.stderr.write()` function
- **[101-compile](./101-compile)**: Script that compiles a Python file to bytecode
- **[102-magic_calculation.py](./102-magic_calculation.py)**: Python function matching a provided bytecode

## String Formatting in Python

Python offers multiple ways to format strings:

### Old-style Formatting (% operator)
```python
name = "John"
age = 30
print("Name: %s, Age: %d" % (name, age))
```

### str.format() Method
```python
name = "John"
age = 30
print("Name: {}, Age: {}".format(name, age))

# With position
print("{1} is {0} years old".format(age, name))

# With keywords
print("{name} is {age} years old".format(name="John", age=30))
```

### f-strings (Python 3.6+)
```python
name = "John"
age = 30
print(f"Name: {name}, Age: {age}")

# With expressions
print(f"Next year, {name} will be {age + 1} years old")
```

## Python and C Integration

Python can be extended with C through extension modules. This is useful for performance-critical code or interfacing with system libraries.

```c
// Simple C extension example
#include <Python.h>

static PyObject* hello_world(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello, World!");
}

static PyMethodDef methods[] = {
    {"hello_world", hello_world, METH_NOARGS, "Returns Hello, World!"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "hello", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_hello(void) {
    return PyModule_Create(&module);
}
```

## Python Style Guide (PEP 8)

Writing clean, readable code is essential in Python. The PEP 8 style guide defines conventions for:

### Indentation
- Use 4 spaces per indentation level
- Continuation lines should align wrapped elements

### Maximum Line Length
- Limit lines to 79 characters
- Limit docstrings/comments to 72 characters

### Imports
- Import order: standard library, third-party, local application
- One import per line
- Avoid wildcard imports (`from module import *`)

### Naming Conventions
- Functions, variables, and modules: `lowercase_with_underscores`
- Classes: `CapitalizedWords`
- Constants: `ALL_CAPS_WITH_UNDERSCORES`

### Spacing
- Use blank lines to separate functions and classes
- Use spaces around operators and after commas
- Avoid extraneous whitespace

## Python Execution Process

When you run a Python script, the following happens:

1. **Parsing**: Python reads the source file and checks for syntax errors
2. **Compilation**: Python compiles the source to bytecode
3. **Interpretation**: The Python Virtual Machine (PVM) executes the bytecode

For frequently used modules, Python saves the bytecode (`.pyc` files) to avoid recompilation.

## Common Pitfalls for Beginners

1. **Indentation Errors**: Improper indentation causes syntax errors
2. **Mutable Default Arguments**: Default arguments are evaluated once at function definition
3. **Integer Division**: In Python 3, `5 / 2` returns `2.5` (use `//` for integer division)
4. **String Immutability**: Cannot modify strings in-place
5. **Variable Scope**: Variables defined inside functions are not accessible outside

## Best Practices

1. **Use Meaningful Names**: Choose descriptive names for variables and functions
2. **Comment Your Code**: Explain complex logic and why, not what
3. **Keep Functions Small**: Each function should do one thing well
4. **Handle Exceptions**: Use try/except to gracefully handle errors
5. **Use Built-in Functions**: Leverage Python's rich standard library
6. **Follow PEP 8**: Maintain consistent style throughout your code

## Tools and Resources

### Code Style Checkers
- **pycodestyle**: Checks code against PEP 8 style convention
  ```bash
  pip install pycodestyle
  pycodestyle your_script.py
  ```

### Python Documentation
- [Official Python Documentation](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Interactive Learning
- [Python Tutor](http://www.pythontutor.com/) - Visualize code execution
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)
- [HackerRank Python Challenges](https://www.hackerrank.com/domains/python)

## Conclusion

Python's simplicity and readability make it an excellent language for beginners, while its power and flexibility make it valuable for experienced developers. This module introduces the fundamental concepts needed to build a solid foundation in Python programming.

Remember, the best way to learn Python is by writing code. Experiment with the examples, modify them, and create your own programs to reinforce your understanding.
