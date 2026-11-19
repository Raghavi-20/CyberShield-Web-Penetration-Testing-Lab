# CyberShield – Web Application Security Assessment Lab

## Overview
CyberShield is a beginner-level web application security assessment project built using Kali Linux and OWASP Juice Shop.

The project demonstrates practical security testing techniques, HTTP traffic inspection, vulnerability identification, security header analysis, and vulnerability documentation.

All testing was conducted against an intentionally vulnerable application running locally.

## Objectives
- Understand basic web application security testing.
- Perform network and service reconnaissance.
- Inspect HTTP requests and responses.
- Identify access control weaknesses.
- Examine application error handling.
- Automate HTTP security header checks using Python.
- Document findings and recommend remediation.

## Tools and Technologies
- Kali Linux
- Docker
- OWASP Juice Shop
- Nmap
- Burp Suite Community Edition
- Python 3
- Git and GitHub

## Project Structure

```text
CyberShield/
├── reconnaissance/
│   ├── nmap-initial.txt
│   └── http-headers.txt
├── scans/
│   └── security-headers.txt
├── scripts/
│   └── security_headers.py
├── vulnerability-reports/
│   ├── IDOR-basket-access.md
│   └── error-handling.md
├── remediation/
├── screenshots/
├── methodology/
└── README.md
```

## Security Testing Performed

### 1. Network Reconnaissance
Used Nmap to identify the local target service and inspect its HTTP response.

### 2. HTTP Traffic Inspection
Used Burp Suite Community Edition to intercept and inspect HTTP requests and responses.

### 3. IDOR – Broken Access Control
Tested the shopping basket endpoint by changing the basket identifier.

Observed that an authenticated test user could retrieve another user's basket information.

### 4. Improper Error Handling
Requested an invalid endpoint and observed a detailed HTTP 500 error containing internal application paths and stack trace information.

## Python Security Header Checker

Developed a Python script to inspect the target application's HTTP response headers.

The script checks:

- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

### Observed Results

| Header | Result |
|---|---|
| Content-Security-Policy | Missing |
| X-Content-Type-Options | Present |
| X-Frame-Options | Present |
| Referrer-Policy | Missing |
| Permissions-Policy | Missing |

The results indicate missing security-hardening headers. Their absence alone does not establish an exploitable vulnerability.

### Run the Scanner

```bash
python scripts/security_headers.py
```

## Vulnerability Reports

Detailed reports are available in the `vulnerability-reports/` directory:

1. IDOR – Shopping Basket Access
2. Verbose Error Handling

Each report includes the issue description, testing evidence, potential impact, and recommended remediation.

## Lab Environment

- Attacker environment: Kali Linux
- Target application: OWASP Juice Shop
- Deployment: Docker
- Target address: http://127.0.0.1:3000

## Scope and Ethics

This project was performed exclusively against a deliberately vulnerable application hosted in a local lab environment.

No external websites, production systems, or third-party accounts were targeted.

## Future Improvements
- Add additional verified vulnerability assessments.
- Implement automated security checks.
- Add remediation testing and validation.
- Improve Python scanner functionality.
- Include screenshots and testing evidence.

## Author
Raghavi S  
B.Tech Information Technology Student
