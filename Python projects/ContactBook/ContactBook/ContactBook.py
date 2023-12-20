contact = {}
def ShowFunction():
    print(contact.items())
    print("Name \t contact")
    for key in contact:
        print("{} \t {}".format(key, contact.get(key)))

while True:
    choice = int(input("1. Add New Contact.\n"
                       "2. Search the Contact.\n"
                       "3. Display the Contact.\n"
                       "4. Edit the Contact.\n"
                       "5. Delete the contact.\n"
                       "6. Exit the Contact.\n"
                       "Please Write Number between (1 - 6)  "))

    if choice == 1:
        name = input("Enter your Contact Name: ")
        phone = input("Enter your Phone Number: ")
        contact[name] = phone

    elif choice == 2:
        ContactName = input("Search the contact: ")
        if ContactName in contact:
            print(ContactName, "Contact number is ", contact[ContactName])
        else:
            print("Not found the contact")

    elif choice == 3:
        if not contact:
            print("Contact book is empty.")
        else:
            ShowFunction()


    elif choice == 4:
        EditContact = input("Edit your Contact: ")
        if EditContact in contact:
            phone = input("Change your number: ")
            contact[EditContact] = phone
            print("Contact updated successfully. ")
            ShowFunction()
        else:
            print("Name is not found!")

    elif choice == 5:
        Del_contact = input("which contact do you want to delete?: ")
        if Del_contact in contact:
            DeletedConfirm = input("do you want to delete contact? [y/n]")
            if DeletedConfirm == "y" or DeletedConfirm == "n":
                contact.pop(Del_contact)
            ShowFunction()
        else:
            print("The name is not found in contact book")

    else:
        print("Thank you for using ContactBook")
        break

