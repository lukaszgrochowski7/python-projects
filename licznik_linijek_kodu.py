import sys
suma = 0

if len(sys.argv) < 2 :
    sys.exit("nie podano pliku")
elif len(sys.argv) > 3:
    sys.exit("za duzo plikow")


else:
    try:
        "." in sys.argv
    except TypeError:
        sys.exit("podano zly format plikue")
    else:
        try:
            sys.argv[1].split('.')[1] != "py"
        except IndexError:
            sys.exit("podano zly format pliku")
        else:
            search = sys.argv[1]
            with open(search) as file:
                for row in file:
                    if row.strip() =="":
                        pass
                    elif row.startswith('#'):
                        pass
                    else:
                        suma = suma + 1 
            print(suma)         
                