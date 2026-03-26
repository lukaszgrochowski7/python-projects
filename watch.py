import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if match := re.search(r"https?://(?:www\.)youtube\.com/embed/([a-zA-Z0-9_]+)",s,re.IGNORECASE):
        koncowka = match.group(1)
        return f"https://youtu.be/{koncowka}"
        






if __name__ == "__main__":
    main()