# 🚪 Project 4: Port Scanner

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Security](https://img.shields.io/badge/Tool-Type%3A%20Recon-orange)

## 📄 Problem Statement

Network ports are the entry points to services on a system. Open or misconfigured ports can be exploited by attackers. This tool helps detect open TCP ports on a given host for basic vulnerability assessment.

---

## 🎯 Objective

Build a lightweight and fast port scanner using Python that scans a target IP address or domain for open TCP ports from 1 to 1024.

---

## 🛠️ Requirements

- Python 3.x
- `socket` module (standard library)
- `concurrent.futures` (standard library)

---

## ⚙️ How It Works

- Uses socket to attempt a TCP connection to each port.
- Uses ThreadPoolExecutor to scan multiple ports concurrently.
- Ports that accept connections are marked as open.

---

## 🚀 How to Run

```bash
python main.py
```

### ✅ Sample Input

```yaml
Enter target IP or domain: example.com
```

### ✅ Sample Output

```yaml
Enter target IP or domain: scanme.nmap.org
[+] Port 22 is open
[+] Port 80 is open
```

---

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
