# Project Manifest: JavaScript Web Scraping

## Project Identity
- **Name**: JavaScript - Web Scraping
- **Type**: Educational
- **Scope**: API Interaction and Web Scraping with Node.js
- **Status**: Completed

## Technology Signature
- **Core**: JavaScript (Node.js)
- **Runtime**: Node.js 10.14.x
- **Libraries**: request, fs
- **Style Guide**: Standard JavaScript (semistandard)
- **Environment**: Ubuntu 20.04 LTS
- **APIs**: Star Wars API, JSONPlaceholder

## Demonstrated Competencies
- File System Operations in Node.js
- HTTP Request Construction and Sending
- JSON Data Parsing and Manipulation
- Asynchronous Programming with Callbacks
- Command-line Argument Processing
- API Response Handling
- Error Management Strategies
- Response Status Code Analysis
- Data Filtering and Transformation
- Sequential Asynchronous Operations
- Web Content Storage
- Resource Aggregation
- RESTful API Integration
- Cross-Origin Resource Management
- Data Structure Manipulation

## System Context
This module builds upon the JavaScript fundamentals and object-oriented concepts from previous modules, focusing on practical web data extraction and API interaction. It demonstrates how JavaScript can be used for automation tasks that involve retrieving data from external sources, processing it, and storing results. These skills are essential for backend development, data collection, and automated testing scenarios, forming the foundation for more advanced web development topics covered in subsequent modules.

## Architecture
- **Command-line Interface**: Scripts executed with arguments via Node.js
- **HTTP Client**: Request module for simplified API calls
- **File System Module**: Node.js fs for reading/writing operations
- **JSON Processing**: Parsing and manipulation of structured data
- **Callback Pattern**: Asynchronous execution flow management
- **Error Handling**: Conditional branching for fault tolerance

## Development Requirements
- Node.js 10.14.x
- Ubuntu 20.04 LTS
- Install request: `npm install request`
- semistandard coding style (Standard JavaScript with semicolons)
- Executable files with proper shebang (#!/usr/bin/node)
- No use of var (const/let only)

## Development Workflow
1. Define required modules and command-line arguments
2. Implement file operations or HTTP requests
3. Process response or file content
4. Extract and transform relevant data
5. Output results or write to destination
6. Implement proper error handling
7. Test with various inputs and edge cases

## Maintenance Notes
- All files include proper shebang (#!/usr/bin/node)
- Error handling is implemented for file operations
- HTTP requests include appropriate error checking
- Command-line arguments are validated where necessary
- Callback functions follow error-first pattern
- Variable naming is clear and consistent
- API endpoints may require updating if services change

## Implementation Specifics

### File System Operations
- **Read File**: [0-readme.js](./0-readme.js) - Read and print file content
- **Write File**: [1-writeme.js](./1-writeme.js) - Write string to file

### HTTP Request Basics
- **Status Code**: [2-statuscode.js](./2-statuscode.js) - Print response status code
- **GET Request**: [3-starwars_title.js](./3-starwars_title.js) - Retrieve and display movie title

### Data Processing
- **Data Filtering**: [4-starwars_count.js](./4-starwars_count.js) - Count films with specific character
- **Resource Storage**: [5-request_store.js](./5-request_store.js) - Download and save web content
- **Data Aggregation**: [6-completed_tasks.js](./6-completed_tasks.js) - Count completed tasks by user

### Advanced API Interaction
- **Resource Listing**: [100-starwars_characters.js](./100-starwars_characters.js) - List all characters in film
- **Sequential Requests**: [101-starwars_characters.js](./101-starwars_characters.js) - List characters in order

## Learning Path Integration
- **Builds On**: JavaScript Objects, Scopes, and Closures (0x13)
- **Leads To**: JavaScript Web jQuery (0x15)
- **Related To**: Python Network #0 and #1 (0x10, 0x11)

## Assessment Criteria
- Correct implementation of file system operations
- Proper handling of HTTP requests and responses
- Effective JSON data processing and transformation
- Appropriate error handling for all operations
- Correct command-line argument processing
- Adherence to JavaScript style guide (semistandard)
- Logical organization of asynchronous code
- Expected output for all test cases