from faker import Faker
from datetime import datetime # importowanie klasy datetime z modułu datetime

# Dekorator mierzący czas wykonania funkcji
def time_it(func):
    def dekor(*args, **kwargs):
        start_time = datetime.now()  # Pobranie aktualnego czasu przed wykonaniem funkcji
        result = func(*args, **kwargs)  # Wywołanie oryginalnej funkcji
        end_time = datetime.now()  # Pobranie aktualnego czasu po wykonaniu funkcji
        duration = end_time - start_time  # Obliczenie różnicy czasu
        print(f"Czas wykonania funkcji '{func.__name__}': {duration.total_seconds()} sekund")
        print()
        print("Poniżej kikla przykładowych wizytówek:")
        print("-" * 40)
        return result
    return dekor

# Wizytówka
class BusinessCard:
    def __init__(self, name, company, job_title, email, phone):
        self.name = name
        self.company = company
        self.job_title = job_title
        self.email = email
        self.phone = phone
    def __str__(self):
        return (f"Imię: {self.name}\n"
                f"Firma: {self.company}\n"
                f"Stanowisko: {self.job_title}\n"
                f"Email: {self.email}\n"
                f"Telefon: {self.phone}")

# Generujemy wizytówki
@time_it # dekorator mierzący czas wykonania
def generate_business_cards(n=1000):
    fake = Faker("pl_PL")
    contacts = []
    for _ in range(n):
        contacts.append(BusinessCard(
            name=fake.name(),
            company=fake.company(),
            job_title=fake.job(),
            email=fake.email(),
            phone=fake.phone_number()
        ))
    return contacts

# wywołanie funkcji
contacts = generate_business_cards()
for contact in contacts[:5]:  # wyświetlamy pierwsze 5 wizytówek
    print(contact)
    print("-" * 30)
    # dowolny tekst 