import re
import sys


def main():
    print(count(input("Text: ")))


def count(dane):
    suma = 0 
    if dane := re.findall(r"\b(um)\b",dane,re.IGNORECASE):
        suma = suma + len(dane)
    else:
        suma = 0 
    return suma 

if __name__ == "__main__":
    main()