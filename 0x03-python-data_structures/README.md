# Python - Data Structures: Lists, Tuples

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/C-Integration-red.svg" alt="C Integration">
  <img src="https://img.shields.io/badge/Level-Beginner-green.svg" alt="Level - Beginner">
</p>

## Introduction

This project explores Python's fundamental data structures: lists and tuples. These structures allow you to store, organize, and manipulate collections of data efficiently. The project covers basic operations, manipulation techniques, and even C language integration with Python's data structures.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why Python programming is awesome
* What lists are and how to use them
* What the differences are between strings and lists
* What the most common methods of lists are and how to use them
* How to use lists as stacks and queues
* What list comprehensions are and how to use them
* What tuples are and how to use them
* When to use tuples versus lists
* What a sequence is in Python
* What tuple packing is
* What sequence unpacking is
* What the `del` statement is and how to use it

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
<summary><strong>Task 0: Print a list of integers</strong></summary>

**File**: [0-print_list_integer.py](./0-print_list_integer.py)

Write a function that prints all integers of a list.

* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```
**Output**:
```
1
2
3
4
5
```
</details>

<details>
<summary><strong>Task 1: Secure access to an element in a list</strong></summary>

**File**: [1-element_at.py](./1-element_at.py)

Write a function that retrieves an element from a list like in C.

* Prototype: `def element_at(my_list, idx):`
* If idx is negative, the function should return None
* If idx is out of range (> of number of element in my_list), the function should return None
* You are not allowed to import any module
* You are not allowed to use try/except

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
```
**Output**:
```
Element at index 3 is 4
```
</details>

<details>
<summary><strong>Task 2: Replace element</strong></summary>

**File**: [2-replace_in_list.py](./2-replace_in_list.py)

Write a function that replaces an element of a list at a specific position (like in C).

* Prototype: `def replace_in_list(my_list, idx, element):`
* If idx is negative, the function should not modify anything, and returns the original list
* If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use try/except

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
```
**Output**:
```
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```
</details>

<details>
<summary><strong>Task 3: Print a list of integers... in reverse!</strong></summary>

**File**: [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py)

Write a function that prints all integers of a list, in reverse order.

* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
```
**Output**:
```
5
4
3
2
1
```
</details>

<details>
<summary><strong>Task 4: Replace in a copy</strong></summary>

**File**: [4-new_in_list.py](./4-new_in_list.py)

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

* Prototype: `def new_in_list(my_list, idx, element):`
* If idx is negative, the function should return a copy of the original list
* If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
* You are not allowed to import any module
* You are not allowed to use try/except

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
```
**Output**:
```
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```
</details>

<details>
<summary><strong>Task 5: Can you C me now?</strong></summary>

**File**: [5-no_c.py](./5-no_c.py)

Write a function that removes all characters c and C from a string.

* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`

**Example**:
```python
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
```
**Output**:
```
Best Shool
hiago
 is fun!
```
</details>

<details>
<summary><strong>Task 6: Lists of lists = Matrix</strong></summary>

**File**: [6-print_matrix_integer.py](./6-print_matrix_integer.py)

Write a function that prints a matrix of integers.

* Prototype: `def print_matrix_integer(matrix=[[]]):`
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

**Example**:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
print("--")
print_matrix_integer()
```
**Output**:
```
1 2 3
4 5 6
7 8 9
--

