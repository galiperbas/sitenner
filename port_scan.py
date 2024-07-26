import socket
import sys

def port_scan(domain, ports=[22, 80, 443, 3389]):
    ip_address = socket.gethostbyname(domain)
    results = {}
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            results[port] = "Open"
        else:
            results[port] = "Closed"
        sock.close()
    return results


if __name__ == "__main__":


    domain = sys.argv[1]
    results = port_scan(domain)
    for port, status in results.items():
        print(f"Port {port}: {status}")
