# JavaScript - Web scraping

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow.svg" alt="JavaScript ES6">
  <img src="https://img.shields.io/badge/Node.js-10.14.x-green.svg" alt="Node.js 10.14.x">
  <img src="https://img.shields.io/badge/API-Integration-blue.svg" alt="API Integration">
  <img src="https://img.shields.io/badge/Web-Scraping-red.svg" alt="Web Scraping">
</p>

## Project Overview

This project explores web data extraction and API interactions using JavaScript in a Node.js environment. It demonstrates how to perform file operations, make HTTP requests, process JSON data, and implement asynchronous programming patterns. The scripts showcase practical applications of JavaScript for automation tasks that involve retrieving, processing, and storing data from web services.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why JavaScript programming is amazing for web scraping
* How to manipulate JSON data effectively
* How to use the `request` module to make HTTP requests
* How to read and write files with the `fs` module
* How to process command-line arguments in Node.js
* How to work with asynchronous operations using callbacks
* How to handle errors properly in asynchronous operations
* How to extract and transform data from API responses
* How to create automation scripts for web data collection
* How to interact with various REST APIs

## Requirements

* Ubuntu 20.04 LTS using Node.js 10.14.x
* All files must be executable and start with `#!/usr/bin/node`
* Code should follow semistandard style (Standard + semicolons)
* Variables must use `const` or `let` (no `var`)
* You must use the `request` module for HTTP requests

## Project Tasks

### File System Operations

### 0. Readme
**[0-readme.js](./0-readme.js)**

Write a script that reads and prints the content of a file.

```javascript
#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
```

### 1. Write me
**[1-writeme.js](./1-writeme.js)**

Write a script that writes a string to a file.

```javascript
#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
```

### HTTP Request Basics

### 2. Status code
**[2-statuscode.js](./2-statuscode.js)**

Write a script that displays the status code of a GET request.

### 3. Star wars movie title
**[3-starwars_title.js](./3-starwars_title.js)**

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

### Data Processing

### 4. Star wars Wedge Antilles
**[4-starwars_count.js](./4-starwars_count.js)**

Write a script that prints the number of movies where the character "Wedge Antilles" is present.

### 5. Loripsum
**[5-request_store.js](./5-request_store.js)**

Write a script that gets the contents of a webpage and stores it in a file.

```javascript
#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
```

### 6. How many completed?
**[6-completed_tasks.js](./6-completed_tasks.js)**

Write a script that computes the number of tasks completed by user id.

### Advanced API Integration

### 7. Who was playing in this movie?
**[100-starwars_characters.js](./100-starwars_characters.js)**

Write a script that prints all characters of a Star Wars movie.

### 8. Right order
**[101-starwars_characters.js](./101-starwars_characters.js)**

Write a script that prints all characters of a Star Wars movie in the same order of the list "characters" in the /films/ response.

## Node.js Web Scraping Guide

### File System Operations with fs

The `fs` module provides an API for interacting with the file system:

```javascript
const fs = require('fs');

// Reading files synchronously
const data = fs.readFileSync('file.txt', 'utf8');

// Reading files asynchronously
fs.readFile('file.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Writing files asynchronously
fs.writeFile('file.txt', 'Hello World!', (err) => {
  if (err) throw err;
  console.log('File saved successfully!');
});

// Streaming data
const readStream = fs.createReadStream('input.txt');
const writeStream = fs.createWriteStream('output.txt');
readStream.pipe(writeStream);
```

### HTTP Requests with request Module

The `request` module simplifies making HTTP requests:

```javascript
const request = require('request');

// Basic GET request
request('https://api.example.com/data', (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  
  console.log('Status Code:', response.statusCode);
  console.log('Body:', body);
});

// POST request with JSON data
request({
  url: 'https://api.example.com/post',
  method: 'POST',
  json: true,
  body: { name: 'John', age: 30 }
}, (error, response, body) => {
  // Handle response
});

// Streaming responses
request('https://example.com/large-file')
  .pipe(fs.createWriteStream('destination.file'));
```

### Working with JSON

JavaScript provides built-in methods for handling JSON:

```javascript
// Parsing JSON string to JavaScript object
const jsonString = '{"name":"John", "age":30}';
const obj = JSON.parse(jsonString);
console.log(obj.name); // John

// Converting JavaScript object to JSON string
const person = { name: 'John', age: 30 };
const json = JSON.stringify(person);
console.log(json); // {"name":"John","age":30}

// Processing JSON from an API
request('https://api.example.com/data', (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    // Process data
  }
});
```

### Handling Asynchronous Operations

JavaScript uses callbacks, promises, and async/await for asynchronous operations:

```javascript
// Callback pattern
function fetchData(callback) {
  request('https://api.example.com', (error, response, body) => {
    callback(error, body);
  });
}

fetchData((error, data) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('Data:', data);
});

// With error handling
request('https://api.example.com', (error, response, body) => {
  if (error) {
    console.error('Error making request:', error);
    return;
  }
  
  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }
  
  try {
    const data = JSON.parse(body);
    console.log('Processed data:', data);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
```

## Environment Setup

```bash
# Install Node.js 10.14.x
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semistandard
sudo npm install semistandard --global

# Install request module
sudo npm install request --global

# Make files executable
chmod +x *.js
```

## Usage Examples

```bash
# Read a file
./0-readme.js cisfun

# Write to a file
./1-writeme.js my_file.txt "Python is cool"

# Get status code of a website
./2-statuscode.js https://alx-intranet.hbtn.io/status

# Get Star Wars movie title
./3-starwars_title.js 1

# Count movies with Wedge Antilles
./4-starwars_count.js https://swapi-api.alx-tools.com/api/films

# Download webpage
./5-request_store.js http://loripsum.net/api loripsum

# Count completed tasks by user
./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos

# List all characters in a Star Wars movie
./100-starwars_characters.js 3
```

## Resources

* [Working with Files in Node.js](https://nodejs.org/api/fs.html)
* [Request - Simplified HTTP client](https://github.com/request/request)
* [JSON Introduction](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [Star Wars API](https://swapi.dev/)
* [Modern Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
* [The Marvel of Web Scraping with Node.js](https://www.freecodecamp.org/news/the-ultimate-guide-to-web-scraping-with-node-js-daa2027dcd3/)
* [Error Handling in Node.js](https://www.joyent.com/node-js/production/design/errors)
* [Stream Handbook](https://github.com/substack/stream-handbook)

---

*Project by ALX Higher Level Programming*

