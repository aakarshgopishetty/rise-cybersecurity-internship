import re
import tkinter as tk

def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[^a-zA-Z0-9]", password):
        strength += 1

    if strength < 1:
        return "Very Weak"
    elif strength == 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    elif strength == 4:
        return "Strong"
    else:
        return "Very Strong"

def on_check():
    password = entry.get()
    result = check_strength(password)
    result_label.config(text=f"Password Strength: {result}")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check)
check_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
