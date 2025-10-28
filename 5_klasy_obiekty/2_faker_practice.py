from faker import Faker #import biblioteki Faker

fake = Faker('pl_PL') # polska lokalizacja

class biz_card: #klasa wizytówka
    def __init__(self, imie_i_nazwisko, adres, telefon, email): #konstruktor klasy
        self.imie_i_nazwisko=fake.name()
        self.adres=fake.address().replace('\n', ' ') #tu misiałem usunąć znak nowej linii ponieważ adresy mogą mieć wiele linii i tak jest generowane
        self.telefon=fake.phone_number()
        self.email=fake.email()
        # powyzsze atrybuty klasy biz_card po polsku dla lepszej czytelności bo mi się mieszają 

# Lista wizytówek
business_cards = [] #utworzona pusta lista na wizytówki

for _ in range(5): 
    wiz = biz_card(imie_i_nazwisko=fake.name(), adres=fake.address(), telefon=fake.phone_number(), email=fake.email()) #tworzenie wizytówki
    business_cards.append(wiz) #dodanie wizytówki do listy

# Wyświetlanie w jednej linii: imię, nazwisko, adres, telefon, email
for wiz in business_cards: # iteracja przez listę wizytówek
    print(f"{wiz.imie_i_nazwisko} - {wiz.telefon} - {wiz.adres} - {wiz.email}")
    print("-" * 40)
