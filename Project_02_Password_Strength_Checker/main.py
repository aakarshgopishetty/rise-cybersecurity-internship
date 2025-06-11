import re
import tkinter as tk
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
        suggestions.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Try adding uppercase letters (A-Z)")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Try adding lowercase letters (a-z)")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Try adding numbers (0-9)")

    if re.search(r"[^a-zA-Z0-9]", password):
        strength += 1
    else:
        suggestions.append("Try adding special characters (!, @, #, etc.)")

    if password.lower() in word_list:
        strength = min(strength, 2)
        suggestions.append("Avoid using dictionary words")

    if strength <= 2:
        level = "Weak"
    elif strength == 3:
        level = "Moderate"
    elif strength == 4:
        level = "Strong"
    else:
        level = "Very Strong"

    return level, suggestions

def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text="Hide")
    else:
        entry.config(show='*')
        toggle_button.config(text="Show")

def on_check():
    password = entry.get()
    result, suggestions = check_strength(password)

    if result == "Weak":
        color = "red"
    elif result == "Moderate":
        color = "orange"
    elif result == "Strong":
        color = "green"
    else:
        color = "darkgreen"

    result_label.config(text=f"Password Strength: {result}", fg=color)

    if suggestions:
        suggestion_text = "Suggestions:\n- " + "\n- ".join(suggestions)
    else:
        suggestion_text = "Excellent! No suggestions needed."

    suggestion_label.config(text=suggestion_text)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

toggle_button = tk.Button(root, text="Show", command=toggle_password)
toggle_button.pack(pady=2)

check_button = tk.Button(root, text="Check Strength", command=on_check)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="", font=("Arial", 10), wraplength=350, justify="left")
suggestion_label.pack(pady=5)

root.mainloop()