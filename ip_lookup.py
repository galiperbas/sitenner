# domain to ip
# flag: -i

import socket
import sys

def domain_to_ip(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Invalid domain name"


if __name__ == "__main__":


    domain = sys.argv[1]
    print(domain_to_ip(domain))
