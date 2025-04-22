# JavaScript - Warm up

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow.svg" alt="JavaScript ES6">
  <img src="https://img.shields.io/badge/Node.js-10.14.x-green.svg" alt="Node.js 10.14.x">
  <img src="https://img.shields.io/badge/SemiStandard-Style-blue.svg" alt="SemiStandard Style">
  <img src="https://img.shields.io/badge/First--Steps-Web_Development-red.svg" alt="First Steps Web Development">
</p>

## Project Overview

This project serves as an introduction to JavaScript programming in a Node.js environment. It covers fundamental JavaScript concepts through progressively complex scripts, transitioning from Python to JavaScript for web development purposes. Each script demonstrates key language features, from basic syntax to advanced concepts like callbacks and modules.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* The differences between `var`, `const`, and `let`
* All available data types in JavaScript
* How to use `if`, `if...else` statements
* How to use comments
* How to assign values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* What is a function and how to use functions
* What a function that doesn't use a return statement returns
* Scope of variables
* Arithmetic operators and how to use them
* How to manipulate dictionary objects (JavaScript objects)
* How to import files in JavaScript

## Requirements

* Ubuntu 20.04 LTS using Node.js 10.14.x
* All files must be executable and start with `#!/usr/bin/node`
* Code should follow semistandard style (Standard + semicolons)
* Variables must use `const` or `let` (no `var`)
* Files must end with a new line

## Project Tasks

### Basic Concepts

### 0. First constant, first print
**[0-javascript_is_amazing.js](./0-javascript_is_amazing.js)**

Write a script that prints "JavaScript is amazing"

```javascript
#!/usr/bin/node
const myVar = 'JavaScript is amazing';
console.log(myVar);
```

### 1. 3 languages
**[1-multi_languages.js](./1-multi_languages.js)**

Write a script that prints 3 lines about programming languages.

### 2. Arguments
**[2-arguments.js](./2-arguments.js)**

Write a script that prints a message depending on the number of arguments passed.

```javascript
#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
```

### 3. Value of my argument
**[3-value_argument.js](./3-value_argument.js)**

Write a script that prints the first argument passed to it.

### 4. Create a sentence
**[4-concat.js](./4-concat.js)**

Write a script that prints two arguments passed in the format: " is "

### 5. An Integer
**[5-to_integer.js](./5-to_integer.js)**

Write a script that prints "My number: <first argument converted to integer>" if possible.

### 6. Loop to languages
**[6-multi_languages_loop.js](./6-multi_languages_loop.js)**

Write a script that prints 3 lines using an array of strings and a loop.

```javascript
#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
}
```

### 7. I love C
**[7-multi_c.js](./7-multi_c.js)**

Write a script that prints "C is fun" x times, where x is the first argument.

### 8. Square
**[8-square.js](./8-square.js)**

Write a script that prints a square of a specified size.

### 9. Add
**[9-add.js](./9-add.js)**

Write a script that prints the addition of 2 integers.

```javascript
#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
```

### 10. Factorial
**[10-factorial.js](./10-factorial.js)**

Write a script that computes and prints a factorial recursively.

### 11. Second biggest!
**[11-second_biggest.js](./11-second_biggest.js)**

Write a script that searches the second biggest integer in the list of arguments.

### 12. Object
**[12-object.js](./12-object.js)**

Update a script to replace the value 12 with 89.

### 13. Add file
**[13-add.js](./13-add.js)**

Write a function that returns the addition of 2 integers, to be exported and used in another file.

## Advanced Tasks

### 14. Const or not const
**[100-let_me_const.js](./100-let_me_const.js)**

Write a file that modifies the value of myVar to 333.

### 15. Call me Moby
**[101-call_me_moby.js](./101-call_me_moby.js)**

Write a function that executes a callback function x times.

```javascript
#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
```

### 16. Add me maybe
**[102-add_me_maybe.js](./102-add_me_maybe.js)**

Write a function that increments and calls a function.

### 17. Increment object
**[103-object_fct.js](./103-object_fct.js)**

Update a script by adding a new function incr that increments the integer value.

## JavaScript Fundamentals Guide

### Variable Declaration

JavaScript offers three ways to declare variables:

