from faker import Faker

class Contact:
    def __init__(self, first_name, last_name, email, position):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def contact(self):
        print(f"Kontaktuję się z {self.first_name} {self.last_name}, {self.position} ({self.email})")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

# Inicjalizacja generatora Faker
fake = Faker('pl_PL')

# Automatyczne generowanie listy kontaktów:
contacts = []
for _ in range(10):    # ilość wygenerowanych kontaktów
    contacts.append(Contact(
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        fake.job()
    ))

# Przykładowe użycie
for contact in contacts:
    print(contact)
    contact.contact()
    print(f"Długość etykiety (label_length): {contact.label_length}\n")

# Sortowanie po imieniu
contacts_by_first_name = sorted(contacts, key=lambda c: c.first_name)
# Sortowanie po nazwisku
contacts_by_last_name = sorted(contacts, key=lambda c: c.last_name)
# Sortowanie po mailu
contacts_by_email = sorted(contacts, key=lambda c: c.email)
