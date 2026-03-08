import requests
while True:
    x = input("czy chcesz kontynuowac ")
    if x ==  "nie":
        break
    else:
        symbol_1 =  input("Podaj symbol pierwszego  krypto ").strip().upper()
        kryptowaluta_1 = requests.get("https://api.coinbase.com/v2/prices/"+symbol_1+"-USD/spot").json()
        symbol_2 = input("Podaj drugiego symbol krypto ").strip().upper()
        kryptowaluta_2 = requests.get("https://api.coinbase.com/v2/prices/"+symbol_2+"-USD/spot").json()
        cena_1 = float(kryptowaluta_1["data"]["amount"])
        cena_2 = float(kryptowaluta_2["data"]["amount"])
        if cena_1 > cena_2:
            print(f"{symbol_1} jest drozszy od {symbol_2} o {(cena_1-cena_2):.1f}$  {(cena_2/cena_1)*100:.1f}%")
        if cena_2 > cena_1:
            print(f" print(f{symbol_2} jest drozszy od {symbol_1} o {(cena_2-cena_1):.1f}$ {(cena_1/cena_2)*100:.1f}%")