```javascript
// Block-scoped, can be reassigned
let count = 1;
count = 2; // Valid

// Block-scoped, cannot be reassigned
const PI = 3.14;
// PI = 3.15; // Error!

// Function-scoped, can be reassigned (Avoid using var!)
var name = 'John';
```

### Data Types

JavaScript has seven primitive data types:

1. **String**: `const str = 'Hello'`
2. **Number**: `const num = 42`
3. **Boolean**: `const bool = true`
4. **Undefined**: `let undef`
5. **Null**: `const nothing = null`
6. **Symbol**: `const sym = Symbol('description')`
7. **BigInt**: `const bigNum = 12345678901234567890n`

And one complex type:
- **Object**: `const obj = {name: 'John', age: 30}`

### Control Structures

```javascript
// If statement
if (condition) {
  // code
} else if (anotherCondition) {
  // code
} else {
  // code
}

// While loop
while (condition) {
  // code
}

// For loop
for (let i = 0; i < 10; i++) {
  // code
}

// For...of loop (arrays)
for (const item of array) {
  // code
}

// For...in loop (objects)
for (const key in object) {
  // code
}
```

### Functions

JavaScript functions can be defined in multiple ways:

```javascript
// Function declaration
function add(a, b) {
  return a + b;
}

// Function expression
const subtract = function(a, b) {
  return a - b;
};

// Arrow function
const multiply = (a, b) => a * b;

// Function with default parameters
function divide(a, b = 1) {
  return a / b;
}
```

### Objects

Objects are collections of key-value pairs:

```javascript
// Creating an object
const person = {
  name: 'John',
  age: 30,
  greet: function() {
    console.log(`Hello, my name is ${this.name}`);
  },
  // Shorthand method syntax
  sayBye() {
    console.log('Goodbye!');
  }
};

// Accessing properties
console.log(person.name); // Dot notation
console.log(person['age']); // Bracket notation

// Adding new properties
person.job = 'Developer';

// Deleting properties
delete person.age;
```

### Working with Arrays

```javascript
// Creating arrays
const numbers = [1, 2, 3, 4, 5];

// Array methods
numbers.push(6); // Add to end
numbers.pop(); // Remove from end
numbers.unshift(0); // Add to beginning
numbers.shift(); // Remove from beginning

// Iteration methods
numbers.forEach(num => console.log(num));
const doubled = numbers.map(num => num * 2);
const evens = numbers.filter(num => num % 2 === 0);
const sum = numbers.reduce((total, num) => total + num, 0);
```

### Module Exports and Imports

Node.js uses CommonJS module system:

```javascript
// Exporting (add.js)
function add(a, b) {
  return a + b;
}

// Method 1: Export single function
module.exports = add;

// Method 2: Export multiple items
exports.add = add;
exports.subtract = function(a, b) {
  return a - b;
};

// Importing
// Method 1 (single export)
const add = require('./add');
console.log(add(2, 3)); // 5

// Method 2 (multiple exports)
const math = require('./add');
console.log(math.add(2, 3)); // 5
console.log(math.subtract(5, 2)); // 3
```

### Process Object and Command-line Arguments

```javascript
// The process.argv array structure:
// [0]: node executable path
// [1]: script file path
// [2+]: command-line arguments

// Example: node script.js arg1 arg2
console.log(process.argv[0]); // /path/to/node
console.log(process.argv[1]); // /path/to/script.js
console.log(process.argv[2]); // arg1
console.log(process.argv[3]); // arg2

// Getting all user-provided arguments
const args = process.argv.slice(2);
```

## Environment Setup

```bash
# Install Node.js 10.14.x
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semistandard
sudo npm install semistandard --global

# Make files executable
chmod +x *.js
```

## Usage Examples

```bash
# Run a basic script
./0-javascript_is_amazing.js

# Pass command-line arguments
./4-concat.js You are

# Generate a square
./8-square.js 3

# Use a module-exported function
node 13-main.js

# Use callback functions
node 101-main.js
```

## Resources

* [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
* [Variables](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables)
* [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
* [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
* [Control Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
* [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
* [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
* [Node.js Documentation](https://nodejs.org/en/docs/)
* [Modern JavaScript Tutorial](https://javascript.info/)
* [SemiStandard Style Guide](https://github.com/standard/semistandard)

---

*Project by ALX Higher Level Programming*


