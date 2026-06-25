import socket

target = input("Enter IP or hostname: ")
port = int(input("Enter port: "))

try:
    s = socket.socket()
    s.settimeout(3)
    s.connect((target, port))

    banner = s.recv(1024)
    print("\nBanner:")
    print(banner.decode(errors="ignore"))

    s.close()

except Exception as e:
    print(f"Error: {e}")
