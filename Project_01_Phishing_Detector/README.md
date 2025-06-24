# 🛡️ Phishing Website Detection Tool

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Educational-yellow)
![Last Commit](https://img.shields.io/github/last-commit/aakarshgopishetty/rise-cybersecurity-internship)
![Repo Size](https://img.shields.io/github/repo-size/aakarshgopishetty/rise-cybersecurity-internship)

A lightweight **Phishing URL Detection Tool** built with **Python** and **Tkinter**, using **rule-based logic** to identify suspicious URLs.

> ✅ Developed as part of the **Cybersecurity & Ethical Hacking Internship** – Tamizhan Skills (June 2025)

---

## 🚨 Problem Statement

Phishing websites deceive users into entering sensitive information such as usernames, passwords, and financial data, leading to fraud and identity theft.

---

## 🎯 Objective

To build a simple and effective tool that helps users detect potentially harmful URLs using predefined suspicious patterns.

---

## 🛠️ Features

- ✅ Rule-based phishing detection
- 📋 Lists **triggered rules** for transparency
- 🎨 Color-coded output (Green = Safe, Red = Suspicious)
- 🧑‍💻 User-friendly GUI using Tkinter
- ⚙️ Easily extensible for further enhancements

---

## 📌 Detection Rules

The tool checks for:

- Presence of `@` symbol
- Use of IP addresses instead of domains
- Long URL lengths (over 75 characters)
- Suspicious keywords (`login`, `secure`, `update`, etc.)
- Multiple subdomains or excessive dots
- Hyphens in the domain

> If two or more rules are triggered, the URL is flagged as suspicious.

---

## 📽️ Demo Video

[Click here to watch the demo](https://www.youtube.com/watch?v=7DESS11h5KQ)

---

## 🚀 How to Run

Make sure Python is installed, then run:

```bash
python phishing_gui.py
