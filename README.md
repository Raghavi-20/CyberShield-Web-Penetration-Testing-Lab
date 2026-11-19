# 🛡️ CyberShield – Web Application Security Assessment Lab

A beginner-level, hands-on web application security assessment project built using Kali Linux, OWASP Juice Shop, Burp Suite Community Edition, Nmap, and Python.

## 📌 Project Overview

CyberShield is a controlled web application security testing lab designed to explore common web security weaknesses through practical testing.

The project focuses on understanding HTTP communication, identifying access-control issues, analyzing error handling, performing basic reconnaissance, and automating HTTP security-header checks.

All testing was conducted against an intentionally vulnerable OWASP Juice Shop instance deployed locally.

## 🎯 Project Objectives

- Understand basic web application security testing.
- Perform local network reconnaissance.
- Inspect HTTP requests and responses.
- Explore broken access control.
- Identify verbose error disclosure.
- Analyze HTTP security headers.
- Develop a Python-based security-header checker.
- Document findings and defensive recommendations.

## 🧰 Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Kali Linux | Security testing environment |
| OWASP Juice Shop | Intentionally vulnerable target application |
| Docker | Local application deployment |
| Nmap | Port and service reconnaissance |
| Burp Suite Community Edition | HTTP request and response analysis |
| Python | Security-header checking |
| Git and GitHub | Version control and project hosting |

## 🏗️ Lab Environment

**Target Application:** OWASP Juice Shop  
**Target URL:** `http://127.0.0.1:3000`  
**Deployment:** Docker container  
**Network Scope:** Localhost only

The application was bound to the loopback interface to keep the testing environment isolated from external network access.

## 🔍 Assessment Activities

### 1. Reconnaissance
- Performed an Nmap scan against the local application port.
- Identified the HTTP service response.
- Recorded initial reconnaissance results.

### 2. Manual Web Application Testing
- Configured Burp Suite Community Edition.
- Captured and inspected HTTP requests.
- Modified basket identifiers to examine access-control enforcement.
- Requested an invalid application route to examine error handling.

### 3. Python Security Header Checker

Developed a Python script using the `urllib` library to inspect five HTTP security headers.

**Headers checked:**
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

**Observed results:**

| Header | Result |
|---|---|
| Content-Security-Policy | Missing |
| X-Content-Type-Options | Present |
| X-Frame-Options | Present |
| Referrer-Policy | Missing |
| Permissions-Policy | Missing |

**Summary:** 2 headers present and 3 missing.

Missing headers indicate potential hardening improvements; they do not independently prove an exploitable vulnerability.

## 🚨 Documented Security Findings

### Finding 01 – Broken Access Control (IDOR-style basket access)

- Tested basket access by modifying the basket identifier in an HTTP request.
- Observed access to another user's basket in the intentionally vulnerable lab.
- Documented the observation, potential impact, and recommended server-side authorization checks.

**Report:** `vulnerability-reports/IDOR-basket-access.md`

### Finding 02 – Verbose Error Handling

- Requested an invalid application route.
- Observed an HTTP 500 response containing a detailed stack trace and internal application paths.
- Documented the information-disclosure risk and recommended safer error handling.

**Report:** `vulnerability-reports/error-handling.md`

## 🛠️ Remediation Recommendations

The project includes defensive recommendations covering:

- Server-side authorization and resource ownership validation.
- Generic error responses and secure server-side logging.
- Appropriate HTTP security-header configuration.
- General web application security practices.

See: `remediation/remediation-guide.md`

## 📁 Project Structure

```text
CyberShield/
│
├── reconnaissance/
│   ├── nmap-initial.txt
│   └── http-headers.txt
│
├── scans/
│   └── security-headers.txt
│
├── scripts/
│   └── security_headers.py
│
├── vulnerability-reports/
│   ├── IDOR-basket-access.md
│   └── error-handling.md
│
├── methodology/
│   └── testing-methodology.md
│
├── remediation/
│   └── remediation-guide.md
│
├── screenshots/
│
├── .gitignore
└── README.md
```

## ▶️ Running the Python Header Checker

Clone the repository:

```bash
git clone https://github.com/Raghavi-20/CyberShield-Web-Penetration-Testing-Lab.git
```

Navigate into the project:

```bash
cd CyberShield-Web-Penetration-Testing-Lab
```

Run the script:

```bash
python scripts/security_headers.py
```

The local OWASP Juice Shop application must be running at `http://127.0.0.1:3000` for the check to work.

## 📚 Documentation

- [Testing Methodology](methodology/testing-methodology.md)
- [Remediation Guide](remediation/remediation-guide.md)
- [IDOR Basket Access Report](vulnerability-reports/IDOR-basket-access.md)
- [Error Handling Report](vulnerability-reports/error-handling.md)

## ⚠️ Scope and Disclaimer

This project was performed strictly within an isolated local lab using OWASP Juice Shop.

No external websites, production systems, or third-party applications were tested.

The project is intended for educational and defensive cybersecurity learning purposes.

## 👩‍💻 Author

**Raghavi S**  
B.Tech Information Technology Student

GitHub: [Raghavi-20](https://github.com/Raghavi-20)
