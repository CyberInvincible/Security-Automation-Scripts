import whois


def whois_lookup(domain):
    try:
        print("\n" + "=" * 60)
        print(f"WHOIS Report for: {domain}")
        print("=" * 60)

        info = whois.whois(domain)

        print(f"Domain Name      : {info.domain_name}")
        print(f"Registrar        : {info.registrar}")
        print(f"Creation Date    : {info.creation_date}")
        print(f"Expiration Date  : {info.expiration_date}")
        print(f"Name Servers     : {info.name_servers}")

    except Exception as e:
        print(f"\nError: {e}")