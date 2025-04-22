# JavaScript - Web jQuery

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow.svg" alt="JavaScript ES6">
  <img src="https://img.shields.io/badge/jQuery-3.x-blue.svg" alt="jQuery 3.x">
  <img src="https://img.shields.io/badge/DOM-Manipulation-green.svg" alt="DOM Manipulation">
  <img src="https://img.shields.io/badge/AJAX-API-red.svg" alt="AJAX API">
</p>

## Project Overview

This project explores front-end JavaScript development using jQuery, focusing on DOM manipulation, event handling, and AJAX for creating dynamic web pages. It demonstrates the benefits of jQuery's concise syntax over vanilla JavaScript while implementing practical web interactions and external API integrations.

## Learning Objectives

By the end of this project, you should be able to explain:

* Why jQuery is still relevant in modern web development
* How to select HTML elements using both vanilla JavaScript and jQuery
* How to create, modify and manipulate DOM elements with jQuery
* How to implement event handling for user interactions
* How to make AJAX requests to external APIs
* How to process and display JSON data from API responses
* How to update page content dynamically without reload
* How to manipulate CSS properties and classes with jQuery
* How to handle form inputs and implement user-driven functionality
* How to compare vanilla JavaScript and jQuery approaches to the same problems

## Requirements

* All files interpreted on Chrome (version 57.0)
* All files end with a new line
* Code should be semistandard compliant with semicolons
* You must use jQuery version 3.x
* HTML should not reload for each action
* Variables must use `const` or `let` (no `var`)

## Project Tasks

### DOM Manipulation

### 0. No jQuery
**[0-script.js](./0-script.js)**

Write a JavaScript script that updates the text color of the header element to red (#FF0000) using document.querySelector.

```javascript
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
});
```

### 1. With jQuery
**[1-script.js](./1-script.js)**

Write a JavaScript script that updates the text color of the header element to red (#FF0000) using jQuery API.

```javascript
$(document).ready(function () {
  $('header').css('color', '#FF0000');
});
```

### 2. Click and turn red
**[2-script.js](./2-script.js)**

Write a JavaScript script that updates the text color of the header element to red (#FF0000) when the user clicks on the tag DIV#red_header.

### 3. Add `.red` class
**[3-script.js](./3-script.js)**

Write a JavaScript script that adds the class red to the header element when the user clicks on the tag DIV#red_header.

### 4. Toggle classes
**[4-script.js](./4-script.js)**

Write a JavaScript script that toggles the class of the header element when the user clicks on the tag DIV#toggle_header.

### 5. List of elements
**[5-script.js](./5-script.js)**

Write a JavaScript script that adds a LI element to a list when the user clicks on the tag DIV#add_item.

### 6. Change the text
**[6-script.js](./6-script.js)**

Write a JavaScript script that updates the text of the header element to "New Header!!!" when the user clicks on DIV#update_header.

### 7. Star wars character
**[7-script.js](./7-script.js)**

Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json.

```javascript
$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
```

### 8. Star Wars movies
**[8-script.js](./8-script.js)**

Write a JavaScript script that fetches and lists the title for all movies by using https://swapi-api.alx-tools.com/api/films/?format=json.

### 9. Say Hello!
**[9-script.js](./9-script.js)**

Write a JavaScript script that fetches and displays the translation of "Hello" from https://fourtonfish.com/hellosalut/?lang=fr.

### Advanced Tasks

### 10. No jQuery - document loaded
**[100-script.js](./100-script.js)**

Write a JavaScript script that updates the text color of the header element to red (#FF0000) using document.querySelector without any jQuery.

### 11. List, add, remove
**[101-script.js](./101-script.js)**

Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks.

### 12. Say hello to everybody!
**[102-script.js](./102-script.js)**

Write a JavaScript script that fetches and prints the translation of "Hello" according to the language.

### 13. And press ENTER
**[103-script.js](./103-script.js)**

Write a JavaScript script that fetches and prints the translation of "Hello" when the user clicks or presses ENTER.

## jQuery vs Vanilla JavaScript

### Element Selection

| Task | jQuery | Vanilla JavaScript |
|------|--------|-------------------|
| Select by ID | `$('#myId')` | `document.getElementById('myId')` |
| Select by Class | `$('.myClass')` | `document.getElementsByClassName('myClass')` or `document.querySelectorAll('.myClass')` |
| Select by Tag | `$('div')` | `document.getElementsByTagName('div')` or `document.querySelectorAll('div')` |
| Complex Selection | `$('ul.nav > li')` | `document.querySelectorAll('ul.nav > li')` |

### DOM Manipulation

| Task | jQuery | Vanilla JavaScript |
|------|--------|-------------------|
| Change Text | `$('#el').text('New text')` | `document.getElementById('el').textContent = 'New text'` |
| Change HTML | `$('#el').html('<span>New</span>')` | `document.getElementById('el').innerHTML = '<span>New</span>'` |
| Change CSS | `$('#el').css('color', 'red')` | `document.getElementById('el').style.color = 'red'` |
| Add Class | `$('#el').addClass('active')` | `document.getElementById('el').classList.add('active')` |
| Toggle Class | `$('#el').toggleClass('active')` | `document.getElementById('el').classList.toggle('active')` |
| Append Element | `$('#list').append('<li>New item</li>')` | `document.getElementById('list').insertAdjacentHTML('beforeend', '<li>New item</li>')` |

### Event Handling

| Task | jQuery | Vanilla JavaScript |
|------|--------|-------------------|
| Click Event | `$('#btn').click(handler)` | `document.getElementById('btn').addEventListener('click', handler)` |
| Document Ready | `$(document).ready(handler)` | `document.addEventListener('DOMContentLoaded', handler)` |
| Multiple Events | `$('#btn').on('click mouseover', handler)` | Need separate listeners in vanilla JS |

### AJAX Requests

| Task | jQuery | Vanilla JavaScript |
|------|--------|-------------------|
| GET Request | `$.get(url, callback)` | `fetch(url).then(res => res.json()).then(callback)` |
| POST Request | `$.post(url, data, callback)` | `fetch(url, {method: 'POST', body: JSON.stringify(data)}).then(...)` |
| JSON Request | `$.getJSON(url, callback)` | `fetch(url).then(res => res.json()).then(callback)` |

## Implementing Common jQuery Tasks

### Document Ready

```javascript
// jQuery
$(document).ready(function() {
  // Code here runs when DOM is ready
});

// Vanilla JavaScript
document.addEventListener('DOMContentLoaded', function() {
  // Code here runs when DOM is ready
});
```

### Making AJAX Calls

```javascript
// jQuery AJAX
$.ajax({
  url: 'https://api.example.com/data',
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log('Data received:', data);
  },
  error: function(xhr, status, error) {
    console.error('Error:', error);
  }
});

// Fetch API (modern JavaScript)
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log('Data received:', data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## Environment Setup

```html
<!-- Include jQuery in your HTML files -->
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

<!-- Link your JavaScript file -->
<script type="text/javascript" src="your-script-file.js"></script>
```

## Resources

* [jQuery API Documentation](https://api.jquery.com/)
* [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [jQuery Selectors](https://api.jquery.com/category/selectors/)
* [jQuery Events API](https://api.jquery.com/category/events/)
* [jQuery AJAX Documentation](https://api.jquery.com/category/ajax/)
* [JSON Format](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
* [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

---

*Project by ALX Higher Level Programming*
