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