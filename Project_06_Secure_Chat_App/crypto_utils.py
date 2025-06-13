from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# For demonstration purposes only; use secure key storage in production
SECRET_KEY = b'yoursecretkey123456789012345678!'

def encrypt_message(message):
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(cipher.nonce + tag + ciphertext).decode()

def decrypt_message(encrypted_msg):
    raw = base64.b64decode(encrypted_msg.encode())
    nonce = raw[:16]
    tag = raw[16:32]
    ciphertext = raw[32:]
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()