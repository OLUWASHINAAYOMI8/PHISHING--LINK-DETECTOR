# Phishing Link Detector (CLI)

This is a beginner-friendly Phishing Link Detector written in Python. It helps identify potentially dangerous URLs based on common phishing indicators.

# Features:
- Detects suspicious keywords (e.g., login, verify, update)
- Flags long URLs or those with special redirection symbols (@)
- Warns if insecure HTTP is used
- Checks for risky file extensions (.zip, .exe, etc.)

## How to Use:
1. Clone or download this repository.
2. Run the script in your terminal:
   ```bash
   python phishing_link_detector.py

3. Paste the URL when prompted.



Example Output:

Enter a URL to check: http://verify-your-bank-login.com
Warning: URL uses insecure 'http'.
Warning: URL contains suspicious keyword: login
Warning: URL contains suspicious keyword: verify

This link is likely PHISHING. Avoid clicking it!

Note:

This tool is for educational purposes only. Always verify suspicious links manually or use online tools like VirusTotal.

Author:

Akindele Emmanuel Akinsola (OAS1602)

