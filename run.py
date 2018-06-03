#!/usr/bin/env python3.6
from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    function to create a new contact
    '''

    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contact(contact):
    '''
    function to save contact that has been created
    '''

    contact.save_contact()

def del_contact(contact):
    '''
    function to delete contact that has been created
    '''

    contact.delete_contact()

def find_contact(number):
    '''
    function to find contact object based on phone number
    '''

    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    function that checks if a contact exists and returns a boolean value
    '''

    return Contact.contact_exists(number)

def display_contacts():
    '''
    function that returns all saved contacts
    '''

    return Contact.display_contacts()

def main():
    user_name = input("Hello, welcome to your contact list. What is your name? ")

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes: \n cc - create a new contact \n dc - display contacts \n fc - find a contact \n ex - exit the contact list app")

        short_code = input().lower()

        if short_code == 'cc':
            print('New Contact')
            print('-' * 10)

            f_name = input('First name...:')

            l_name = input('Last name...:')

            p_number = input('Phone number...:')

            e_address = input('Email address...: ')

            save_contact(create_contact(f_name,l_name,p_number,e_address)) #create and save new contact
            print('\n')
            print(f'New contact {f_name} {l_name} created')
            print('\n')

        elif short_code == 'dc':

            if display_contacts():
                print('Here is a list of all your contacts')
                print('\n')

                for contact in display_contacts():
                    print(f'{contact.first_name} {contact.last_name} ......{contact.phone_number}')

                print('\n')
            else:
                print('\n')
                print('You don\'t seem to have any contact saved yet')
                print('\n')

        elif short_code == 'fc':

            search_number = input('Enter the number you want to search for:')

            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f'{search_contact.first_name} {search_contact.last_name}')
                print('-' * 20)

                print(f'Phone number...... {search_contact.phone_number} \n Email address...... {search_contact.email}')

            else:
                print('That contact does not exist')

        elif short_code == 'ex':
            print('Bye..... It was fun while it lasted.... :-)')
            break

        else:
            print('I really didn\'t get that. Please use the short codes')

if __name__ == '__main__':

    main()