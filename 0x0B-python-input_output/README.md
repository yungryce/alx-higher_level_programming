# Python Input/Output

This project explores file handling operations in Python, including reading from and writing to files, working with JSON for data serialization, and implementing object persistence.

## Learning Objectives

By the end of this project, you should be able to:

- Open, read, and write text files in Python
- Understand various file access modes (`r`, `w`, `a`, `r+`, etc.)
- Use context managers (`with` statement) for file operations
- Convert Python data structures to JSON strings
- Parse JSON strings into Python objects
- Implement object serialization and deserialization
- Save and load objects to/from files
- Handle file exceptions appropriately
- Create utility scripts for file manipulation

## File I/O in Python

### Basic File Operations

Python provides built-in functions for file operations:

#### Opening Files

```python
# Basic file opening
file = open('filename.txt', 'r')  # Open for reading (default)
file = open('filename.txt', 'w')  # Open for writing (creates new file or truncates existing)
file = open('filename.txt', 'a')  # Open for appending
file = open('filename.txt', 'r+')  # Open for reading and writing

# Always close files when done
file.close()

# Better approach using context manager (automatically closes file)
with open('filename.txt', 'r') as file:
    # Operations on file
    content = file.read()
```

#### Reading Files

```python
# Read entire file content
with open('filename.txt', 'r') as file:
    content = file.read()  # Reads all content as a single string

# Read line by line
with open('filename.txt', 'r') as file:
    for line in file:  # Memory-efficient for large files
        print(line, end='')

# Read specific number of characters
with open('filename.txt', 'r') as file:
    chunk = file.read(100)  # Read first 100 characters

# Read all lines into a list
with open('filename.txt', 'r') as file:
    lines = file.readlines()  # Returns list of lines with newline characters
```

#### Writing to Files

```python
# Write string to file (overwrites existing content)
with open('filename.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("Another line.\n")

# Append to file
with open('filename.txt', 'a') as file:
    file.write("This gets added to the end.\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('filename.txt', 'w') as file:
    file.writelines(lines)  # No newlines added automatically
```

### JSON Operations

JSON (JavaScript Object Notation) is a lightweight data interchange format that's easy for humans to read and write and easy for machines to parse and generate.

#### Serializing Python Objects to JSON

```python
import json

# Convert Python object to JSON string
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": ["Python", "JavaScript", "Go"],
    "active": True
}

# Convert to JSON string
json_string = json.dumps(data)
print(json_string)

# With formatting for better readability
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(pretty_json)

# Write directly to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
```

#### Deserializing JSON to Python Objects

```python
import json

# Parse JSON string to Python object
json_string = '{"name": "John", "age": 30, "city": "New York"}'
parsed_data = json.loads(json_string)
print(parsed_data["name"])  # Access like a dictionary

# Read JSON from file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

### Object Serialization

For classes and custom objects, you can implement methods to convert them to dictionary representations suitable for JSON serialization:

```python
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Return dictionary representation of Student instance"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

# Create and serialize student
student = Student("John", "Doe", 20)
student_json = json.dumps(student.to_json())
print(student_json)

# Save to file
with open('student.json', 'w') as file:
    json.dump(student.to_json(), file)
```

## Project Files

### Basic File Operations
- **[0-read_file.py](./0-read_file.py)**: Function that reads a text file and prints its content
- **[1-write_file.py](./1-write_file.py)**: Function that writes a string to a text file and returns character count
- **[2-append_write.py](./2-append_write.py)**: Function that appends text to a file and returns character count

### JSON Operations
- **[3-to_json_string.py](./3-to_json_string.py)**: Function that returns JSON string representation of an object
- **[4-from_json_string.py](./4-from_json_string.py)**: Function that returns Python object from JSON string
- **[5-save_to_json_file.py](./5-save_to_json_file.py)**: Function to write object to file using JSON representation
- **[6-load_from_json_file.py](./6-load_from_json_file.py)**: Function to create object from JSON file
- **[7-add_item.py](./7-add_item.py)**: Script to add command line arguments to a Python list saved in a file
- **[8-class_to_json.py](./8-class_to_json.py)**: Function that returns dictionary description of object for JSON serialization

### Student Class with JSON Serialization
- **[9-student.py](./9-student.py)**: Simple Student class with JSON serialization
- **[10-student.py](./10-student.py)**: Student class with filtered attribute serialization
- **[11-student.py](./11-student.py)**: Student class with reload from JSON capability

### Advanced Operations
- **[12-pascal_triangle.py](./12-pascal_triangle.py)**: Function that generates Pascal's Triangle
- **[100-append_after.py](./100-append_after.py)**: Function to insert text after lines containing specific string
- **[101-stats.py](./101-stats.py)**: Script for parsing and analyzing log data

## Environment
- Python 3.8.5
- pycodestyle 2.8.0

## Best Practices for File Handling

1. **Always use context managers** (`with` statement) to ensure files are properly closed
2. **Handle exceptions** properly for file operations
3. **Check file existence** before trying to read a file
4. **Use appropriate file modes** for your specific needs
5. **Be careful with large files** - consider reading line by line instead of loading entirely into memory
6. **Use text mode** (`'r'`, `'w'`) for text files and binary mode (`'rb'`, `'wb'`) for binary files
7. **Specify encoding** when dealing with text files to avoid encoding issues
8. **Always validate JSON** data before processing it

## Example Usage

Reading a file and displaying its contents:

```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file.txt")
```

Writing to a file and getting character count:

```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
```

Saving a Python object to a JSON file:

```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)
```

## Further Resources

- [Python Official Documentation - Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python's json module](https://docs.python.org/3/library/json.html)
- [Automate the Boring Stuff with Python - Working with Files](https://automatetheboringstuff.com/2e/chapter9/)
- [Real Python - Working with Files in Python](https://realpython.com/working-with-files-in-python/)
