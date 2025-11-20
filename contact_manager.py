# ---------------------------------------------
# Name: ISHIKA GROVER
# Date: 14-11-2025
# Project: Contact Book Manager
# ---------------------------------------------
print("""
========================================
       WELCOME TO CONTACT BOOK MANAGER
========================================

Manage your contacts easily:
- Add, view, search, update, delete contacts
- Save and load data using CSV & JSON
- Simple and beginner-friendly interface

Let's begin!
""")

# Task 2 — Create & Save Contacts (CSV)
import csv

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {"name": name, "phone": phone, "email": email}

    try:
        with open("contacts.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email])
        print("Contact saved successfully!\n")

    except Exception as e:
        print("Error saving contact:", e)


# Task 3 — Read & Display Contacts
def display_contacts():
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

            if not contacts:
                print("Contact list is empty.\n")
                return

            print("\nName\t\tPhone\t\tEmail")
            print("-----------------------------------------------")
            for c in contacts:
                print(f"{c[0]}\t\t{c[1]}\t\t{c[2]}")
            print()

    except FileNotFoundError:
        print("contacts.csv not found. Add contacts first.\n")

# Task 4 — Search, Update, Delete Contacts

def search_contact(name):
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == name.lower():
                    print("Contact Found:")
                    print("Name:", row[0])
                    print("Phone:", row[1])
                    print("Email:", row[2], "\n")
                    return row
        print("Contact not found.\n")
    except Exception as e:
        print("Error:", e)

def update_contact(name):
    contacts = []

    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        updated = False
        for c in contacts:
            if c[0].lower() == name.lower():
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                c[1] = new_phone
                c[2] = new_email
                updated = True

        if updated:
            with open("contacts.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Contact not found.\n")

    except Exception as e:
        print("Error:", e)

def delete_contact(name):
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        new_list = [c for c in contacts if c[0].lower() != name.lower()]

        with open("contacts.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_list)

        print("Contact deleted successfully!\n")

    except Exception as e:
        print("Error:", e)
    
# Task 5 — Save & Load Contacts in JSON
import json

def export_to_json():
    data = []
    try:
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append({"name": row[0], "phone": row[1], "email": row[2]})

        with open("contacts.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print("Contacts exported to contacts.json\n")

    except Exception as e:
        print("Error exporting:", e)

def load_from_json():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        print("\nContacts from JSON:")
        print("Name\tPhone\tEmail")
        print("--------------------------------------")
        for c in contacts:
            print(f"{c['name']}\t{c['phone']}\t{c['email']}")
        print()

    except Exception as e:
        print("Error loading JSON:", e)


# Task 6  — Error Logging
import datetime

def log_error(message, operation):
    with open("error_log.txt", "a") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"Time: {timestamp}\n")
        log.write(f"Operation: {operation}\n")
        log.write(f"Error: {message}\n")
        log.write("----------------------------------\n")

# ---------------------- MAIN MENU ----------------------
while True:
    print("""
===========================
        MAIN MENU
===========================
1. Add Contact
2. Display Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Export to JSON
7. Load from JSON
8. Exit
===========================
""")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        display_contacts()

    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "4":
        name = input("Enter name to update: ")
        update_contact(name)

    elif choice == "5":
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == "6":
        export_to_json()

    elif choice == "7":
        load_from_json()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.\n")
1