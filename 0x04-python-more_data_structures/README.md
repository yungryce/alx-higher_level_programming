# Python - More Data Structures: Set, Dictionary

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/PEP8-Style-orange.svg" alt="PEP8 Style">
  <img src="https://img.shields.io/badge/Functional-Programming-purple.svg" alt="Functional Programming">
  <img src="https://img.shields.io/badge/Level-Intermediate-yellow.svg" alt="Level - Intermediate">
</p>

## Overview

This project explores Python's advanced data structures: sets and dictionaries, along with functional programming concepts like lambda functions and map/filter operations. These powerful tools enable efficient data manipulation and transformation, critical for writing concise, optimized Python code.

## Learning Objectives

* Learn what sets are and how to use them
* Discover when to use sets versus lists
* Master dictionary creation and manipulation
* Understand lambda functions and their applications
* Implement map, filter, and reduce operations
* Create C functions to interact with Python objects

## Requirements

* Python 3.8.5
* Ubuntu 20.04 LTS
* pycodestyle 2.8.*
* GCC for C functions

## Project Structure

<details>
<summary><strong>Matrix Operations</strong></summary>

* **Task 0**: [0-square_matrix_simple.py](./0-square_matrix_simple.py)
  * Compute square value of all integers in a matrix
  * Returns a new matrix with the result

* **Task 13**: [101-square_matrix_map.py](./101-square_matrix_map.py)
  * Square matrix values using map and lambda
  * Maximum 3 lines of code
</details>

<details>
<summary><strong>Functional Programming</strong></summary>

* **Task 1**: [1-search_replace.py](./1-search_replace.py)
  * Replace all occurrences of an element in a list

* **Task 11**: [11-multiply_list_map.py](./11-multiply_list_map.py)
  * Multiply list values by a number using map
  * Maximum 3 lines of code

* **Task 12**: [100-weight_average.py](./100-weight_average.py)
  * Calculate weighted average from a list of tuples
</details>

<details>
<summary><strong>Set Operations</strong></summary>

* **Task 2**: [2-uniq_add.py](./2-uniq_add.py)
  * Add all unique integers in a list

* **Task 3**: [3-common_elements.py](./3-common_elements.py)
  * Return common elements between two sets

* **Task 4**: [4-only_diff_elements.py](./4-only_diff_elements.py)
  * Return elements present in only one set
</details>

<details>
<summary><strong>Dictionary Operations</strong></summary>

* **Task 5**: [5-number_keys.py](./5-number_keys.py)
  * Return number of keys in a dictionary

* **Task 6**: [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py)
  * Print dictionary by ordered keys

* **Task 7**: [7-update_dictionary.py](./7-update_dictionary.py)
  * Replace or add key/value in a dictionary

* **Task 8**: [8-simple_delete.py](./8-simple_delete.py)
  * Delete a key in a dictionary

* **Task 9**: [9-multiply_by_2.py](./9-multiply_by_2.py)
  * Multiply all values in a dictionary by 2

* **Task 10**: [10-best_score.py](./10-best_score.py)
  * Return key with the biggest integer value

* **Task 14**: [102-complex_delete.py](./102-complex_delete.py)
  * Delete keys with a specific value in a dictionary
</details>

<details>
<summary><strong>Special Applications</strong></summary>

* **Task 13**: [12-roman_to_int.py](./12-roman_to_int.py)
  * Convert Roman numeral to integer
  * Handle cases I to MMMCMXCIX (1 to 3999)
</details>

<details>
<summary><strong>C/Python Integration</strong></summary>

* **Task 16**: [103-python.c](./103-python.c)
  * C functions that print Python objects (lists, bytes)
  * Demonstrates Python/C API usage
</details>

## Key Concepts

### Sets
```python
# Creation
my_set = {1, 2, 3, 4}
empty_set = set()

# Operations
union = set_a | set_b  # Elements in either set
intersection = set_a & set_b  # Elements in both sets
difference = set_a - set_b  # Elements in set_a but not in set_b
symmetric_diff = set_a ^ set_b  # Elements in either set but not both

# Methods
my_set.add(5)  # Add element
my_set.remove(2)  # Remove element (raises error if missing)
my_set.discard(2)  # Remove element (no error if missing)
```

### Dictionaries
```python
# Creation
my_dict = {'key1': 'value1', 'key2': 'value2'}
empty_dict = {}

# Operations
value = my_dict['key1']  # Access (raises error if missing)
value = my_dict.get('key1', default)  # Access with default
my_dict['key3'] = 'value3'  # Add or update
del my_dict['key1']  # Delete key

# Methods
keys = my_dict.keys()  # Get all keys
values = my_dict.values()  # Get all values
items = my_dict.items()  # Get all key-value pairs
```

### Functional Programming
```python
# Lambda functions
add = lambda x, y: x + y
square = lambda x: x**2

# Map - Apply function to every item
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))  # [1, 4, 9, 16]

# Filter - Keep items that match condition
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # [2, 4]

# List comprehensions
squared = [x**2 for x in [1, 2, 3, 4]]  # [1, 4, 9, 16]
evens = [x for x in [1, 2, 3, 4] if x % 2 == 0]  # [2, 4]
```

## When to Use Different Data Structures

| Data Structure | Best For | Advantages | Limitations |
|----------------|----------|------------|-------------|
| **Lists** | Ordered collections | Indexing, slicing, mutable | Slow lookups, duplicates |
| **Sets** | Unique items, membership tests | Fast lookups, mathematical set ops | No indexing, unordered |
| **Dictionaries** | Key-value mappings | Fast lookups, flexible keys | No inherent order (pre-3.7) |
| **Tuples** | Immutable sequences | Hashable (can be dict keys/set items) | Fixed size after creation |

## Resources

* [Python Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)
* [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [Lambda, Filter, Reduce and Map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
* [Python C API](https://docs.python.org/3.8/c-api/index.html)

---

*Project by ALX Higher Level Programming*
