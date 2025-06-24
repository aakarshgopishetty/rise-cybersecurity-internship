# 🛡️ Project 7: SQL Injection Demonstration

![Status](https://img.shields.io/badge/Projects-7%2F8%20Completed-blue)
![Security](https://img.shields.io/badge/SQL--Injection-Vulnerable-red)

## 📌 Problem Statement

Many web applications are vulnerable to **SQL injection attacks** due to **improper input validation** and unsafe coding practices. This project demonstrates how SQL injection works and how to **secure** your application from it.

---

## 🎯 Objective

- Build a simple login form using **Python Flask** and **SQLite**
- Simulate an **SQL Injection vulnerability**
- Show the difference between vulnerable and secure code
- Educate on safe coding practices

---

## ⚙️ Requirements

- Python 3
- Flask
- SQLite3 (built-in with Python)
- Basic HTML

Install Flask using:

```bash
pip install flask
```

## 🚀 How to Run

- Make sure app.py and login.html are in the correct folder structure.
- Run the app:

```bash
python app.py
```

- Open your browser and go to:

``` bash
http://127.0.0.1:5000
```

- Test a normal login:

``` bash

Username: admin
Password: admin123

```

- Test SQL Injection:

``` bash
Username: ' OR '1'='1' --

Password: (anything)

```

- You will be logged in without knowing the real password — a vulnerability!

## 🔐 How to Fix It (secure_app.py)

- Use parameterized queries instead of string formatting:

```python
c.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, pwd))
```

- This ensures user input is treated as data, not executable SQL code.

## 📽️ Demo Video

[Click here to watch the demo](https://www.youtube.com/watch?v=sFdt4u8zoFc)

## ⚠️ Disclaimer

- This project is for educational purposes only.
- Do not use these techniques in real-world applications or against any system without permission.

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
