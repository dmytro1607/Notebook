from Main_menu.helpers import AddressBook

address_book = AddressBook()

while True:
    print('Menu:')
    print('1 - Add contact')
    print('2 - Delete contact')
    print('3 - Change contact')
    print('4 - Search by phone number')
    print('5 - Search by name')
    print('6 - Sorting by name')
    print('7 - Sorting by surname')
    print('8 - Exit')

    choice = input('Make your choice > ')
    match choice:
        case '1':
            AddressBook().add_contact()
        case '2':
            AddressBook().remove_contact()
        case '3':
            AddressBook().edit_contact(address_book.contacts)
        case '4':
            AddressBook().search_by_phone()
        case '5':
            AddressBook().search_by_name(address_book.contacts)
        case '6':
            AddressBook().sort_by_name()
        case '7':
            AddressBook().sort_by_surname()
        case '8':
            AddressBook().save_to_file()
            print('GoodBye!')
            break
        case _:
            print("Invalid choice, please try again.")
