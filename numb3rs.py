import re
import sys


def main():
    ip = input("IPV4 address: ").strip()
    print(validate(ip))

def validate(ip):
    matches = re.search(r"^(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.((2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$",ip)
    if matches:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()