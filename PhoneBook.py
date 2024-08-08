import json
import re
import os


FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            if content.strip():  
                return json.loads(content)
            else:
                return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("email: ")
    
    
    if not re.match(r"^[0-9]{11}$", phone):
        print("Invalid contact number.(write it like : 09xxxxxxxxx or for example 021yyyyyyyy)")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email.")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("New contact added.")


def edit_contact(contacts):
    name = input("The name that you want to edit: ")
    for contact in contacts:
        if contact["name"] == name:
            print(f"Info: {contact}")
            new_phone = input("New number: ")
            
            if not re.match(r"^[0-9]{11}$", new_phone):
                print("Invalid contact number.(write it like : 09xxxxxxxxx or for example 021yyyyyyyy)")
                return
            
            new_email = input("New email: ")
            if not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                print("Invalid email.")
                return
            
            contact["phone"] = new_phone
            contact["email"] = new_email
            
            save_contacts(contacts)
            print("info updated.")
            return
    print("Not found.")


def delete_contact(contacts):
    name = input("The name that you want to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("contact deleted.")
            return
    print("Not found.")
    
    
def display_contacts(contacts):
    if not contacts:
        print("PhoneBook is empty.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def sort_contacts(contacts):
    contacts.sort(key=lambda x: x["name"])
    save_contacts(contacts)
    print("contact sorted.")
    for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")



def main():
    contacts = load_contacts()

    while True:
        print("PhoneBook")
        print("1.Add new contact")
        print("2.Edit contact")
        print("3.Delete contact")
        print("4.Show all contacts")
        print("5.Sort contacts")
        print("6.Exit")
        choice = input("Choose(1-6) :")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            sort_contacts(contacts)
        elif choice == '6':
            print("Done...")
            break
        else:
            print("Invalid...")
            
            
main()