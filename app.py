from python.security_headers_checker import check_headers
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def menu():
    while True:
        clear_screen()

        print("=" * 60)
        print("      CyberInvincible Security Toolkit (CIST)")
        print("                  Version 1.0.0")
        print("=" * 60)
        print("        Python-Based Cybersecurity Toolkit")
        print("=" * 60)

        print("\nReconnaissance")
        print("-" * 20)
        print("1. WHOIS Lookup")
        print("2. DNS Lookup")
        print("3. Subdomain Enumerator")
        print("4. Banner Grabber")

        print("\nNetwork")
        print("-" * 20)
        print("5. Port Scanner")

        print("\nWeb Security")
        print("-" * 20)
        print("6. Security Headers Checker")
        print("7. SSL Certificate Analyzer")
        print("8. HTTP Methods Tester")

        print("\nUtilities")
        print("-" * 20)
        print("9. Hash Generator")

        print("\n0. Exit")

        print("\n" + "=" * 60)

        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nWHOIS Lookup coming soon.")

        elif choice == "2":
            print("\nDNS Lookup coming soon.")

        elif choice == "3":
            print("\nSubdomain Enumerator coming soon.")

        elif choice == "4":
            print("\nBanner Grabber coming soon.")

        elif choice == "5":
            print("\nPort Scanner coming soon.")

        elif choice == "6":
            website = input("\nEnter Website URL: ").strip()

            if not website.startswith("http"):
                website = "https://" + website

            check_headers(website)

        elif choice == "7":
            print("\nSSL Certificate Analyzer coming soon.")

        elif choice == "8":
            print("\nHTTP Methods Tester coming soon.")

        elif choice == "9":
            print("\nHash Generator coming soon.")

        elif choice == "0":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")

        pause()


if __name__ == "__main__":
    menu()