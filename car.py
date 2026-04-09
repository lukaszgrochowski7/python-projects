
import sys
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def __str__(self):
        return f"brand:{self.brand} Year: {self.year}"


    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self,brand):
        if not brand:
            raise ValueError("brak marki ")
        else:
            self._brand = brand 
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,year):
        try:
            year = int(year)
        except ValueError:
            sys.exit("Nie podano roku")
        else:
            if year<1886 or year > 2026:
                raise ValueError("Niepoprawna data")
            else:
                self._year = year
          






def main():
    car = get_car()
    print(car)



def get_car():
    brand = input("Brand: ")
    year = input("Year: ")
    return Car(brand,year)


if __name__ == "__main__":
    main()