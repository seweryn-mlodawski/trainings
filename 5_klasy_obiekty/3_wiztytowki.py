from faker import Faker # import biblioteki Faker

fake = Faker('pl_PL')

class BizCard:
    def __init__(self): # konstruktor klasy
        full_name = fake.name().split() # generowanie pełnego imienia i nazwiska
        self.imie = full_name[0] # pierwsza część jako imię
        self.nazwisko = full_name[-1] # ostatnia część jako nazwisko
        self.email = fake.email() # generowanie e-maila

    def __str__(self): # metoda do reprezentacji obiektu jako string
        return f"{self.imie} {self.nazwisko}, {self.email}" 

class Part:
    def __init__(self):
        self.part_name = fake.word().capitalize()
        self.part_number = fake.ean13()
        self.category = fake.color_name()

    def __str__(self):
        return f"{self.part_name} ({self.category}) - {self.part_number}" 

# Tworzenie listy wizytówek
business_cards = [BizCard() for _ in range(5)] # tworzenie 5 wizytówek

print("Wizytówki:")
for wiz in business_cards:
    print(wiz)

# Sortowanie
print("\nSortowanie według imienia:")
for wiz in sorted(business_cards, key=lambda x: x.imie):
    print(wiz)

print("\nSortowanie według nazwiska:")
for wiz in sorted(business_cards, key=lambda x: x.nazwisko):
    print(wiz)

print("\nSortowanie według e-maila:")
for wiz in sorted(business_cards, key=lambda x: x.email):
    print(wiz)

# Tworzenie listy części
parts = [Part() for _ in range(5)]

print("\nCzęści:")
for p in parts:
    print(p)

# sortowanie
print("\nSortowanie według nazwy części:")
for p in sorted(parts, key=lambda x: x.part_name):
    print(p)

print("\nSortowanie według numeru części:")
for p in sorted(parts, key=lambda x: x.part_number):
    print(p)

print("\nSortowanie według kategorii:")
for p in sorted(parts, key=lambda x: x.category):
    print(p)

    # tworzenie listy pracowników
    employees = [Part() for _ in range(5)]

    print("\nPracownicy i pracownice:")
    for e in employees:
        print(e)

    # sortowanie
    print("\nSortowanie według imienia:")
    for e in sorted(employees, key=lambda x: x.imie):
        print(e)

        # tylko pod komita
        