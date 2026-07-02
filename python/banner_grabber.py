import socket


def banner_grabber(host, port):
    try:
        print("\n" + "=" * 60)
        print("Banner Grabber")
        print("=" * 60)

        print(f"Target : {host}")
        print(f"Port   : {port}")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        s.connect((host, port))

        try:
            banner = s.recv(1024).decode(errors="ignore").strip()

            if banner:
                print("\nBanner")
                print("-" * 30)
                print(banner)
            else:
                print("\nNo banner received.")
        except:
            print("\nConnected successfully, but no banner was received.")

        s.close()

    except Exception as e:
        print(f"\nConnection failed: {e}")