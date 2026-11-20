# CyberShield – Security Assessment Summary

## 1. Project Overview
CyberShield is a beginner-level web application security assessment
project conducted in an isolated Kali Linux environment.

## 2. Target Application
- Application: OWASP Juice Shop
- Environment: Local Docker container
- Target: http://127.0.0.1:3000
- Testing scope: Local environment only

## 3. Tools Used
- Kali Linux
- Docker
- OWASP Juice Shop
- Burp Suite Community Edition
- Nmap
- Python

## 4. Security Testing Performed

### A. Reconnaissance
Performed local port and service discovery using Nmap.
Port 3000 was identified as open.

### B. Broken Access Control (IDOR)
Modified a basket request to access another user's basket.
The application returned another user's basket information.

### C. Error Handling
Tested an invalid application endpoint.
The server returned an HTTP 500 response containing
detailed internal error information.

### D. Security Headers
Developed a Python script to inspect HTTP security headers.

Results:
- X-Content-Type-Options: Present
- X-Frame-Options: Present
- Content-Security-Policy: Missing
- Referrer-Policy: Missing
- Permissions-Policy: Missing

## 5. Recommendations
- Implement server-side authorization checks.
- Prevent users from accessing other users' resources.
- Avoid exposing internal stack traces.
- Configure appropriate HTTP security headers.
- Validate and handle invalid requests safely.

## 6. Limitations
- Testing was restricted to a deliberately vulnerable local application.
- No external systems were tested.
- Recommended fixes were documented but not implemented
  or retested.

## 7. Conclusion
This project provided practical experience in web application
reconnaissance, HTTP traffic inspection, access-control testing,
error-handling analysis, and basic Python-based security checks.
