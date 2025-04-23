# phishing_link_detector.py

print("=== Phishing Link Detector ===")

url = input("Enter a URL to check: ")

# Suspicious patterns to check for
suspicious_keywords = ["login", "verify", "update", "security", "account", "free", "urgent"]
suspicious_extensions = [".zip", ".exe", ".scr", ".rar"]
suspicious_chars = ["@", "-", "_", "%", "&", "=", "+"]

score = 0

# Check for HTTP (not secure)
if url.startswith("http://"):
    score += 1
    print("Warning: URL uses insecure 'http'.")

# Check for long URLs
if len(url) > 75:
    score += 1
    print("Warning: URL is unusually long.")

# Check for @ symbol (used in redirection tricks)
if "@" in url:
    score += 1
    print("Warning: URL contains '@' symbol.")

# Check for suspicious keywords
for word in suspicious_keywords:
    if word in url.lower():
        score += 1
        print(f"Warning: URL contains suspicious keyword: {word}")

# Check for file extensions
for ext in suspicious_extensions:
    if url.lower().endswith(ext):
        score += 1
        print(f"Warning: URL ends with suspicious extension: {ext}")

# Final evaluation
print("\n=== Result ===")
if score >= 3:
    print("This link is likely PHISHING. Avoid clicking it!")
elif score == 1 or score == 2:
    print("This link is SUSPICIOUS. Be careful.")
else:
    print("This link looks SAFE. But always verify manually.")