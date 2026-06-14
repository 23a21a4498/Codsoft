contacts = {}

while True:
    print("\n CONTACT BOOK ")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = str(input("Name: "))
        phone = int(input("Phone: "))
        email = input("Email: ")
        address = input("Address: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        for name, details in contacts.items():
            print(f"\nName: {name}")
            print("Phone:", details["Phone"])

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter contact name to update: ")
        if name in contacts:
            contacts[name]["Phone"] = input("New Phone: ")
            contacts[name]["Email"] = input("New Email: ")
            contacts[name]["Address"] = input("New Address: ")
            print("Contact Updated!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")