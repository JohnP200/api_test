# API Endpoint Tester

A simple and effective Python tool to test multiple API endpoints and inspect their HTTP response status codes. Designed for developers and security leaners to quickly evaluate the availability and behavior API routes.

## Features

- Reads endpoints from a `.txt` file (one URL per line)
- Sends `GET` requests to each endpoint 
- Displays response codes (e.g., `200 OK`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`)
- Simplem, lightweight, and beginner-friendly
- Easily extendable to include headers or other requets methods 

## Requirements
- Python3
- requests

---

## Usage

### 1. Install Required Library
```bash 
pip install requests

## Example
[+] https://jasonplaceholder.typicode.com/posts is accessible (Status Code: 200)
[-] https://jasonplaceholder.typicode.com/invalid-endpoint not found (Status Code: 404)

## Disclaimer
This project is intended for educational purposes only. Do not use this to scan or test API that you do not own or have explicit permission to access. The author is not responsible for any misuse or damage casued by this script. Always follow legal and ethical guidelines when testing endpoints

## License
MIT License