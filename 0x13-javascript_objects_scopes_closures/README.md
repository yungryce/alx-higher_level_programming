# JavaScript - Objects, Scopes and Closures

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow.svg" alt="JavaScript ES6">
  <img src="https://img.shields.io/badge/OOP-Classes-blue.svg" alt="OOP Classes">
  <img src="https://img.shields.io/badge/Closures-Scopes-green.svg" alt="Closures & Scopes">
  <img src="https://img.shields.io/badge/Inheritance-Prototype-red.svg" alt="Inheritance & Prototype">
</p>

## Project Overview

This project expands on JavaScript fundamentals by diving into object-oriented programming concepts, scopes, and closures. It builds upon the basics covered in the JavaScript warm-up module to demonstrate class creation, inheritance, method implementation, and functional programming techniques in JavaScript.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What `this` means and when to use it
* What `undefined` means and why variable type and scope matter
* What a closure is and how to use one
* What a prototype is and how to inherit an object from another
* How to create and use classes using ES6 syntax
* How to implement inheritance between classes in JavaScript
* How to manipulate arrays and dictionaries with JavaScript

## Requirements

* Ubuntu 20.04 LTS using Node.js 10.14.x
* All files must be executable and start with `#!/usr/bin/node`
* Code should follow semistandard style (Standard + semicolons)
* Variables must use `const` or `let` (no `var`)
* All files must include proper documentation

## Project Tasks

### Class Definition and Inheritance

### 0. Rectangle #0
**[0-rectangle.js](./0-rectangle.js)**

Write an empty class Rectangle that defines a rectangle.

```javascript
#!/usr/bin/node
class Rectangle {
}

module.exports = Rectangle;
```

### 1. Rectangle #1
**[1-rectangle.js](./1-rectangle.js)**

Write a class Rectangle that defines a rectangle with width and height attributes.

### 2. Rectangle #2
**[2-rectangle.js](./2-rectangle.js)**

Improve the Rectangle class with instance validation: create an empty object if width or height is 0 or negative.

```javascript
#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
```

### 3. Rectangle #3
**[3-rectangle.js](./3-rectangle.js)**

Add a print() method to the Rectangle class that uses the character X to print the rectangle.

### 4. Rectangle #4
**[4-rectangle.js](./4-rectangle.js)**

Add rotate() and double() methods to the Rectangle class.

### 5. Square #0
**[5-square.js](./5-square.js)**

Create a Square class that extends the Rectangle class.

```javascript
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
```

### 6. Square #1
**[6-square.js](./6-square.js)**

Add a charPrint(c) method to the Square class that prints the square with the character c.

### Utility Functions and Closures

### 7. Occurrences
**[7-occurrences.js](./7-occurrences.js)**

Write a function that returns the number of occurrences of an element in a list.

### 8. Esrever
**[8-esrever.js](./8-esrever.js)**

Write a function that returns the reversed version of a list without using the built-in reverse method.

```javascript
#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};
```

### 9. Log me
**[9-logme.js](./9-logme.js)**

Write a function that prints the number of arguments already printed and the new argument value.

### 10. Number conversion
**[10-converter.js](./10-converter.js)**

Write a function that converts a number from base 10 to another base passed as argument.

### Advanced Operations

### 11. Factor index
**[100-map.js](./100-map.js)**

Write a script that imports an array and computes a new array using map.

### 12. Sorted occurrences
**[101-sorted.js](./101-sorted.js)**

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

### 13. Concat files
**[102-concat.js](./102-concat.js)**

Write a script that concatenates two files and stores the result in a third file.

## JavaScript OOP Concepts Guide

### Classes in ES6

ES6 introduced the `class` syntax for defining objects and their behavior:

```javascript
class Person {
  constructor (name, age) {
    this.name = name;
    this.age = age;
  }

  sayHello () {
    console.log(`Hello, my name is ${this.name}`);
  }
}

const john = new Person('John', 30);
john.sayHello(); // Hello, my name is John
```

### Inheritance with extends

The `extends` keyword allows one class to inherit from another:

```javascript
class Student extends Person {
  constructor (name, age, grade) {
    super(name, age); // Call parent constructor
    this.grade = grade;
  }

  study () {
    console.log(`${this.name} is studying`);
  }
}

const alice = new Student('Alice', 20, 'A');
alice.sayHello(); // Inherited from Person
alice.study();    // Defined in Student
```

### Understanding this

The `this` keyword in JavaScript refers to the current execution context:

```javascript
// In a class method, 'this' refers to the instance
class Counter {
  constructor () {
    this.count = 0;
  }
  
  increment () {
    this.count++;
  }
}

// In a regular function, 'this' depends on how the function is called
function showThis () {
  console.log(this);
}

showThis();        // 'this' is the global object (or undefined in strict mode)
const obj = { method: showThis };
obj.method();      // 'this' is the obj object
```

### Closures

A closure is a function that maintains access to its outer scope's variables:

```javascript
function createCounter () {
  let count = 0;  // Private variable
  
  return function () {
    count++;      // Access to count via closure
    return count;
  };
}

const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
```

### Prototypes and Prototype Chain

Every JavaScript object has a prototype from which it inherits properties:

```javascript
// Constructor function (pre-ES6 approach)
function Animal (name) {
  this.name = name;
}

// Adding a method to the prototype
Animal.prototype.makeSound = function () {
  console.log('Some generic sound');
};

// Creating a new object
const cat = new Animal('Fluffy');
cat.makeSound(); // Some generic sound

// Checking prototype chain
console.log(cat.__proto__ === Animal.prototype); // true
```

### Working with Arrays

Common functional programming methods for arrays:

```javascript
const numbers = [1, 2, 3, 4, 5];

// map: transform each element
const doubled = numbers.map(num => num * 2); // [2, 4, 6, 8, 10]

// filter: keep elements that pass a test
const evens = numbers.filter(num => num % 2 === 0); // [2, 4]

// reduce: accumulate values
const sum = numbers.reduce((total, num) => total + num, 0); // 15

// forEach: execute function for each element
numbers.forEach(num => console.log(num));
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
# Create and inspect a Rectangle
node tests/1-main.js

# Test a class that inherits from another
node tests/5-main.js

# Test a closure function
node tests/9-main.js

# Concatenate two files
./102-concat.js fileA fileB fileC
```

## Resources

* [JavaScript Objects Basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)
* [Object-oriented JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
* [Class Inheritance](https://javascript.info/class-inheritance)
* [JavaScript Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [this/self](https://alistapart.com/article/getoutbindingsituations/)
* [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

---

*Project by ALX Higher Level Programming*

