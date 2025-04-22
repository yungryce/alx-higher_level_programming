# Project Manifest: Python Test-Driven Development

## Project Identity
- **Name**: Python - Test-Driven Development
- **Type**: Educational
- **Scope**: Test-First Programming Methodology
- **Status**: Completed

## Technology Signature
- **Core**: Python 3.8.5
- **Testing Frameworks**: doctest, unittest
- **Environment**: Ubuntu 20.04 LTS
- **Development Pattern**: Test-Driven Development (TDD)

## Demonstrated Competencies
- Test-First Development Approach
- Documentation Writing with Docstrings
- Test Case Design and Implementation
- Edge Case Identification
- Interactive Test Creation
- Function Validation
- Input Validation
- Exception Handling
- Code-Test Integration
- Matrix Operations Testing
- String Manipulation Testing
- Numerical Operations Testing
- Object Comparison Testing
- Test Automation

## System Context
This component introduces Test-Driven Development (TDD), a critical software development methodology that emphasizes writing tests before implementing functionality. By focusing on testing first, developers can better design interfaces, validate functionality, and ensure code robustness. TDD leads to more maintainable, reliable, and documented code, which is essential for professional software development.

## Development Requirements
- Python 3.8.5+
- pycodestyle 2.8.* (PEP8)
- Text Editor or IDE
- Understanding of Python functions, exceptions, and classes

## Development Workflow
1. Write comprehensive test cases (doctest or unittest)
2. Run tests to verify they fail (Red phase)
3. Implement minimum code to pass tests (Green phase)
4. Refactor code while maintaining passing tests (Refactor phase)
5. Document code with detailed docstrings
6. Validate final implementation against all tests

## Maintenance Notes
- All Python files begin with the shebang line `#!/usr/bin/python3`
- Python code follows PEP8 style guidelines
- Functions have comprehensive docstrings with examples
- Test files (.txt or Python unittest) are organized in the tests/ directory
- Edge cases are covered in tests
- Both doctest and unittest frameworks are utilized

## Implementation Specifics

### Integer Operations
- **Addition Function**: [0-add_integer.py](./0-add_integer.py) & [tests/0-add_integer.txt](./tests/0-add_integer.txt) - Function to add two integers with type validation

### Matrix Operations
- **Matrix Division**: [2-matrix_divided.py](./2-matrix_divided.py) & [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt) - Divide all elements of a matrix by a number
- **Matrix Multiplication**: [100-matrix_mul.py](./100-matrix_mul.py) & [tests/100-matrix_mul.txt](./tests/100-matrix_mul.txt) - Multiply two matrices with validation
- **Lazy Matrix Multiplication**: [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py) & [tests/101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt) - Matrix multiplication using NumPy

### String Operations
- **Name Printing**: [3-say_my_name.py](./3-say_my_name.py) & [tests/3-say_my_name.txt](./tests/3-say_my_name.txt) - Print a formatted name string with validation
- **Text Indentation**: [5-text_indentation.py](./5-text_indentation.py) & [tests/5-text_indentation.txt](./tests/5-text_indentation.txt) - Format text with proper indentation after punctuation

### Geometric Shapes
- **Square Printing**: [4-print_square.py](./4-print_square.py) & [tests/4-print_square.txt](./tests/4-print_square.txt) - Print a square using # characters with validation

### Max Integer Function
- **Max Integer Function**: [6-max_integer.py](./6-max_integer.py) & [tests/6-max_integer_test.py](./tests/6-max_integer_test.py) - Find the maximum integer in a list with unittest

### CPython Integration
- **CPython #3: Python Strings**: [102-python.c](./102-python.c) - C function to print Python string information

## Testing Approaches

### Doctest
- **Format**: Interactive Python shell examples embedded in docstrings
- **Benefits**: Self-documenting, clear expected outputs, easy to read
- **Example**:
  ```python
  def add_integer(a, b=98):
      """
      Adds two integers.
      
      >>> add_integer(1, 2)
      3
      >>> add_integer(100, -2)
      98
      >>> add_integer(2)
      100
      >>> add_integer(100.3, -2)
      98
      """
      # Function implementation
  ```

### Unittest
- **Format**: Python classes inheriting from unittest.TestCase
- **Benefits**: More structured, fixtures, setup/teardown, assertions
- **Example**:
  ```python
  class TestMaxInteger(unittest.TestCase):
      def test_positive_numbers(self):
          self.assertEqual(max_integer([1, 2, 3, 4]), 4)
          
      def test_empty_list(self):
          self.assertIsNone(max_integer([]))
  ```

## Test Case Categories

### Happy Path Tests
- Normal expected inputs
- Typical use cases
- Standard functionality verification

### Edge Case Tests
- Empty inputs
- Boundary values
- Minimum/maximum values
- Zero values

### Error Case Tests
- Invalid types
- Out-of-range values
- Missing required arguments
- Testing raised exceptions

## Documentation Guidelines
- Module-level docstrings explain purpose and usage
- Function docstrings include:
  - Purpose description
  - Parameter explanations
  - Return value descriptions
  - Interactive examples (doctest)
  - Exception specifications
- Test files are organized mirroring implementation files