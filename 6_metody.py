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
        # Zwraca długość imienia i nazwiska z uwzględnieniem spacji pomiędzy nimi
        return len(f"{self.first_name} {self.last_name}")


# Przykładowe użycie:
contacts = [
    Contact("Jan", "Kowalski", "jan.kowalski@example.com", "Inżynier"),
    Contact("Anna", "Nowak", "anna.nowak@example.com", "HR Specialist"),
    Contact("Piotr", "Wiśniewski", "piotr.wisniewski@example.com", "Developer"),
    Contact("Maria", "Zielińska", "maria.zielinska@example.com", "Manager"),
    Contact("Tomasz", "Wójcik", "tomasz.wojcik@example.com", "Sprzedawca")
]

# Wyświetlenie kontaktów
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
print("Sortowanie po imieniu:")
for contact in contacts_by_first_name:
    print(contact)