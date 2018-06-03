import unittest #importing the unittest module
from contact import Contact
import pyperclip

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        setup method to run before each test cases.
        '''
        self.new_contact = Contact("Newton", "Karanu", "0714895623", "newton.karanu@moringaschool.com") #create new contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''

        self.assertEqual(self.new_contact.first_name, "Newton")
        self.assertEqual(self.new_contact.last_name,"Karanu")
        self.assertEqual(self.new_contact.number,"0714895623")
        self.assertEqual(self.new_contact.email,"newton.karanu@moringaschool.com")

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into the contact list
        '''
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    def test_contact_exists(self):
        '''
        test_contact_exists test case to check if we can return a boolean if we cannot find the contact.
        '''
        self.new_contact.save_contact()
        Test_contact = Contact("Test","user","0711223344","test@user.com")
        Test_contact.save_contact()

        contact_exists = Contact.contact_exists("0711223344")

        self.assertTrue(contact_exists)

    def tearDown(self):
        '''
        tearDown method that helps clean up after each test has run.
        '''
        Contact.contact_list = []

    def test_save_multiple_contacts(self):
        '''
        test_save_multiple_contacts test case to test if we can save multiple contact objects into our contact_list
        '''
        self.new_contact.save_contact()
        Test_contact = Contact("Test","user","0712345678","test@user.com")
        Test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    def test_delete_contact(self):
        '''
        test_delete_contact test case to test if we can remove a contact object from our contact list
        '''
        self.new_contact.save_contact()
        Test_contact = Contact("Test","user","0712345678","test@user.com")
        Test_contact.save_contact()

        self.new_contact.delete_contact() #deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)

    def test_find_contact_by_number(self):
        '''
        test_find_contact_by_number test case to test if we can find a contact object by phone number.
        '''
        self.new_contact.save_contact()
        Test_contact = Contact("Test","user","0712345678","test@user.com")
        Test_contact.save_contact()

        found_contact = Contact.find_by_number("0712345678")
        self.assertEqual(found_contact.email,Test_contact.email)

    def test_display_all_contacts(self):
        '''
        test_dislplay_all_contacts test case to test if we can be able to display all contacts
        '''

        self.assertEqual(Contact.display_contacts(),Contact.contact_list)

    def test_copy_email(self):
        '''
        test_copy_self test case to confirm that we are copying the email address from a found contact
        '''

        self.new_contact.save_contact()
        Contact.copy_email("0714895623")

        self.assertEqual(self.new_contact.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()