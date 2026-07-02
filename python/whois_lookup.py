import whois


def whois_lookup(domain):
    try:
        print("\n" + "=" * 60)
        print(f"WHOIS Report for: {domain}")
        print("=" * 60)

        result = whois.whois(domain)

        print(f"Domain Name     : {result.domain_name}")
        print(f"Registrar       : {result.registrar}")
        print(f"Creation Date   : {result.creation_date}")
        print(f"Expiration Date : {result.expiration_date}")
        print(f"Updated Date    : {result.updated_date}")
        print(f"Name Servers    : {result.name_servers}")

    except Exception as e:
        print(f"\nError: {e}")