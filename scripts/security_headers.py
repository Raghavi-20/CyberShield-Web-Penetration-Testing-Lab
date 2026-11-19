import urllib.request
import urllib.error

URL = "http://127.0.0.1:3000"

security_headers = {
    "Content-Security-Policy": "Helps prevent malicious script injection",
    "X-Content-Type-Options": "Prevents MIME-type sniffing",
    "X-Frame-Options": "Helps prevent clickjacking",
    "Referrer-Policy": "Controls referrer information",
    "Permissions-Policy": "Controls browser feature permissions"
}

print("\n===================================")
print("     CYBERSHIELD SECURITY SCANNER")
print("===================================")
print(f"\nTarget: {URL}\n")

try:
    request = urllib.request.Request(URL, method="GET")
    
    with urllib.request.urlopen(request, timeout=10) as response:
        headers = response.headers

        print(f"HTTP Status: {response.status}\n")
        print("SECURITY HEADER ANALYSIS")
        print("-----------------------------------")

        present = 0
        missing = 0

        for header, description in security_headers.items():
            value = headers.get(header)

            if value:
                print(f"[PRESENT] {header}")
                print(f"          Value: {value}")
                present += 1
            else:
                print(f"[MISSING] {header}")
                print(f"          Purpose: {description}")
                missing += 1

        print("\n===================================")
        print("          SCAN SUMMARY")
        print("===================================")
        print(f"Headers present : {present}")
        print(f"Headers missing: {missing}")
        print("Scan completed successfully.")

except urllib.error.URLError as error:
    print(f"Connection failed: {error}")

except Exception as error:
    print(f"Unexpected error: {error}")
