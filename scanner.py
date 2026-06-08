import socket

target = input("Enter IP Address: ")

ports = [21, 22, 80, 443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} Open")

    sock.close()