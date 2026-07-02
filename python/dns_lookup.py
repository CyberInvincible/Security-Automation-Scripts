import socket


def dns_lookup(domain):
    try:
        print("\n" + "=" * 60)
        print(f"DNS Lookup Report for: {domain}")
        print("=" * 60)

        ip = socket.gethostbyname(domain)

        print(f"Domain      : {domain}")
        print(f"IPv4 Address: {ip}")

        print("\nAddress Information")
        print("-" * 30)

        addresses = socket.getaddrinfo(domain, None)

        unique = set()

        for addr in addresses:
            ip_addr = addr[4][0]

            if ip_addr not in unique:
                unique.add(ip_addr)
                print(ip_addr)

        print("\nLookup completed successfully.")

    except socket.gaierror:
        print("\nError: Unable to resolve domain.")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")