
from Main_menu.contacts import Contact
import csv


class ContactDetailsError(Exception):
    pass


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class AddressBook(metaclass=SingletonMeta):
    def __init__(self):
        self.contacts = []
        self.load_from_file()

    def add_contact(self):
        first_name = input("Name*: ")
        last_name = input("Surname*: ")
        phone_number = input("Phone number*: ")
        address = input("Address: ")
        birthdate = input("Birthdate: ")
        if not first_name or not last_name or not phone_number:
            print("Name, Surname and Phone number must be filled.")
            return
        contact = Contact(first_name, last_name, phone_number, address, birthdate)
        self.contacts.append(contact)
        self.show_contact(contact)
        with open("/Users/admin/Desktop/Python/notebook-dm/src/Main_menu/data/contacts.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([contact.first_name, contact.last_name, contact.phone_number, contact.address, contact.birthday])

        print("Contact added successfully.")

    def remove_contact(self):
        phone_number = input("Enter phone number of the contact to remove: ")
        contact_removed = False
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.contacts.remove(contact)
                contact_removed = True
                print("Contact removed successfully.")
                break
        if not contact_removed:
            print("Contact not found.")
            return

        with open("/Users/admin/Desktop/Python/notebook-dm/src/Main_menu/data/contacts.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["first_name", "last_name", "phone_number", "address", "birthday"])
            for contact in self.contacts:
                writer.writerow(
                    [contact.first_name, contact.last_name, contact.phone_number, contact.address, contact.birthday])

    def show_contact(self, contact):
        print(contact)

    def edit_contact(self, contacts):
        print("Add name and surname which you want to edit")
        first_name = input("Name: ")
        last_name = input("Surname: ")
        contact_found = False
        for contact in contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                contact_found = True
                print(f"Contact found: {contact}")
                print("Add new information:")
                new_first_name = input("Name (Leave it empty if you don't want to change it): ")
                new_last_name = input("Surname (Leave it empty if you don't want to change it): ")
                new_phone_number = input("Phone number (Leave it empty if you don't want to change it): ")
                new_address = input("Address (Leave it empty if you don't want to change it): ")
                new_birth_date = input("Date of birth (Leave it empty if you don't want to change it): ")
                if new_first_name:
                    contact.first_name = new_first_name
                if new_last_name:
                    contact.last_name = new_last_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_address:
                    contact.address = new_address
                if new_birth_date:
                    contact.birth_date = new_birth_date

                print(f"Contact successfully updated: {contact}")
                self.save_to_file()
                break
        if not contact_found:
            raise ContactDetailsError(f"Contact {first_name} {last_name} not found.")

    def print_entry(self, entry):
        print("First name:", entry.first_name)
        print("Last name:", entry.last_name)
        print("Phone number:", entry.phone_number)
        print("Address:", entry.address)
        print("Date of birth:", entry.birthday)
        print()

    def search_by_name(self, contacts):
        name = input("Enter searching name: ").lower()
        results = []
        for entry in contacts:
            if entry.first_name.lower().startswith(name) or \
                    entry.last_name.lower().startswith(name) or \
                    entry.first_name.lower() == name or \
                    entry.last_name.lower() == name:
                results.append(entry)
        if results:
            print(f"Found {len(results)} contacts:")
            for entry in results:
                self.print_entry(entry)
        else:
            raise ContactDetailsError("Contacts not found.")

    def search_by_phone(self):
        phone_number = input("Enter phone number: ")
        for contact in self.contacts:
            if contact.phone_number == phone_number:
                self.show_contact(contact)
                break
        else:
            print(f"Contact with phone number {phone_number} not found.")

    def sort_by_name(self):
        self.contacts.sort(key=lambda x: x.first_name.lower())
        print("Sorted contacts:")
        for contact in self.contacts:
            print(contact)

    def sort_by_surname(self):
        self.contacts.sort(key=lambda contact: contact.last_name)
        print("Sorted contacts:")
        for contact in self.contacts:
            print(contact)

    def load_from_file(self):
        try:
            with open("/Users/admin/Desktop/Python/notebook-dm/src/Main_menu/data/contacts.csv", "r") as f:
                reader = csv.DictReader(f)
                self.contacts = [Contact(**row) for row in reader]
                print(f"Loaded {len(self.contacts)} records from file.")
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open("/Users/admin/Desktop/Python/notebook-dm/src/Main_menu/data/contacts.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["first_name", "last_name", "phone_number", "address", "birthdate"])
            for contact in self.contacts:
                writer.writerow(
                    [contact.first_name, contact.last_name, contact.phone_number, contact.address, contact.birthday])
        print("Contacts saved to file.")