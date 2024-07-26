import requests
from bs4 import BeautifulSoup
import sys

def collect_links(domain):
    response = requests.get(f"http://{domain}")
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links


if __name__ == "__main__":


    domain = sys.argv[1]
    results = collect_links(domain)
    for link in results:
        print(link)
