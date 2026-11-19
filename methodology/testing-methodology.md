# CyberShield – Testing Methodology

## 1. Project Overview
CyberShield is a beginner-level web application security assessment lab created using Kali Linux and OWASP Juice Shop. The purpose is to understand common web security weaknesses through controlled, hands-on testing.

## 2. Testing Environment
- Operating System: Kali Linux
- Target Application: OWASP Juice Shop
- Deployment: Docker
- Target URL: http://127.0.0.1:3000
- Reconnaissance Tool: Nmap
- Web Testing Tool: Burp Suite Community Edition
- Programming Language: Python

## 3. Scope and Authorization
All testing was performed against an intentionally vulnerable OWASP Juice Shop instance running locally.

The target was restricted to the local loopback address (127.0.0.1). No external websites, production systems, or third-party services were tested.

## 4. Assessment Process

### Phase 1: Lab Setup
- Installed and configured Docker in Kali Linux.
- Deployed OWASP Juice Shop as a local container.
- Restricted the application port to the loopback interface.

### Phase 2: Reconnaissance
- Used Nmap to inspect the local application's port.
- Reviewed the HTTP response and security-related headers.
- Recorded the initial reconnaissance output.

### Phase 3: Manual Web Application Testing
- Configured Burp Suite Community Edition.
- Captured and inspected HTTP requests and responses.
- Tested basket access using modified request parameters.
- Observed error handling by requesting an invalid application route.

### Phase 4: Security Header Analysis
- Developed a Python script using the urllib library.
- Checked for five commonly recommended HTTP security headers.
- Recorded which headers were present and missing.

### Phase 5: Documentation
- Documented the two reproduced Juice Shop challenges.
- Recorded observations, potential impacts, and remediation recommendations.
- Saved scan output and project documentation.

## 5. Findings Summary

| Finding | Observation |
|---|---|
| Broken Access Control | Access to another user's basket was demonstrated in the lab. |
| Verbose Error Handling | An invalid route returned a detailed server error and internal stack trace. |
| HTTP Security Headers | The Python checker identified three missing headers out of five checked. |

## 6. Limitations
- Testing was limited to a deliberately vulnerable local application.
- Findings are specific to the lab environment.
- The Python script performs basic HTTP header checks; it is not a comprehensive vulnerability scanner.
- No production environment or external target was assessed.

## 7. Conclusion
This assessment provided practical experience with local lab deployment, network reconnaissance, HTTP request analysis, basic access-control testing, error handling analysis, and Python-based security header checking.
