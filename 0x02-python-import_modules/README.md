# Python - Import & Modules

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/Ubuntu-20.04LTS-yellow.svg" alt="Ubuntu 20.04 LTS">
  <img src="https://img.shields.io/badge/Level-Beginner-green.svg" alt="Level - Beginner">
</p>

## Introduction

This project explores Python's module system, focusing on how to import and use functions from other files. Modules are essential for organizing code, promoting reusability, and building larger applications. The project also covers command line arguments, module discovery, and advanced import techniques.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

## Requirements

### General
* All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* A README.md file at the root of the folder of the project is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All files must be executable
* The length of your files will be tested using `wc`

## Project Tasks

<details>
<summary><strong>Task 0: Import a simple function from a simple file</strong></summary>

**File**: [0-add.py](./0-add.py)

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

* You have to use the `print` function with string format to display integers
* You have to assign:
  * the value `1` to a variable called `a`
  * the value `2` to a variable called `b`
  * and use those two variables as arguments when calling the `add` function
* You can't use the `from import` syntax
* Your code should not be executed when imported

**Example Output**:
```
1 + 2 = 3
```
</details>

<details>
<summary><strong>Task 1: My first toolbox!</strong></summary>

**File**: [1-calculation.py](./1-calculation.py)

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

* You have to import the functions: `add`, `sub`, `mul`, and `div` from `calculator_1.py`
* You have to use those functions to perform: addition, subtraction, multiplication, and division operations
* You have to define:
  * the value `10` to a variable `a`
  * the value `5` to a variable `b`
* Use these two variables to calculate operations
* You can't use the `*` syntax for importing
* Your code should not be executed when imported

**Example Output**:
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```
</details>

<details>
<summary><strong>Task 2: How to make a script dynamic!</strong></summary>

**File**: [2-args.py](./2-args.py)

Write a program that prints the number of and the list of its arguments.

* The output should be:
  * Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
  * `:` (or `.` if no arguments were passed) followed by
  * a new line, followed by (if at least one argument),
  * one line per argument: the position of the argument (starting at 1) followed by `:`, followed by the argument value and a new line
* Your code should not be executed when imported

**Example Output**:
```
$ ./2-args.py
0 arguments.
$ ./2-args.py Hello
1 argument:
1: Hello
$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```
</details>

<details>
<summary><strong>Task 3: Infinite addition</strong></summary>

**File**: [3-infinite_add.py](./3-infinite_add.py)

Write a program that prints the result of the addition of all arguments.

* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using `int()`
* Your code should not be executed when imported

**Example Output**:
```
$ ./3-infinite_add.py
0
$ ./3-infinite_add.py 79 10
89
$ ./3-infinite_add.py 79 10 -40 -300 89
-162
```
</details>

<details>
<summary><strong>Task 4: Who are you?</strong></summary>

**File**: [4-hidden_discovery.py](./4-hidden_discovery.py)

Write a program that prints all the names defined by the compiled module `hidden_4.pyc` (please download it locally).

* You should print one name per line, in alpha order
* You should print only names that do not start with `__`
* Your code should not be executed when imported
* Make sure to download the `hidden_4.pyc` file before testing
</details>

<details>
<summary><strong>Task 5: Everything can be imported</strong></summary>

**File**: [5-variable_load.py](./5-variable_load.py)

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

* You are not allowed to use `*` for importing
* Your code should not be executed when imported
</details>

<details>
<summary><strong>Task 6: Build my own calculator! (Advanced)</strong></summary>

**File**: [100-my_calculator.py](./100-my_calculator.py)

Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.

* Usage: `./100-my_calculator.py a operator b`
* If the number of arguments is not 3, your program should print `Usage: ./100-my_calculator.py <a> <operator> <b>` and exit with code 1
* If the operator is not one of +, -, *, or /, your program should print `Unknown operator. Available operators: +, -, * and /` and exit with code 1
* You can cast `a` and `b` into integers by using `int()`
* Your code should not be executed when imported

**Example Output**:
```
$ ./100-my_calculator.py 3 + 5
3 + 5 = 8
$ ./100-my_calculator.py 3 H 5
Unknown operator. Available operators: +, -, * and /
$ ./100-my_calculator.py 3 + 5 + 4
Usage: ./100-my_calculator.py <a> <operator> <b>
```
</details>

<details>
<summary><strong>Task 7: Easy print (Advanced)</strong></summary>

**File**: [101-easy_print.py](./101-easy_print.py)

Write a program that prints `#pythoniscool`, followed by a new line, in the standard output.

* Your program should be maximum 2 lines long
* You are not allowed to use `print` or `eval` or `open` or `import sys`
</details>

<details>
<summary><strong>Task 8: ByteCode -> Python #3 (Advanced)</strong></summary>

**File**: [102-magic_calculation.py](./102-magic_calculation.py)

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
</details>

<details>
<summary><strong>Task 9: Fast alphabet (Advanced)</strong></summary>

**File**: [103-fast_alphabet.py](./103-fast_alphabet.py)

Write a program that prints the alphabet in uppercase, followed by a new line.

* Your program should be maximum 3 lines long
* You are not allowed to use:
  * any loops
  * any conditional statements
  * `str.join()`
  * any string literal
  * any system calls
</details>

## Python Module Concepts

### Module System Basics
A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`. Modules help organize code by grouping related functionality.

### Import Methods
Python provides several ways to import modules:
- `import module_name` - Imports the entire module
- `from module_name import function_name` - Imports a specific function
- `from module_name import *` - Imports all functions (not recommended)
- `import module_name as alias` - Imports with an alias for shorter references

### The `dir()` Function
The built-in `dir()` function returns a list of names in the current scope or a list of attributes of an object. It's useful for examining modules to see what functions, classes, and variables they define.

### Execution Guards
The code `if __name__ == "__main__":` is used to prevent code from running when the module is imported. This allows a file to be used both as a script and as an importable module.

### Command Line Arguments
The `sys.argv` list contains command line arguments passed to a Python script. `sys.argv[0]` is the script name, and subsequent elements are the arguments.

## Key Points to Remember

- Module imports should be placed at the beginning of a file
- Always use execution guards to control what runs when a module is imported
- The `dir()` function helps explore what a module contains
- Python's standard library offers many useful modules
- Be specific about what you import to avoid namespace pollution
- Command line arguments provide flexibility for script execution

## Additional Resources

- [Python Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library](https://docs.python.org/3/library/index.html)
- [Python Import System](https://docs.python.org/3/reference/import.html)
- [Command Line Arguments in Python](https://docs.python.org/3/library/sys.html#sys.argv)

---

*Project by ALX Higher Level Programming*
