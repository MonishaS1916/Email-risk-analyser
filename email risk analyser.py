# email risk analyser 
email = input("Enter email content: ").lower()

score = 0

# Suspicious keywords
keywords = [
    "urgent", "password", "bank", "verify", "click here",
    "account suspended", "login", "security alert"
]

for word in keywords:
    if word in email:
        score += 2

# Check links
if "http://" in email or "https://" in email:
    score += 2

# Suspicious domains
bad_domains = [".ru", ".xyz", ".top", ".click", ".info"]

for domain in bad_domains:
    if domain in email:
        score += 2

# Decision making
if score <= 2:
    print("🟢 Safe Email")
elif score <= 5:
    print("🟡 Suspicious Email")
else:
    print("🔴 Dangerous Email (Phishing Risk)")