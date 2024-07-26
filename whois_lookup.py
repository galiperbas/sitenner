# whois
# flag: -w

import whois
import sys


def whois_looking(domain):
    try:
        # Perform Whois lookup
        whois_info = whois.whois(domain)

        # Print the result
        for key, value in whois_info.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    domain = sys.argv[1]
    print(whois_looking(domain))
