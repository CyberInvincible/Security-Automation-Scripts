import socket
import time


def port_scanner(host, start_port, end_port):
    print("\n" + "=" * 60)
    print("Port Scanner")
    print("=" * 60)
    print(f"Target : {host}")
    print(f"Ports  : {start_port}-{end_port}")
    print("=" * 60)

    start_time = time.time()

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[OPEN ] {port:<6} {service}")
            open_ports.append(port)

        sock.close()

    end_time = time.time()

    print("\n" + "=" * 60)
    print(f"Open Ports : {len(open_ports)}")
    print(f"Scan Time  : {round(end_time-start_time,2)} seconds")
    print("=" * 60)