# Python - Network #0

<p align="center">
  <img src="https://img.shields.io/badge/HTTP-Protocol-blue.svg" alt="HTTP Protocol">
  <img src="https://img.shields.io/badge/Curl-Command-red.svg" alt="Curl Command">
  <img src="https://img.shields.io/badge/Bash-Scripting-green.svg" alt="Bash Scripting">
  <img src="https://img.shields.io/badge/Web-APIs-yellow.svg" alt="Web APIs">
</p>

## Project Overview

This project introduces fundamental concepts of HTTP protocols, web APIs, and command-line networking tools. It focuses on using `curl` to make various types of HTTP requests and understand the structure of HTTP communications through Bash scripting with practical implementations.

## Learning Objectives

By the end of this project, you should be able to explain:

* What a URL is and its components
* What HTTP is and how it works as a request-response protocol
* How to read and interpret a URL (scheme, domain, path, query parameters)
* What a domain name is and subdomains
* What an HTTP request and response consist of
* HTTP headers and their role
* HTTP message body
* HTTP request methods (GET, POST, PUT, DELETE)
* HTTP response status codes
* HTTP Cookies and their purpose
* How to make requests with cURL
* Application/JSON content type
* Base64 encoding

## Requirements

* Ubuntu 20.04 LTS
* Bash scripts must pass Shellcheck (version 0.7.0 via apt-get)
* The first line of all Bash scripts should be `#!/bin/bash`
* All files must be executable
* All curl commands must have the `-s` (silent) option
* Python code must follow pycodestyle (version 2.8.*)

## Project Tasks

### 0. cURL body size
**[0-body_size.sh](0-body_size.sh)**

Write a Bash script that takes a URL, sends a request, and displays the size of the response body in bytes.

```bash
#!/bin/bash
# Script that displays the size of the body of a response
curl -s "$1" | wc -c
```

### 1. cURL to the end
**[1-body.sh](1-body.sh)**

Write a Bash script that takes a URL, sends a GET request, and displays the body of the response for a 200 status code.

### 2. cURL Method
**[2-delete.sh](2-delete.sh)**

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.

### 3. cURL only methods
**[3-methods.sh](3-methods.sh)**

Write a Bash script that takes a URL and displays all HTTP methods the server will accept.

### 4. cURL headers
**[4-header.sh](4-header.sh)**

Write a Bash script that takes a URL as an argument, sends a GET request with a specific header, and displays the body of the response.

### 5. cURL POST parameters
**[5-post_params.sh](5-post_params.sh)**

Write a Bash script that takes a URL, sends a POST request with specific parameters, and displays the body of the response.

### 6. Find a peak
**[6-peak.py](6-peak.py)**, **[6-peak.txt](6-peak.txt)**

Write a function that finds a peak in a list of unsorted integers with the lowest complexity.

### 7. Only status code
**[100-status_code.sh](100-status_code.sh)**

Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

### 8. cURL a JSON file
**[101-post_json.sh](101-post_json.sh)**

Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

### 9. Catch me if you can!
**[102-catch_me.sh](102-catch_me.sh)**

Write a Bash script that makes a request that causes the server to respond with a message in the body containing "You got me!".

## HTTP Concepts Guide

### URLs and Their Structure

A URL (Uniform Resource Locator) has the following structure:

```
scheme://domain:port/path?query_string#fragment_id
```

- **Scheme**: Protocol (http, https, ftp)
- **Domain**: Server name or IP address
- **Port**: Optional port number (default: 80 for HTTP, 443 for HTTPS)
- **Path**: Path to the resource
- **Query String**: Optional parameters
- **Fragment ID**: Optional anchor

### HTTP Methods

| Method | Description |
|--------|-------------|
| GET    | Retrieve data from the server |
| POST   | Submit data to be processed |
| PUT    | Update existing resource |
| DELETE | Remove a resource |
| HEAD   | Same as GET but returns headers only |
| OPTIONS| Returns supported methods for a URL |
| PATCH  | Partially update a resource |

### Common HTTP Status Codes

| Code | Category | Description |
|------|----------|-------------|
| 200  | Success  | OK - Request successful |
| 201  | Success  | Created - Resource created |
| 301  | Redirection | Moved Permanently |
| 304  | Redirection | Not Modified (cached) |
| 400  | Client Error | Bad Request |
| 401  | Client Error | Unauthorized |
| 403  | Client Error | Forbidden |
| 404  | Client Error | Not Found |
| 405  | Client Error | Method Not Allowed |
| 500  | Server Error | Internal Server Error |
| 503  | Server Error | Service Unavailable |

### cURL Command Basics

cURL is a command-line tool for transferring data with URLs. Here are some common options:

- `-X, --request`: Specify request method (GET, POST, etc.)
- `-H, --header`: Add header to the request
- `-d, --data`: Send data in the request body
- `-F, --form`: Submit form data
- `-I, --head`: Fetch headers only
- `-L, --location`: Follow redirects
- `-s, --silent`: Silent mode (don't show progress)
- `-o, --output`: Write output to a file
- `-v, --verbose`: Verbose output

### Example cURL Commands

#### Basic GET Request:
```bash
curl -s https://example.com
```

#### GET Request with Headers:
```bash
curl -s -H "User-Agent: MyApp/1.0" https://example.com
```

#### POST Request with Form Data:
```bash
curl -s -X POST -d "name=John&age=25" https://example.com
```

#### POST JSON Data:
```bash
curl -s -X POST -H "Content-Type: application/json" -d '{"name":"John","age":25}' https://example.com
```

#### Save Response to File:
```bash
curl -s -o response.txt https://example.com
```

### HTTP Headers Explained

HTTP headers provide additional information about the request or response:

**Common Request Headers:**
- `User-Agent`: Client application info
- `Host`: Domain name of the server
- `Accept`: Media types the client can process
- `Content-Type`: Media type of the request body
- `Authorization`: Authentication credentials
- `Cookie`: Stored cookies

**Common Response Headers:**
- `Server`: Information about the server
- `Content-Type`: Media type of the response
- `Content-Length`: Size of the response body
- `Set-Cookie`: Send cookies to the client
- `Cache-Control`: Caching directives

## Find a Peak Algorithm

The "Find a Peak" problem asks for any peak element in an array. A peak element is one that is greater than or equal to its neighbors.

### Solution Approach

A naive approach would be to scan the entire array, but we can use a binary search approach to achieve O(log n) complexity:

```python
def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    
    return binary_peak_find(list_of_integers, 0, len(list_of_integers) - 1)

def binary_peak_find(arr, start, end):
    """Use binary search to find peak."""
    if start == end:
        return arr[start]
    
    mid = (start + end) // 2
    
    # If mid element is greater than its next element
    # and greater than its previous element, it is a peak
    if ((mid == 0 or arr[mid] >= arr[mid - 1]) and
        (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])):
        return arr[mid]
    
    # If mid element is less than its left element,
    # then the left half must contain a peak
    elif mid > 0 and arr[mid - 1] > arr[mid]:
        return binary_peak_find(arr, start, mid - 1)
    
    # Otherwise, the right half must contain a peak
    else:
        return binary_peak_find(arr, mid + 1, end)
```

## Resources

* [HTTP (HyperText Transfer Protocol)](https://www.tutorialspoint.com/http/index.htm)
* [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
* [Curl Documentation](https://curl.haxx.se/docs/)
* [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
* [URL Anatomy](https://doepud.co.uk/blog/anatomy-of-a-url)

---

*Project by ALX Higher Level Programming*
