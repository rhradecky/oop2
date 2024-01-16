'''
class MojaKalkulacka:
    @staticmethod
    def sucet(a,b):
        return a + b
    def sucin(a,b):
        return a*b

print(MojaKalkulacka.sucet(2,2))
print(MojaKalkulacka.sucin(2,3))



class Zviera:
    def hlas(self):
        raise NotImplementedError("Podtrieda musi  bla bla")

class Pes(Zviera):
    def hlas(self):
        return "Haf"

class Kohut(Zviera):
    def hlas(self):
        return "kikirikik"

class Macka(Zviera):
    def hlas(self):
        return "Mnau"

def vydaj_zvuk(zviera):
    return zviera.hlas()

pes = Pes()
macka = Macka()
kohut = Kohut()

for zviera in [pes, macka, kohut]:
    print(vydaj_zvuk(zviera))



class Zviera:
    def nohy(self):
        raise NotImplementedError("Podtrieda musi  bla bla")

class Pes(Zviera):
    def nohy(self):
        return "4"

class Kohut(Zviera):
    def nohy(self):
        return "2"

class Macka(Zviera):
    def nohy(self):
        return "4"


def pocet_noh(zviera):
    return zviera.nohy()

pes = Pes()
macka = Macka()
kohut = Kohut()

for zviera in [pes, macka, kohut]:
    print("zviera ma", pocet_noh(zviera), "nohy")



class Stadion:
    def __init__(self, stadion_name, date_of_opening, country,city,  seating_capacity):
        self.stadion_name = stadion_name
        self.date_of_opening = date_of_opening
        self.country = country
        self.city = city
        self.seating_capacity = seating_capacity


    def stadiony(self):
        print(f"Nazov stadiona: {self.stadion_name}   datum otvorenia: {self.date_of_opening}   Krajina: {self.country} Mesto: {self.city}   Pocet sedadiel: {self.seating_capacity}")


bratislava = Stadion( "Stadion x", "2008", "Slovensko","Bratislava", 20000)
kosice = Stadion( "Stadion y", "2008", "Slovensko","Kosice", 1000)
trnava = Stadion( "Stadion z", "1999", "Slovensko","Trnava", 5000)
banska = Stadion( "Stadion w", "2018", "Slovensko","Banska Bystrica", 8000)
trencin = Stadion( "Stadion H", "2011", "Slovensko","Trencin", 9000)






stadiony = [bratislava, kosice, trnava, banska, trencin]
stadiony.sort(key=lambda i: i.seating_capacity, reverse=True)
print("asd")
print(stadiony[0].stadion_name)




#najvatsi_stadion = None
#najvatsia_kapacita = 0

#for i in [bratislava, kosice, trnava, banska, trencin]:
#    if i.seating_capacity > najvatsia_kapacita
#        najvatsia_kapacita = i.seating_capacity
#        najvatsi_stadion = i

#print(najvatsi_stadion)







class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __len__(self):
        return self.capacity

    def __add__(self, other):
        return Stadium(self.name + " " + other.name, self.capacity + other.capacity)

    def __eq__(self, other):
        return self.name == other.name and self.capacity == other.capacity


stadium1 = Stadium("Etihad Stadium", 11222)
stadium2 = Stadium("Etihad Stadium", 11222)

print(stadium1)
print(stadium2)
if stadium1 == stadium2:
    print("rovnaky")
else:
    print("rozny")

'''


class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price is negative")


kniha = Book("Harry Potter", 400, 10)
print(kniha.price)
kniha.price = 20
print(kniha.price)
kniha.price = -10
