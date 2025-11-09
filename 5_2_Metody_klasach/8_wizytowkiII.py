from faker import Faker

class BaseContact:
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"

    def contact(self):
        print(f"Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

class BusinessContact(BaseContact):
    def __init__(self, first_name, last_name, private_phone, email, position, company, business_phone):
        super().__init__(first_name, last_name, private_phone, email)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer służbowy {self.business_phone} i dzwonię do {self.first_name} {self.last_name}")

def create_contacts(card_type, how_many):
    fake = Faker('pl_PL')
    contacts = []
    for _ in range(how_many):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        private_phone = fake.phone_number()
        if card_type == BaseContact:
            contact = BaseContact(first_name, last_name, private_phone, email)
        elif card_type == BusinessContact:
            position = fake.job()
            company = fake.company()
            business_phone = fake.phone_number()
            contact = BusinessContact(first_name, last_name, private_phone, email, position, company, business_phone)
        else:
            raise ValueError("Podaj BaseContact lub BusinessContact!")
        contacts.append(contact)
    return contacts

if __name__ == "__main__":
    business_cards = create_contacts(BusinessContact, 5)
    for card in business_cards:
        print(card)
        card.contact()
        print(f"Długość etykiety: {card.label_length}\n")

    print("--- Wersja prywatnych kontaktów ---\n")
    private_cards = create_contacts(BaseContact, 5)
    for card in private_cards:
        print(card)
        card.contact()
        print(f"Długość etykiety: {card.label_length}\n")
