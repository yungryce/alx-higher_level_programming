# Python - if/else, loops, functions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/Ubuntu-20.04LTS-yellow.svg" alt="Ubuntu 20.04 LTS">
  <img src="https://img.shields.io/badge/Level-Beginner-green.svg" alt="Level - Beginner">
</p>

## Introduction

This project covers the fundamentals of Python's control flow tools: conditionals, loops, and functions. These concepts are essential for building more complex Python programs and are the building blocks for logical decision-making in your code.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why Python programming is awesome
* Why indentation is so important in Python
* How to use the `if`, `if...else` statements
* How to use comments in your code
* How to assign values to variables
* How to use the `while` and `for` loops
* How Python's `for` loop differs from C's
* How to use the `break` and `continue` statements
* How to use `else` clauses on loops
* What the `pass` statement does and when to use it
* How to use `range`
* What is a function and how to define and use one
* What a function returns if it doesn't use a `return` statement
* Scope of variables in Python
* What a traceback is and how to read it
* How to create and manipulate linked lists in a C/Python hybrid environment

## Requirements

### Python Scripts
* All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* Code should use the pycodestyle (version 2.8.*)
* All files must be executable
* Length of files will be tested using `wc`

### C Scripts
* All files compiled on Ubuntu 20.04 LTS using gcc with options: `-Wall -Werror -Wextra -pedantic -std=gnu89`
* All files should end with a new line
* Code should use the Betty style
* No more than 5 functions per file
* Prototypes of all functions should be included in a header file called `lists.h`
* Don't forget to push your header file
* All header files should be include guarded

## Project Tasks

<details>
<summary><strong>Task 0: Positive anything is better than negative nothing</strong></summary>

**File**: [0-positive_or_negative.py](./0-positive_or_negative.py)

This program assigns a random signed number to the variable `number` each time it is executed. It then prints whether the number stored in the variable is positive, zero, or negative.

**Example Output**:
```
-4 is negative
0 is zero
10 is positive
```
</details>

<details>
<summary><strong>Task 1: The last digit</strong></summary>

**File**: [1-last_digit.py](./1-last_digit.py)

This program assigns a random signed number to the variable `number` each time it is executed. It then prints the last digit of the number, along with some conditional text.

**Example Output**:
```
Last digit of 4205 is 5 and is less than 6 and not 0
Last digit of -626 is -6 and is less than 6 and not 0
Last digit of 1144 is 4 and is less than 6 and not 0
```
</details>

<details>
<summary><strong>Task 2: I sometimes suffer from insomnia...</strong></summary>

**File**: [2-print_alphabet.py](./2-print_alphabet.py)

This program prints the ASCII alphabet in lowercase, not followed by a new line, using only one print function and one loop.

**Output**:
```
abcdefghijklmnopqrstuvwxyz
```
</details>

<details>
<summary><strong>Task 3: When I was having that alphabet soup...</strong></summary>

**File**: [3-print_alphabt.py](./3-print_alphabt.py)

This program prints the ASCII alphabet in lowercase, excluding the letters 'q' and 'e', not followed by a new line.

**Output**:
```
abcdfghijklmnoprstuvwxyz
```
</details>

<details>
<summary><strong>Task 4: Hexadecimal printing</strong></summary>

**File**: [4-print_hexa.py](./4-print_hexa.py)

This program prints all numbers from 0 to 98 in decimal and in hexadecimal format.

**Example Output**:
```
0 = 0x0
1 = 0x1
...
97 = 0x61
98 = 0x62
```
</details>

<details>
<summary><strong>Task 5: 00...99</strong></summary>

**File**: [5-print_comb2.py](./5-print_comb2.py)

This program prints numbers from 0 to 99, separated by ", " and printed in ascending order with two digits.

**Output**:
```
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```
</details>

<details>
<summary><strong>Task 6: Inventing is a combination of brains and materials...</strong></summary>

**File**: [6-print_comb3.py](./6-print_comb3.py)

This program prints all possible different combinations of two digits, with the two digits being different and the smaller digit coming first. Numbers are printed in ascending order.

**Output**:
```
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```
</details>

<details>
<summary><strong>Task 7: islower</strong></summary>

**File**: [7-islower.py](./7-islower.py)

This function checks for lowercase character and returns `True` if the character is lowercase, `False` otherwise. This function works like Python's built-in `islower()` function.

**Example Usage**:
```python
print(islower('a'))  # True
print(islower('A'))  # False
```
</details>

<details>
<summary><strong>Task 8: To uppercase</strong></summary>

**File**: [8-uppercase.py](./8-uppercase.py)

