import sys
import subprocess
from colorama import Fore, Style


def execute_command(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            return stderr.decode()
        return stdout.decode()
    except Exception as e:
        return str(e)


def index():
    # Renk tanımlamaları
    Yellow = Fore.YELLOW
    Red = Fore.RED
    BM = Fore.BLUE
    Green = Fore.GREEN
    Normal = Style.RESET_ALL

    print(f'''
    {BM}S{Normal}itenner - {Yellow}S{Normal}canning {Red}T{Normal}ool
          _____
         /     \\
        | () () |
         \\  ^  /
          |||||
          |||||
          {Green}©{Normal}2024
        ''')


def main():
    if len(sys.argv) < 3:
        index()
        print()
        print("Usage: python/python3 main.py <domain> <flags>")
        print("-i: domain to ip")
        print("-w: whois")
        print("-p: port scan")
        print("-g: google excel search")
        print("-l: link collector")
        print("-A: all flags")
        print("-o: output")
        print()

        return

    domain = sys.argv[1]
    flags = sys.argv[2:]

    output = []

    if '-i' in flags:
        result = execute_command(['python', 'ip_lookup.py', domain])
        output.append(result)

    if '-w' in flags:
        result = execute_command(['python', 'whois_lookup.py', domain])
        output.append(result)

    if '-p' in flags:
        result = execute_command(['python', 'port_scan.py', domain])
        output.append(result)

    if '-g' in flags:
        result = execute_command(['python', 'google_excel_search.py', domain])
        output.append(result)

    if '-l' in flags:
        result = execute_command(['python', 'link_collector.py', domain])
        output.append(result)

    if '-A' in flags:
        result = execute_command(['python', 'ip_lookup.py', domain])
        output.append(result)
        result = execute_command(['python', 'whois_lookup.py', domain])
        output.append(result)
        result = execute_command(['python', 'port_scan.py', domain])
        output.append(result)
        result = execute_command(['python', 'google_excel_search.py', domain])
        output.append(result)
        result = execute_command(['python', 'link_collector.py', domain])
        output.append(result)

    if '-o' in flags:
        with open('output.txt', 'w') as f:
            f.write('\n'.join(output))
    else:
        print('\n'.join(output))


if __name__ == "__main__":
    main()
