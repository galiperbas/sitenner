import sys
from urllib.parse import quote


def print_google_dork_link(domain):
    try:
        # Google arama dork'unu oluştur
        query = f"site:{domain} filetype:xls OR filetype:xlsx"
        encoded_query = quote(query)
        google_search_url = f"https://www.google.com/search?q={encoded_query}"

        print("Google arama linki:")
        print(google_search_url)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python google_dork_search.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    print_google_dork_link(domain)
