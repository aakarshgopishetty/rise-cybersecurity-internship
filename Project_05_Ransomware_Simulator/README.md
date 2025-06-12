# 💣 Project 5: Simple Ransomware Simulator (Educational Use Only)

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/Use-Educational%20Only-red)

---

## 📄 Problem Statement

Ransomware is a malicious software that encrypts user data and demands payment to restore it. Understanding its behavior is essential for building effective security defenses.

---

## 🎯 Objective

Simulate the behavior of ransomware in a **safe and controlled environment** by:

- Encrypting all files in a chosen folder.
- Allowing decryption with the correct key.
- Demonstrating the importance of backups and encryption awareness.

---

## 🛠️ Requirements

- Python 3.x
- `cryptography` module (Install using: `pip install cryptography`)
- Test files/folder to encrypt

---

## 🗂️ Files

- `encrypt.py` – Script to encrypt files inside a specified directory.
- `decrypt.py` – Script to decrypt files using the stored encryption key.
- `secret.key` – The encryption key saved during the simulation (keep it safe!).

---

## ⚙️ How It Works

### 🔐 `encrypt.py`

- Generates a random encryption key using Fernet.
- Saves the key to `secret.key`.
- Encrypts all non-excluded files in the specified folder using Fernet symmetric encryption.

### 🔓 `decrypt.py`

- Reads the saved encryption key from `secret.key`.
- Decrypts previously encrypted files back to their original state.

### ❗ Kill Switch

- A built-in "kill switch" checks for the presence of a `STOP` file in the directory.
- If found, encryption halts immediately for safety.

---

## 🧪 Sample Output

```yaml
Enter folder path to encrypt: sample_files
[+] Encrypted: sample_files\file1.txt
[+] Encrypted: sample_files\file2.txt
```

```yaml
Enter folder path to decrypt: sample_files
[+] Decrypted: sample_files\file1.txt
[+] Decrypted: sample_files\file2.txt
```

---

## ⚠️ Disclaimer – Educational Use Only

This project simulates ransomware behavior **strictly for educational and ethical cybersecurity awareness purposes**. It is intended to demonstrate how file encryption and decryption works in controlled environments.

- ❗ **Do NOT deploy this code on any system without explicit permission.**
- ❗ **Do NOT use this code for malicious purposes.**
- ❗ Unauthorized access, encryption, or tampering with user files is a **criminal offense** under cybersecurity laws.
- ✔️ Always run this script in a **safe, isolated directory** with **non-critical test files**.
- ✔️ The developers and contributors are **not responsible for any misuse or damage** caused by this project.

> ⚠️ **Reminder:** Cybersecurity is about defense, not offense.

---

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
