def main():
    while True:
        print("\n" + "=" * 60)
        print(" CyberInvincible Security Toolkit (CIST)")
        print("=" * 60)
        print("1. Security Headers Checker")
        print("2. Port Scanner (Coming Soon)")
        print("3. WHOIS Lookup (Coming Soon)")
        print("4. DNS Lookup (Coming Soon)")
        print("0. Exit")
        print("=" * 60)

        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nLaunching Security Headers Checker...\n")

        elif choice == "2":
            print("\nPort Scanner - Coming Soon!")

        elif choice == "3":
            print("\nWHOIS Lookup - Coming Soon!")

        elif choice == "4":
            print("\nDNS Lookup - Coming Soon!")

        elif choice == "0":
            print("\nThank you for using CIST!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()