import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or domain: ")

def scan_port(port):
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Port {port} is open")
    except:
        pass

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))

#AF_INET =IPv4, SOCK_STREAM = TCP connection