# Project Manifest: Python if/else, loops, functions

## Project Identity
- **Name**: Python - if/else, loops, functions
- **Type**: Educational
- **Scope**: Python Control Flow Fundamentals
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5
- **Supporting**: C (for linked list manipulation)
- **Environment**: Ubuntu 20.04 LTS
- **Testing Tools**: Python Interpreter

## Demonstrated Competencies
- Conditional Logic with if/else statements
- Loop Construction (for and while)
- Function Definition and Implementation
- ASCII Character Manipulation
- Working with Numeric Ranges
- String Formatting and Manipulation
- Python Code Style and Conventions
- Linked List Operations in C
- Algorithm Development

## System Context
This component builds upon basic Python introductions to establish core programming concepts necessary for any Python developer. Mastery of control flow statements (conditionals and loops) and function definitions are fundamental skills required before advancing to modules, data structures, and more complex Python concepts.

## Development Requirements
- Python 3.8.5+
- gcc compiler (for C programs)
- pycodestyle 2.8.* (PEP8)
- Text Editor or IDE

## Development Workflow
1. Understand the control flow concept (if/else, loops, or functions)
2. Implement the required functionality in Python
3. Test with various inputs to ensure correctness
4. Validate code against PEP8 style guidelines
5. For C tasks, compile with gcc and test with provided main functions

## Maintenance Notes
- All Python files begin with the shebang line `#!/usr/bin/python3`
- All Python files are executable
- Python code follows PEP8 style guidelines
- C code follows Betty style guidelines
- All files contain appropriate documentation

## Implementation Specifics

### Conditional Statements
- **Random Number Assessment**: [0-positive_or_negative.py](./0-positive_or_negative.py) - Determine if a random number is positive, negative, or zero
- **Last Digit Analysis**: [1-last_digit.py](./1-last_digit.py) - Print the last digit of a number and analyze its properties

### Loop Constructs
- **Alphabet Printing**: [2-print_alphabet.py](./2-print_alphabet.py) - Print ASCII lowercase alphabet without a new line
- **Selective Alphabet**: [3-print_alphabt.py](./3-print_alphabt.py) - Print ASCII alphabet excluding 'q' and 'e'
- **Hexadecimal Numbers**: [4-print_hexa.py](./4-print_hexa.py) - Print numbers 0 to 98, in decimal and hexadecimal
- **Number Combinations**: [5-print_comb2.py](./5-print_comb2.py) - Print numbers 0 to 99 with formatting
- **Two-digit Combinations**: [6-print_comb3.py](./6-print_comb3.py) - Print all possible different combinations of two digits

### Function Implementations
- **Lowercase Checking**: [7-islower.py](./7-islower.py) - Function to check for lowercase character
- **String Case Conversion**: [8-uppercase.py](./8-uppercase.py) - Function to print a string in uppercase
- **Last Digit Extraction**: [9-print_last_digit.py](./9-print_last_digit.py) - Function to print the last digit of a number
- **Addition Function**: [10-add.py](./10-add.py) - Function to add two integers
- **Power Function**: [11-pow.py](./11-pow.py) - Function to compute a to the power of b
- **FizzBuzz Implementation**: [12-fizzbuzz.py](./12-fizzbuzz.py) - Function for the classic FizzBuzz problem

### C Programming with Python Integration
- **Linked List Insertion**: [13-insert_number.c](./13-insert_number.c) - C function to insert a number into a sorted singly linked list
- **Header File**: [lists.h](./lists.h) - Header file for the linked list C functions

### Advanced Tasks
- **ASCII Art**: [100-print_tebahpla.py](./100-print_tebahpla.py) - Print the ASCII alphabet in reverse, alternating lowercase and uppercase
- **String Manipulation**: [101-remove_char_at.py](./101-remove_char_at.py) - Function to create a copy of a string, removing a character at a specific position
- **Python Bytecode**: [102-magic_calculation.py](./102-magic_calculation.py) - Python function that matches a given Python bytecode

## Testing Approach
- Each Python script can be run directly to test functionality
- C functions are tested with provided main functions
- Manual testing with various inputs ensures correct behavior
- Automated testing against test cases validates implementation

## Error Handling
- Scripts handle edge cases appropriately
- Input validation where necessary
- Clear error messages for incorrect inputs
- Proper memory management in C functions