# 📧 Email Risk Analyzer

A simple Python-based Email Risk Analyzer that detects potentially malicious or phishing emails using keyword, link, and suspicious domain analysis.

## 🚀 Features

- Detects suspicious phishing keywords.
- Checks for HTTP/HTTPS links.
- Identifies suspicious domain extensions.
- Calculates a risk score.
- Classifies emails into:
  - 🟢 Safe Email
  - 🟡 Suspicious Email
  - 🔴 Dangerous Email (Phishing Risk)

## 🛠️ Technologies Used

- Python 3

## 📂 Project Structure

```
Email-Risk-Analyzer/
│
├── email risk analyser.py
└── README.md
```

## ⚙️ How It Works

### 1. User Input
The user enters the email content.

Example:

```
Urgent! Your bank account has been suspended.
Click here: https://bank.xyz/login
```

### 2. Keyword Analysis

The program searches for suspicious keywords such as:

- urgent
- password
- bank
- verify
- click here
- account suspended
- login
- security alert

Each detected keyword adds **2 points** to the risk score.

### 3. Link Detection

If the email contains:

- http://
- https://

the risk score increases by **2 points**.

### 4. Suspicious Domain Detection

The analyzer checks for risky domains like:

- .ru
- .xyz
- .top
- .click
- .info

Each detected domain adds **2 points**.

### 5. Risk Classification

| Score | Result |
|--------|--------|
| 0 - 2 | 🟢 Safe Email |
| 3 - 5 | 🟡 Suspicious Email |
| 6 or more | 🔴 Dangerous Email (Phishing Risk) |

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/your-username/Email-Risk-Analyzer.git
```

2. Navigate to the project folder

```
cd Email-Risk-Analyzer
```

3. Run the program

```
python "email risk analyser.py"
```

or

```
py "email risk analyser.py"
```

---

## 💻 Example

### Input

```
Urgent!
Your bank account has been suspended.
Click here:
https://secure-bank.xyz/login
Verify your password immediately.
```

### Output

```
🔴 Dangerous Email (Phishing Risk)
```

---

## 📌 Future Enhancements

- GUI using Tkinter
- Machine Learning-based phishing detection
- Email header analysis
- URL reputation checking
- Spam score visualization
- Email attachment scanning
- Real-time phishing detection

---

## 🎯 Purpose

This project demonstrates basic cybersecurity concepts by identifying phishing indicators in email content using simple rule-based analysis. It serves as a beginner-friendly cybersecurity and Python project.

---

## 👩‍💻 Author

**Monisha S**

Bachelor of Engineering – Computer Science and Engineering (Cybersecurity)

RMK College of Engineering and Technology
