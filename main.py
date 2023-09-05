contact={}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.Add new contact \n2.Search Contact \n3.Display contacts \n4.Update/Edit contact \n5.Delete contact\n6.Exit\nEnter your choice: "))
    if choice==1:
        name=input("Enter the contact name: ")
        phone=int(input("Enter the contact number: "))
        contact[name]=phone

    elif choice==2:
        search_name=input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in the contact book.")

    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()

    elif choice==4:
        update_contact=input("Enter the contact name to be edited: ")
        if update_contact in contact:
            phone=int(input("Enter the mobile number: "))
            contact[update_contact]=phone
            print("Contact updated successfully.")
            display_contact()

        else:
            print("Name is not found in the contact book.")

    elif choice==5:
        del_contact=input("Enter the contact name to be deleted: ")
        if del_contact in contact:
            confirm_contact=input("Do you want to delete this contact? (y/n)")
            if confirm_contact=="y"or confirm_contact=="Y":
                contact.pop(del_contact)
                display_contact()
                print("Contact deleted successfully.")
            elif confirm_contact=="n" or confirm_contact== "N":
                display_contact()
                print("Okay contact is not deleted")

        else:
            print("Name is not found in the contact book.")

    else:
        break





