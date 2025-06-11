import re
import tkinter as tk
from tkinter import messagebox

suspicious_keywords = ["login", "verify", "update", "secure", "account", "bank", "signin", "confirm"]

def is_ip_address(url):
    return re.match(r"http[s]?://(\d{1,3}\.){3}\d{1,3}", url) is not None

def contains_suspicious_keywords(url):
    return [i for i in suspicious_keywords if i in url.lower()]

def triggered_rules(url):
    triggers = []

    if len(url) > 75:
        triggers.append("URL too long (>75)")
    if is_ip_address(url):
        triggers.append("Contains IP address")
    keywords = contains_suspicious_keywords(url)
    if keywords:
        triggers.append(f"Suspicious keyword(s): {', '.join(keywords)}")
    if url.count('.') > 4:
        triggers.append("Too many dots (subdomains)")
    if '@' in url:
        triggers.append("Contains '@' symbol")
    domain = re.findall(r"https?://([^/]+)", url)
    if domain and '-' in domain[0]:
        triggers.append("Hyphen in domain")

    return triggers

def is_suspicious(url):
    if '@' in url:
        return True
    return len(triggered_rules(url)) >= 2

def check_url():
    url = entry.get().strip()
    if not url:
        messagebox.showwarning("Empty Field", "Please enter a URL")
        return

    reasons = triggered_rules(url)
    suspicious = is_suspicious(url)

    result_label.config(
        text="⚠️ Suspicious URL" if suspicious else "✅ Legitimate URL",
        fg="red" if suspicious else "green"
    )

    explanation.config(text="\n".join(reasons) if reasons else "No suspicious patterns found.")

# GUI setup
root = tk.Tk()
root.title("Phishing Website Detector")
root.geometry("520x300")
root.resizable(False, False)

tk.Label(root, text="Enter URL to Check:", font=("Arial", 12)).pack(pady=8)
entry = tk.Entry(root, width=60, font=("Arial", 11))
entry.pack(pady=5)

tk.Button(root, text="Check URL", command=check_url, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=6)

explanation = tk.Label(root, text="", wraplength=500, justify="left", fg="gray", font=("Arial", 10))
explanation.pack(pady=5)

root.mainloop()
