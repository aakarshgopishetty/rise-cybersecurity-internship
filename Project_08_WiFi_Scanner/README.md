# 📡 Wi-Fi Network Scanner

![Status](https://img.shields.io/badge/Projects-8%2F8%20Completed-brightgreen)

## 🧠 Overview

This project is a simple Python-based **Wi-Fi Network Scanner**. It uses the `pywifi` module to detect and list all nearby wireless networks along with their **SSID**, **signal strength**, and **security type**. It helps users identify the strongest and most secure networks for optimal connectivity.

---

## 🎯 Objective

> Simulate a utility that scans and displays nearby Wi-Fi networks with basic details such as signal strength and encryption type.

---

## 📋 Requirements

- Python 3.x
- `pywifi` module
- `comtypes` (only on Windows)
- OS: Windows or Linux (tested on Windows)

---

## 🧪 Installation

```bash
pip install pywifi comtypes
```

## ▶️ How to Run

```bash
python main.py
```

## 🧾 Features

- Detects all nearby Wi-Fi networks

- Displays: SSID (Wi-Fi name), Signal strength (in dBm), Security type (WPA, WPA2, etc.)

## 🛠️ How It Works

- The script uses pywifi to interface with your system’s wireless interface.
- Scans for available networks.
- Extracts signal strength and authentication type.
- Displays the information in a user-friendly format.

## 📊 Example Output

```yaml
Nearby Wi-Fi Networks:

SSID                           Signal (dBm)    Security
------------------------------------------------------------
Home Network                   -66             WPA2-PSK
Hone Network 2                 -73             WPA2-PSK
```

## ⚠️ Notes

- Must be run on a system that has Wi-Fi hardware.
- pywifi is known to work more reliably on Windows than on some Linux systems.

## 📚 Educational Use Only

This project is for educational and demonstrative purposes only. Do not use this tool to access or tamper with networks you do not own or have explicit permission to analyze.

## 📽️ Demo Video

[Click here to watch the demo](https://www.youtube.com/watch?v=Wx3RAWNDaCs)

## 👨‍💻 Developed by

**Aakarsh Gopishetty**  
Cybersecurity & Ethical Hacking Intern – Tamizhan Skills, Summer 2025
