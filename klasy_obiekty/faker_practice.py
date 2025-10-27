from faker import Faker

fake = Faker('pl_PL')  # polska lokalizacja

for _ in range(5):
    imie_nazwisko = fake.name()
    adres = fake.address()
    telefon = fake.phone_number()
    email = fake.email()
    print("Wizytówka:")
    print(f"Imię i nazwisko: {imie_nazwisko}")
    print(f"Adres: {adres}")
    print(f"Telefon: {telefon}")
    print(f"Email: {email}")
    print("-" * 40)
