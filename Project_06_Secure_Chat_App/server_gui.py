import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = ''
PORT = 5555

class SecureChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Chat Server")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        self.send_button = tk.Button(root, text="Send", command=self.send_message, state=tk.DISABLED)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen(1)

        # Start thread to wait for client connection
        threading.Thread(target=self.accept_connection, daemon=True).start()

    def accept_connection(self):
        self.display_message("[+] Waiting for a client...")
        self.conn, self.addr = self.sock.accept()
        self.display_message(f"[+] Connected to {self.addr}")
        self.send_button.config(state=tk.NORMAL)
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        message = self.entry.get()
        if message:
            encrypted = encrypt_message(message)
            try:
                self.conn.send(encrypted.encode())
                self.display_message("You: " + message)
                self.entry.delete(0, tk.END)
            except:
                self.display_message("[!] Failed to send message.")

    def receive_messages(self):
        while True:
            try:
                encrypted = self.conn.recv(4096).decode()
                if encrypted == 'exit':
                    self.display_message("[Client disconnected]")
                    break
                message = decrypt_message(encrypted)
                self.display_message("Client: " + message)
            except:
                break

    def display_message(self, message):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.configure(state='disabled')
        self.text_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureChatApp(root)
    root.mainloop()
