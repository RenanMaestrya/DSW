class Agenda:
    def __init__(self):
        self.contacts = []  # List to store contacts

    def save_contact(self, name, phone, email):
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact["name"] != name]

    def search_person(self, name):
        indices = [i for i, contact in enumerate(self.contacts) if contact["name"] == name]
        return indices

    def print_agenda(self):
        for i, contact in enumerate(self.contacts):
            print(f"Contact {i+1}:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print()

    def detail_contact(self, index):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            print(f"Contact Details {index + 1}:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Invalid index.")
