# Python - Network #1

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8.5-blue.svg" alt="Python 3.8.5">
  <img src="https://img.shields.io/badge/urllib-Package-green.svg" alt="urllib Package">
  <img src="https://img.shields.io/badge/requests-Library-red.svg" alt="Requests Library">
  <img src="https://img.shields.io/badge/API-Integration-yellow.svg" alt="API Integration">
</p>

## Project Overview

This project explores making HTTP requests in Python using both the standard `urllib` package and the popular third-party `requests` library. It covers the full spectrum of web interactions: fetching resources, handling responses, working with headers, sending data through different HTTP methods, processing JSON payloads, and implementing proper error handling mechanisms.

## Learning Objectives

By the end of this project, you should be able to explain:

* How to fetch internet resources using Python's `urllib` package
* How to decode and process urllib body responses
* How to make HTTP requests (GET, POST, PUT, DELETE) using the `requests` package
* How to fetch and manipulate JSON resources from external services
* How to manipulate data from external services
* How to handle query parameters in URLs
* How to implement proper HTTP error and exception handling
* How to authenticate with web services including GitHub's API

## Requirements

* Ubuntu 20.04 LTS with Python 3.8.5
* Code style must comply with pycodestyle (version 2.8.*)
* All files must be executable and start with `#!/usr/bin/python3`
* All modules, classes, and functions must have documentation
* Code should handle edge cases appropriately

## Project Tasks

### Urllib Implementation

The first part of the project uses Python's built-in `urllib` package:

### 0. What's my status?
**[0-hbtn_status.py](./0-hbtn_status.py)**

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the urllib package and displays the response details.

```python
#!/usr/bin/python3
"""Script that fetches a URL using urllib"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
```

### 1. Response header value
**[1-hbtn_header.py](./1-hbtn_header.py)**

Write a Python script that takes in a URL, sends a request using urllib, and displays the value of the X-Request-Id header.

### 2. POST an email
**[2-post_email.py](./2-post_email.py)**

Write a Python script that takes in a URL and an email, sends a POST request with the email as a parameter, and displays the body of the response.

### 3. Error code
**[3-error_code.py](./3-error_code.py)**

Write a Python script that takes in a URL, sends a request using urllib, and displays the body of the response, handling HTTP errors appropriately.

### Requests Library Implementation

The second part reimplements similar functionality using the more modern `requests` library:

### 4. What's my status? #1
**[4-hbtn_status.py](./4-hbtn_status.py)**

Write a Python script that fetches https://alx-intranet.hbtn.io/status using the requests package.

```python
#!/usr/bin/python3
"""Script that fetches a URL using requests"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
```

### 5. Response header value #1
**[5-hbtn_header.py](./5-hbtn_header.py)**

Write a Python script that takes in a URL, sends a request using requests, and displays the value of the X-Request-Id header.

### 6. POST an email #1
**[6-post_email.py](./6-post_email.py)**

Write a Python script that takes in a URL and an email, sends a POST request with the email as a parameter, and displays the body of the response using requests.

### 7. Error code #1
**[7-error_code.py](./7-error_code.py)**

Write a Python script that takes in a URL, sends a request using requests, and displays the body of the response, handling HTTP errors appropriately.

### 8. Search API
**[8-json_api.py](./8-json_api.py)**

Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

### API Integration

The final part demonstrates real-world API integration:

### 10. My GitHub!
**[10-my_github.py](./10-my_github.py)**

Write a Python script that takes GitHub credentials and uses the GitHub API to display your user ID.

### 11. Time for an interview!
**[100-github_commits.py](./100-github_commits.py)**

Write a Python script that lists the 10 most recent commits on a specific repository.

## Python HTTP Client Comparison

### urllib vs requests

| Feature | urllib | requests |
|---------|--------|----------|
| Syntax Complexity | More verbose and complex | Clean and intuitive |
| HTTP Methods | Requires different handlers | Simple method functions |
| Headers | Manual dictionary creation | Simple dictionary passing |
| JSON Handling | Requires manual decoding | Built-in .json() method |
| Error Handling | Uses try/except with HTTPError | Response.raise_for_status() |
| Authentication | Complex implementation | Simple auth parameter |
| Session Management | Manual cookie handling | Session objects |
| Development Status | Standard library, stable | External, actively maintained |

## Working with APIs in Python

### API Concepts

1. **Authentication Methods**:
   - **Basic Auth**: Username/password encoded in Base64
   - **API Keys**: Token passed in headers or query parameters
   - **OAuth**: Token-based authorization protocol
   - **JWT**: JSON Web Tokens for secure claims transmission

2. **Common HTTP Methods for APIs**:
   - **GET**: Retrieve data
   - **POST**: Create new resources
   - **PUT**: Update existing resources
   - **DELETE**: Remove resources
   - **PATCH**: Partially update resources

3. **Working with JSON**:
```python
# Parsing JSON responses
import json
import requests

response = requests.get("https://api.example.com/data")
data = response.json()  # Automatically parses JSON

# Creating JSON payloads
payload = {"name": "John", "age": 30}
response = requests.post("https://api.example.com/users", json=payload)
```

4. **Error Handling Best Practices**:
```python
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raises exception for 4XX/5XX responses
    data = response.json()
except HTTPError as e:
    print(f"HTTP Error: {e}")
except ConnectionError:
    print("Connection Error: Failed to connect to the server")
except Timeout:
    print("Timeout Error: Request timed out")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Environment Setup

```bash
# Install requests library if not already installed
pip3 install requests

# Ensure files are executable
chmod +x *.py
```

## Usage Examples

```bash
# Fetch status of a website
./0-hbtn_status.py

# Get a specific header from a URL
./1-hbtn_header.py https://alx-intranet.hbtn.io/status

# Send POST request with email parameter
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

# Handle HTTP errors
./3-error_code.py http://0.0.0.0:5000/status_401

# Access GitHub API with authentication
./10-my_github.py your_username your_personal_access_token
```

## Resources

* [urllib — URL handling modules](https://docs.python.org/3/library/urllib.html)
* [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
* [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* [GitHub REST API Documentation](https://docs.github.com/en/rest)
* [JSON Encoder and Decoder in Python](https://docs.python.org/3/library/json.html)
* [Python Requests Documentation](https://requests.readthedocs.io/en/master/)
* [HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

---

*Project by ALX Higher Level Programming*
