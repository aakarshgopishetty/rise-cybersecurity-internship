import re
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import font as tkFont

suspicious_keywords = ["login", "verify", "update", "secure", "account", "bank", "signin", "confirm"]

def is_ip_address(url):
    return re.match(r"http[s]?://(\d{1,3}\.){3}\d{1,3}", url) is not None

def contains_suspicious_keywords(url):
    return [i for i in suspicious_keywords if i in url.lower()]

def triggered_rules(url):
    triggers = []

    if len(url) > 75:
        triggers.append("• URL too long (>75 characters)")
    if is_ip_address(url):
        triggers.append("• Contains IP address instead of domain")
    keywords = contains_suspicious_keywords(url)
    if keywords:
        triggers.append(f"• Suspicious keyword(s): {', '.join(keywords)}")
    if url.count('.') > 4:
        triggers.append("• Too many subdomains")
    if '@' in url:
        triggers.append("• Contains '@' symbol (URL redirection)")
    domain = re.findall(r"https?://([^/]+)", url)
    if domain and '-' in domain[0]:
        triggers.append("• Hyphen in domain name")

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

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    reasons = triggered_rules(url)
    suspicious = is_suspicious(url)

    if suspicious:
        result_label.config(text="⚠️  SUSPICIOUS URL DETECTED", fg="#d32f2f")
        result_frame.config(bg="#ffebee")
        recommendation.config(text="🛡️ Recommendation: Do not visit this website", fg="#d32f2f")
    else:
        result_label.config(text="✅  URL APPEARS LEGITIMATE", fg="#388e3c")
        result_frame.config(bg="#e8f5e8")
        recommendation.config(text="✓ This URL passed basic security checks", fg="#388e3c")

    if reasons:
        explanation_text = "Security Issues Found:\n" + "\n".join(reasons)
        explanation.config(text=explanation_text, fg="#424242")
    else:
        explanation.config(text="✓ No suspicious patterns detected in this URL.", fg="#666666")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="")
    explanation.config(text="")
    recommendation.config(text="")
    result_frame.config(bg="#f5f5f5")

def on_enter_key(event):
    check_url()

root = tk.Tk()
root.title("🔒 Phishing Website Detector")
root.geometry("650x550")
root.resizable(True, True)
root.minsize(600, 500)
root.config(bg="#f0f0f0")

title_font = tkFont.Font(family="Arial", size=14, weight="bold")
header_font = tkFont.Font(family="Arial", size=11, weight="bold")
body_font = tkFont.Font(family="Arial", size=9)
button_font = tkFont.Font(family="Arial", size=10, weight="bold")

header_frame = tk.Frame(root, bg="#2196f3", height=40)
header_frame.pack(fill="x", padx=0, pady=0)
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame, 
    text="🔒 Phishing Website Detector", 
    font=title_font, 
    bg="#2196f3", 
    fg="white"
)
title_label.pack(pady=(10, 0))

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

input_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid", bd=1)
input_frame.pack(fill="x", pady=(0, 10))

tk.Label(
    input_frame, 
    text="Enter URL to analyze:", 
    font=header_font, 
    bg="#ffffff", 
    fg="#333333"
).pack(anchor="w", padx=12, pady=(12, 5))

entry = tk.Entry(
    input_frame, 
    width=60, 
    font=("Arial", 10), 
    relief="solid", 
    bd=1,
    bg="#fafafa"
)
entry.pack(padx=12, pady=(0, 8), ipady=6, fill="x")
entry.bind('<Return>', on_enter_key)

button_frame = tk.Frame(input_frame, bg="#ffffff")
button_frame.pack(pady=(0, 12))

check_button = tk.Button(
    button_frame,
    text="🔍 Analyze URL",
    command=check_url,
    bg="#4caf50",
    fg="white",
    font=button_font,
    relief="flat",
    padx=15,
    pady=6,
    cursor="hand2"
)
check_button.pack(side="left", padx=(0, 8))

clear_button = tk.Button(
    button_frame,
    text="🗑️ Clear",
    command=clear_fields,
    bg="#757575",
    fg="white",
    font=button_font,
    relief="flat",
    padx=15,
    pady=6,
    cursor="hand2"
)
clear_button.pack(side="left")

result_frame = tk.Frame(main_frame, bg="#f5f5f5", relief="solid", bd=1)
result_frame.pack(fill="both", expand=True)

tk.Label(
    result_frame, 
    text="Analysis Results", 
    font=header_font, 
    bg="#f5f5f5", 
    fg="#333333"
).pack(anchor="w", padx=12, pady=(12, 8))

result_label = tk.Label(
    result_frame, 
    text="", 
    font=("Arial", 11, "bold"), 
    bg="#f5f5f5"
)
result_label.pack(pady=(0, 3))

recommendation = tk.Label(
    result_frame, 
    text="", 
    font=("Arial", 9, "italic"), 
    bg="#f5f5f5"
)
recommendation.pack(pady=(0, 8))

separator = tk.Frame(result_frame, height=1, bg="#dddddd")
separator.pack(fill="x", padx=12, pady=(0, 8))

explanation = tk.Label(
    result_frame, 
    text="Enter a URL above to begin analysis...", 
    wraplength=550, 
    justify="left", 
    fg="#666666", 
    font=body_font,
    bg="#f5f5f5",
    height=8
)
explanation.pack(anchor="w", padx=12, pady=(0, 12), fill="x")

status_frame = tk.Frame(root, bg="#e0e0e0", height=22)
status_frame.pack(fill="x", side="bottom")
status_frame.pack_propagate(False)

status_label = tk.Label(
    status_frame, 
    text="Ready to analyze URLs", 
    font=("Arial", 8), 
    bg="#e0e0e0", 
    fg="#666666"
)
status_label.pack(side="left", padx=8, pady=2)

entry.focus()

root.mainloop()