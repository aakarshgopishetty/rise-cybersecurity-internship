# 🔐 Project 3: Keylogger (Educational Use Only)

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/Use-Educational%20Only-red)

## 📄 Problem Statement

Keyloggers are programs that record user keystrokes. While often used maliciously, understanding how keyloggers work can help cybersecurity professionals build better detection and defense mechanisms.

---

## 🎯 Objective

Create a simple keylogger using Python to demonstrate how keyboard inputs can be logged for educational and ethical awareness purposes only.

---

## 🛠️ Requirements

- Python 3.x
- `pynput` library (Install using: `pip install pynput`)
- File system access to create and write to `log.txt`

---

## ⚙️ How It Works

- Listens to keyboard input using `pynput.keyboard.Listener`.
- Logs every keystroke into a file named `log.txt`.
- Special keys like `Enter`, `Backspace` are represented with tags (`[Key.enter]`, etc.).

---

## 📁 Files

- `keylogger.py` – Main script
- `log.txt` – Log file where keystrokes are recorded

---

## ⚠️ Disclaimer

This keylogger is developed **strictly for educational use only** as part of the Rise Cybersecurity Internship by Tamizhan Skills. Unauthorized or malicious use of keyloggers is **illegal and unethical**.

---

## 📦 Imports Used

```python
    from pynput import keyboard
```

---

## 🔒 Kill Switch Feature

- To safely stop the keylogger: Press the combination Ctrl + Alt + Q.
- This will immediately stop the keylogger and close the listener.

---

## ✅ Output Example

When a user types something like:

`Hello123!` → [Backspace] → [Enter]

The `log.txt` file will contain:

Hello123![Key.backspace][Key.enter]

### Note

- Regular characters are recorded directly.
- Special keys are logged in bracketed format like `[Key.space]`, `[Key.enter]`, `[Key.backspace]`, etc.

---

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