This function prints a string in uppercase followed by a new line, only using one print and one loop.

**Example Usage**:
```python
uppercase("best")  # Outputs: BEST
uppercase("Best School 98 Battery street")  # Outputs: BEST SCHOOL 98 BATTERY STREET
```
</details>

<details>
<summary><strong>Task 9: There are only 3 colors...</strong></summary>

**File**: [9-print_last_digit.py](./9-print_last_digit.py)

This function prints the last digit of a number and returns that value.

**Example Usage**:
```python
print_last_digit(98)  # Outputs: 8 (and returns: 8)
print_last_digit(-1024)  # Outputs: 4 (and returns: 4)
```
</details>

<details>
<summary><strong>Task 10: a + b</strong></summary>

**File**: [10-add.py](./10-add.py)

This function adds two integers and returns the result.

**Example Usage**:
```python
print(add(1, 2))  # Outputs: 3
print(add(98, 0))  # Outputs: 98
```
</details>

<details>
<summary><strong>Task 11: a ^ b</strong></summary>

**File**: [11-pow.py](./11-pow.py)

This function computes `a` to the power of `b` and returns the value.

**Example Usage**:
```python
print(pow(2, 2))  # Outputs: 4
print(pow(98, 2))  # Outputs: 9604
print(pow(98, 0))  # Outputs: 1
print(pow(100, -2))  # Outputs: 0.0001
```
</details>

<details>
<summary><strong>Task 12: Fizz Buzz</strong></summary>

**File**: [12-fizzbuzz.py](./12-fizzbuzz.py)

This function prints the numbers from 1 to 100 separated by a space. For multiples of three, it prints "Fizz" instead of the number. For multiples of five, it prints "Buzz". For numbers that are multiples of both three and five, it prints "FizzBuzz".

**Example Usage**:
```python
fizzbuzz()  
# Outputs: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16...
```
</details>

<details>
<summary><strong>Task 13: Insert in sorted linked list</strong></summary>

**Files**: 
- [13-insert_number.c](./13-insert_number.c)
- [lists.h](./lists.h)

This C function inserts a number into a sorted singly linked list. It returns the address of the new node, or NULL if it failed.

**Example Linked List Before Insertion**:
```
0 -> 1 -> 2 -> 3 -> 4 -> 98
```

**Example Linked List After Insertion of 27**:
```
0 -> 1 -> 2 -> 3 -> 4 -> 27 -> 98
```
</details>

<details>
<summary><strong>Task 14: Smile in the mirror (Advanced)</strong></summary>

**File**: [100-print_tebahpla.py](./100-print_tebahpla.py)

This program prints the ASCII alphabet in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase).

**Output**:
```
zYxWvUtSrQpOnMlKjIhGfEdCbA
```
</details>

<details>
<summary><strong>Task 15: Remove at position (Advanced)</strong></summary>

**File**: [101-remove_char_at.py](./101-remove_char_at.py)

This function creates a copy of a string, removing the character at the position `n` (not using the `str.replace()`).

**Example Usage**:
```python
print(remove_char_at("Best School", 3))  # Outputs: "Bes School"
print(remove_char_at("Chicago", 2))  # Outputs: "Chcago"
print(remove_char_at("C is fun!", 0))  # Outputs: " is fun!"
```
</details>

<details>
<summary><strong>Task 16: ByteCode -> Python #2 (Advanced)</strong></summary>

**File**: [102-magic_calculation.py](./102-magic_calculation.py)

This function does exactly the same as a provided Python bytecode.

</details>

## Python Control Flow Concepts

### Conditional Statements
Python's `if`, `elif`, and `else` statements allow your program to make decisions based on the evaluation of conditions. The indentation in Python determines the block of code that will be executed when a condition is met.

### Loops
Python has two primary loop constructs:
- **for loop**: Iterates over a sequence (list, tuple, string, etc.)
- **while loop**: Continues to execute as long as a condition is true

### Functions
Functions in Python are defined using the `def` keyword. They allow you to encapsulate reusable pieces of code and make your programs more modular.

### ASCII and Character Manipulation
Python offers easy ways to work with ASCII values:
- `ord()`: Converts a character to its ASCII value
- `chr()`: Converts an ASCII value to its character

## Key Points to Remember

- Python is indentation-sensitive; consistent indentation is crucial
- The `range()` function generates a sequence of numbers
- Python's `for` loop iterates over a sequence, unlike C's for loop
- Functions without a `return` statement return `None` by default
- Variables defined inside a function have a local scope

## Additional Resources

- [Python Documentation on Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Built-ins](https://docs.python.org/3/library/functions.html)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

---

*Project by ALX Higher Level Programming*