```
</details>

<details>
<summary><strong>Task 7: Tuples addition</strong></summary>

**File**: [7-add_tuple.py](./7-add_tuple.py)

Write a function that adds 2 tuples.

* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value 0 for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

**Example**:
```python
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
```
**Output**:
```
(89, 100)
(2, 89)
(1, 89)
```
</details>

<details>
<summary><strong>Task 8: More returns!</strong></summary>

**File**: [8-multiple_returns.py](./8-multiple_returns.py)

Write a function that returns a tuple with the length of a string and its first character.

* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module

**Example**:
```python
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
```
**Output**:
```
Length: 22 - First character: A
```
</details>

<details>
<summary><strong>Task 9: Find the max</strong></summary>

**File**: [9-max_integer.py](./9-max_integer.py)

Write a function that finds the biggest integer of a list.

* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the built-in `max()`

**Example**:
```python
my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
```
**Output**:
```
Max: 90
```
</details>

<details>
<summary><strong>Task 10: Only by 2</strong></summary>

**File**: [10-divisible_by_2.py](./10-divisible_by_2.py)

Write a function that finds all multiples of 2 in a list.

* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

**Example**:
```python
my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
```
**Output**:
```
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```
</details>

<details>
<summary><strong>Task 11: Delete at</strong></summary>

**File**: [11-delete_at.py](./11-delete_at.py)

Write a function that deletes the item at a specific position in a list.

* Prototype: `def delete_at(my_list=[], idx=0):`
* If idx is negative or out of range, nothing changes (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module

**Example**:
```python
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)
```
**Output**:
```
[1, 2, 3, 5]
[1, 2, 3, 5]
```
</details>

<details>
<summary><strong>Task 12: Switch</strong></summary>

**File**: [12-switch.py](./12-switch.py)

Complete the given source code to switch values of `a` and `b`:

```python
#!/usr/bin/python3
a = 89
b = 10
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("a={:d} - b={:d}".format(a, b))
```

**Output**:
```
a=10 - b=89
```
</details>

<details>
<summary><strong>Task 13: Linked list palindrome</strong></summary>

**Files**: 
- [13-is_palindrome.c](./13-is_palindrome.c)
- [lists.h](./lists.h)

Write a function in C that checks if a singly linked list is a palindrome.

* Prototype: `int is_palindrome(listint_t **head);`
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
* An empty list is considered a palindrome

**Example**:
```c
// Testing code provided that creates a linked list and checks if it's a palindrome
```
</details>

<details>
<summary><strong>Task 14: CPython #0: Python lists (Advanced)</strong></summary>

**File**: [100-print_python_list_info.c](./100-print_python_list_info.c)

Create a C function that prints some basic info about Python lists.

* Prototype: `void print_python_list_info(PyObject *p);`
* Python version: 3.4
* Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
* Format of the output:
  * Size of the list
  * Allocated memory
  * Type of each element

**Example Output**:
```
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
```
</details>

## Python Data Structures: Key Concepts

### Lists
Lists are ordered, mutable collections that can store elements of different types.

```python
# List creation
my_list = [1, 2, 3, 4, 5]

# Common operations
my_list.append(6)       # Add element at end
my_list.insert(2, 10)   # Insert at index 2
my_list.remove(3)       # Remove first occurrence of value
my_list.pop(1)          # Remove and return element at index 1
my_list.index(4)        # Get index of first occurrence of value
my_list.count(2)        # Count occurrences of value
my_list.sort()          # Sort in-place
my_list.reverse()       # Reverse in-place
my_list.copy()          # Return a shallow copy
my_list.clear()         # Remove all items

# Accessing elements
first = my_list[0]      # First element
last = my_list[-1]      # Last element
slice = my_list[1:3]    # Elements from index 1 to 2

# List as stack (LIFO)
my_list.append(value)   # Push
my_list.pop()           # Pop

# List as queue (FIFO)
my_list.append(value)   # Enqueue
my_list.pop(0)          # Dequeue (inefficient, use collections.deque)

# List comprehension
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Tuples
Tuples are ordered, immutable collections that can store elements of different types.

```python
# Tuple creation
my_tuple = (1, 2, 3, 4, 5)
single_element = (1,)   # Note the comma

# Tuple operations
length = len(my_tuple)
max_value = max(my_tuple)
min_value = min(my_tuple)
sum_values = sum(my_tuple)

# Accessing elements (same as lists)
first = my_tuple[0]
last = my_tuple[-1]
slice = my_tuple[1:3]

# Tuple packing
coordinates = 10, 20

# Tuple unpacking
x, y = coordinates

# Multiple assignment
a, b = 1, 2
a, b = b, a  # Swap values
```

### Lists vs. Tuples: When to Use Which

**Use Lists When:**
- You need a collection that might change
- You need to append or remove elements
- You need to sort or reverse elements in-place
- You're representing a collection of similar items

**Use Tuples When:**
- You need an immutable sequence
- You want to ensure data integrity
- You're using it as a dictionary key (lists can't be used as keys)
- You're returning multiple values from a function
- You want to represent fixed data like coordinates or RGB values

## Additional Resources

- [Python Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Documentation - Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python C API Reference - Lists](https://docs.python.org/3/c-api/list.html)
- [Python C API Reference - Tuples](https://docs.python.org/3/c-api/tuple.html)
- [Understanding Lists in Python](https://realpython.com/python-lists-tuples/)
- [Python List Methods](https://www.w3schools.com/python/python_ref_list.asp)

---

*Project by ALX Higher Level Programming*
