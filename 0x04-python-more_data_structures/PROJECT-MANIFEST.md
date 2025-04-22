# Project Manifest: Python More Data Structures - Sets, Dictionaries

## Project Identity
- **Name**: Python - More Data Structures: Set, Dictionary
- **Type**: Educational
- **Scope**: Advanced Python Data Structure Concepts
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5
- **Supporting**: C (for Python API integration)
- **Environment**: Ubuntu 20.04 LTS
- **Testing Tools**: Python Interpreter, GCC Compiler

## Demonstrated Competencies
- Set Creation and Operations
- Dictionary Manipulation
- Functional Programming Techniques
- Lambda Functions
- Map, Filter, and Reduce Patterns
- Matrix Operations
- Memory Efficiency Optimization
- Python/C API Integration
- Key-Value Data Management
- Data Transformation Patterns
- Roman Numeral Conversion

## System Context
This component builds upon Python's basic data structures knowledge to introduce more advanced collection types and functional programming concepts. Sets and dictionaries provide powerful tools for data manipulation, while functional programming techniques like lambda, map, and filter enable concise and efficient code. These concepts are fundamental for developing robust Python applications with optimal data handling.

## Development Requirements
- Python 3.8.5+
- GCC Compiler (for C extension)
- pycodestyle 2.8.* (PEP8)
- Text Editor or IDE

## Development Workflow
1. Understand the specific data structure operation required
2. Choose the appropriate data structure (set or dictionary)
3. Implement using standard methods or functional programming techniques
4. Test with various inputs including edge cases
5. For C-based functions, implement the Python/C API integration
6. Validate code against coding standards (PEP8)

## Maintenance Notes
- All Python files begin with the shebang line `#!/usr/bin/python3`
- Python code follows PEP8 style guidelines
- C code follows Betty style guidelines
- Function documentation clearly explains purpose and return values
- Memory management in C functions is properly handled
- Functional programming techniques used where appropriate

## Implementation Specifics

### Matrix Operations
- **Square Matrix Calculation**: [0-square_matrix_simple.py](./0-square_matrix_simple.py) - Compute square value of all integers in a matrix
- **Lambda Matrix Operation**: [101-square_matrix_map.py](./101-square_matrix_map.py) - Square matrix using map and lambda

### Set Operations
- **Unique Addition**: [2-uniq_add.py](./2-uniq_add.py) - Add all unique integers in a list
- **Common Elements**: [3-common_elements.py](./3-common_elements.py) - Return common elements between two sets
- **Different Elements**: [4-only_diff_elements.py](./4-only_diff_elements.py) - Return elements present in only one set

### Dictionary Operations
- **Key Counting**: [5-number_keys.py](./5-number_keys.py) - Return number of keys in a dictionary
- **Dictionary Printing**: [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py) - Print dictionary by ordered keys
- **Dictionary Updates**: [7-update_dictionary.py](./7-update_dictionary.py) - Replace or add key/value in a dictionary
- **Key Deletion**: [8-simple_delete.py](./8-simple_delete.py) - Delete a key in a dictionary
- **Value Multiplication**: [9-multiply_by_2.py](./9-multiply_by_2.py) - Multiply all values in a dictionary by 2
- **Best Score Finder**: [10-best_score.py](./10-best_score.py) - Return key with the biggest integer value
- **Complex Deletion**: [102-complex_delete.py](./102-complex_delete.py) - Delete keys with a specific value

### Functional Programming
- **Element Replacement**: [1-search_replace.py](./1-search_replace.py) - Replace all occurrences of an element in a list
- **Weighted Average**: [100-weight_average.py](./100-weight_average.py) - Return weighted average of integers tuple
- **List Multiplication**: [11-multiply_list_map.py](./11-multiply_list_map.py) - Multiply list values using map

### Special Applications
- **Roman Numeral Conversion**: [12-roman_to_int.py](./12-roman_to_int.py) - Convert Roman numeral to integer

### C/Python Integration
- **Python Object Info**: [103-python.c](./103-python.c) - C functions that print Python objects info

## Data Structure Characteristics

### Sets
- **Uniqueness**: Sets store unique elements only
- **Operations**: Union, intersection, difference, symmetric difference
- **Performance**: O(1) average case for add, remove, and lookup
- **Use Cases**: Removing duplicates, membership testing, mathematical set operations

### Dictionaries
- **Structure**: Key-value pairs with unique keys
- **Operations**: Insertion, deletion, updating, lookup by key
- **Performance**: O(1) average case for common operations
- **Use Cases**: Fast lookups, counting occurrences, storing related data

### Functional Programming Concepts
- **Lambda Functions**: Anonymous functions for short operations
- **Map**: Apply function to each item in a sequence
- **Filter**: Extract elements from a sequence that satisfy a condition
- **Reduce**: Apply function cumulatively to sequence items

## Testing Approach
- Each function tested with various inputs including edge cases
- C functions tested with Python API integration tests
- Performance considerations evaluated for large datasets
- Functional correctness verified against expected outputs

## Error Handling
- Edge cases considered (empty collections, non-existent keys)
- Type checking where necessary
- Graceful handling of invalid inputs
- C functions properly check Python object types