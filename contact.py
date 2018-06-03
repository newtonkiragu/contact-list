import pyperclip
class Contact:
    """
    class that generates new instances of contacts
    """

    contact_list = [] #empty contact list

    def __init__(self,first_name,last_name,number,email):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name
            last_name: New contact last name
            number: New contact phone number
            email: New contact email
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def save_contact(self):
        '''
        save_contact method saves contact object into contact list
        '''
        Contact.contact_list.append(self)

    def delete_contact(self):
        '''
        delete_contact method removes a saved contact object from contact list
        '''
        Contact.contact_list.remove(self)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.
        
        Args:
            number: Phone number to search for
        Returns:
            contact of person that matches that number.
        '''

        for contact in cls.contact_list:
            if contact.number == number:
                return contact
    
    @classmethod
    def contact_exists(cls,number):
        '''
        Method that confirms if a contact exists from the contact list.

        Args:
            number:Phone number to search if it exists
        Returns:
            boolean: true or false depending if the contact exists
        '''

        for contact in cls.contact_list:
            if contact.number == number:
                return True

        return False

    @classmethod
    def display_contacts(cls):
        '''
        Method that returns the contact list
        '''

        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)