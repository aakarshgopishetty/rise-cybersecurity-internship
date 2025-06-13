import tkinter as tk
from tkinter import scrolledtext
import socket
import threading
from crypto_utils import encrypt_message, decrypt_message

HOST = input("Enter server IP: ")
PORT = 5555

class ClientChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Secure Chat")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def send_message(self):
        message = self.entry.get()
        if message:
            encrypted = encrypt_message(message)
            self.sock.send(encrypted.encode())
            self.display_message("You: " + message)
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                encrypted = self.sock.recv(4096).decode()
                if encrypted == 'exit':
                    break
                message = decrypt_message(encrypted)
                self.display_message("Server: " + message)
            except:
                break

    def display_message(self, message):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.configure(state='disabled')
        self.text_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientChatApp(root)
    root.mainloop()
