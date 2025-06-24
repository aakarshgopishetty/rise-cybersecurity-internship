import re
import tkinter as tk
from tkinter import ttk, font as tkFont
import nltk
from nltk.corpus import words

try:
    word_list = set(words.words())
except LookupError:
    nltk.download('words')
    word_list = set(words.words())

def check_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("• Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("• Add uppercase letters (A-Z)")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("• Add lowercase letters (a-z)")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("• Add numbers (0-9)")

    if re.search(r"[^a-zA-Z0-9]", password):
        strength += 1
    else:
        suggestions.append("• Add special characters (!@#$%^&*)")

    if password.lower() in word_list:
        strength = min(strength, 2)
        suggestions.append("• Avoid common dictionary words")

    if strength <= 2:
        level = "Weak"
    elif strength == 3:
        level = "Moderate"
    elif strength == 4:
        level = "Strong"
    else:
        level = "Very Strong"

    return level, suggestions, strength

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text="👁️ Hide")
    else:
        entry.config(show='*')
        toggle_button.config(text="👁️ Show")

def on_password_change(*args):
    password = password_var.get()
    if password:
        result, suggestions, strength = check_strength(password)
        update_strength_display(result, suggestions, strength)
    else:
        reset_display()

def update_strength_display(result, suggestions, strength):
    # Update strength indicator
    if result == "Weak":
        color = "#f44336"
        progress_color = "#ffcdd2"
        progress_width = 1
    elif result == "Moderate":
        color = "#ff9800"
        progress_color = "#ffe0b2"
        progress_width = 2
    elif result == "Strong":
        color = "#4caf50"
        progress_color = "#c8e6c9"
        progress_width = 4
    else:  # Very Strong
        color = "#2e7d32"
        progress_color = "#a5d6a7"
        progress_width = 5

    result_label.config(text=f"🔒 {result}", fg=color)
    
    # Update progress bars
    for i, bar in enumerate(progress_bars):
        if i < progress_width:
            bar.config(bg=color)
        else:
            bar.config(bg="#e0e0e0")

    # Update suggestions
    if suggestions:
        suggestion_text = "💡 Improve your password:\n" + "\n".join(suggestions)
        suggestion_label.config(text=suggestion_text, fg="#666666")
    else:
        suggestion_label.config(text="✅ Excellent! Your password is secure.", fg="#4caf50")

def reset_display():
    result_label.config(text="Enter a password to check its strength", fg="#999999")
    suggestion_label.config(text="", fg="#666666")
    for bar in progress_bars:
        bar.config(bg="#e0e0e0")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("500x450")
root.resizable(True, True)
root.minsize(450, 400)
root.config(bg="#f8f9fa")

# Custom fonts
title_font = tkFont.Font(family="Arial", size=16, weight="bold")
header_font = tkFont.Font(family="Arial", size=12, weight="bold")
body_font = tkFont.Font(family="Arial", size=10)
button_font = tkFont.Font(family="Arial", size=10, weight="bold")

# Header frame
header_frame = tk.Frame(root, bg="#1976d2", height=60)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)

title_label = tk.Label(
    header_frame,
    text="🔐 Password Strength Checker",
    font=title_font,
    bg="#1976d2",
    fg="white"
)
title_label.pack(expand=True)

# Main content frame
main_frame = tk.Frame(root, bg="#f8f9fa")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Password input section
input_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
input_frame.pack(fill="x", pady=(0, 15))

tk.Label(
    input_frame,
    text="Enter your password:",
    font=header_font,
    bg="white",
    fg="#333333"
).pack(anchor="w", padx=15, pady=(15, 8))

# Password entry with variable for real-time checking
password_var = tk.StringVar()
password_var.trace('w', on_password_change)

entry_frame = tk.Frame(input_frame, bg="white")
entry_frame.pack(fill="x", padx=15, pady=(0, 10))

entry = tk.Entry(
    entry_frame,
    textvariable=password_var,
    show="*",
    font=("Arial", 12),
    relief="solid",
    bd=1,
    bg="#fafafa",
    width=30
)
entry.pack(side="left", fill="x", expand=True, ipady=8)

toggle_button = tk.Button(
    entry_frame,
    text="👁️ Show",
    command=toggle_password,
    bg="#e3f2fd",
    fg="#1976d2",
    font=button_font,
    relief="flat",
    padx=10,
    cursor="hand2"
)
toggle_button.pack(side="right", padx=(10, 0))

# Strength indicator section
strength_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
strength_frame.pack(fill="x", pady=(0, 15))

tk.Label(
    strength_frame,
    text="Password Strength:",
    font=header_font,
    bg="white",
    fg="#333333"
).pack(anchor="w", padx=15, pady=(15, 8))

result_label = tk.Label(
    strength_frame,
    text="Enter a password to check its strength",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#999999"
)
result_label.pack(pady=(0, 10))

# Progress bar indicators
progress_frame = tk.Frame(strength_frame, bg="white")
progress_frame.pack(pady=(0, 15))

progress_bars = []
for i in range(5):
    bar = tk.Frame(progress_frame, width=60, height=8, bg="#e0e0e0", relief="flat")
    bar.pack(side="left", padx=2)
    bar.pack_propagate(False)
    progress_bars.append(bar)

# Suggestions section
suggestions_frame = tk.Frame(main_frame, bg="white", relief="solid", bd=1)
suggestions_frame.pack(fill="both", expand=True)

tk.Label(
    suggestions_frame,
    text="Security Tips:",
    font=header_font,
    bg="white",
    fg="#333333"
).pack(anchor="w", padx=15, pady=(15, 8))

suggestion_label = tk.Label(
    suggestions_frame,
    text="",
    font=body_font,
    bg="white",
    fg="#666666",
    wraplength=450,
    justify="left",
    anchor="nw"
)
suggestion_label.pack(anchor="w", padx=15, pady=(0, 10), fill="x")

# Separator line
separator = tk.Frame(suggestions_frame, height=1, bg="#e0e0e0")
separator.pack(fill="x", padx=15, pady=(5, 10))

# Tips section with proper canvas
tips_canvas = tk.Canvas(suggestions_frame, bg="white", height=80, highlightthickness=0)
tips_canvas.pack(fill="x", padx=15, pady=(0, 15))

tips_text = """🛡️ Security Best Practices:
• Use a unique password for each account
• Consider using a password manager  
• Enable two-factor authentication when possible
• Avoid personal information in passwords"""

tips_label = tk.Label(
    tips_canvas,
    text=tips_text,
    font=("Arial", 9),
    bg="white",
    fg="#888888",
    justify="left",
    anchor="nw"
)
tips_canvas.create_window(0, 0, window=tips_label, anchor="nw")

# Focus on password entry
entry.focus()

root.mainloop()