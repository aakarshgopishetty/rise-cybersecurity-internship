# 🔐 Project 6: Secure Chat App

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Encryption](https://img.shields.io/badge/Encryption-AES256-purple)
![Projects](https://img.shields.io/badge/Projects-5%2F8%20Completed-brightgreen)

## 📄 Problem Statement

Most chat applications do not offer end-to-end encryption by default. This project demonstrates how to build a secure messaging application with AES encryption to ensure privacy during communication.

## 🎯 Objective

To develop a secure chat application that allows encrypted text communication between two users using AES-256 encryption.

## 🛠️ Requirements

- Python 3.x  
- [`pycryptodome`](https://pypi.org/project/pycryptodome/) (`pip install pycryptodome`)
- `socket`, `threading`, and `tkinter` (standard libraries)

## 🔐 How It Works

- Messages are encrypted using AES-256 in EAX mode before transmission.
- Messages are decrypted on the receiver's end.
- Both server and client apps have a GUI made with Tkinter for sending/receiving encrypted messages.

## 🧪 How to Run

### 🖥️ Server Side

```bash
python server_GUI.py
```

- Starts the server GUI.
- Waits for a client to connect.

### 💻 Client Side

```bash
python client_GUI.py
```

- Enter the IP address of the server (e.g., 127.0.0.1 for localhost).
- Start sending encrypted messages.

## 🧠 Security

- Encryption: AES-256 using EAX mode (confidentiality and integrity).

- Key: Pre-shared 32-byte key stored in crypto_utils.py.

### ⚠️ For production or real-world use, never hardcode keys. Use secure key exchange methods like Diffie-Hellman or RSA

## ⚠️ Disclaimer

This project is built strictly for educational and demonstration purposes as part of the Rise Cybersecurity Internship by Tamizhan Skills. Do not use it for unauthorized communication interception or data exfiltration.

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
