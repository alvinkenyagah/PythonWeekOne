import unittest
from user import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.new_person=Person("Alvin", "Alvin123")
    def test_init(self):
        self.assertEqual(self.new_person.username,"Alvin")
        self.assertEqual(self.new_person.password,"Alvin123")

    def test_save_user(self):
        self.new_person.saveUser()
        self.assertEqual(len(Person.person_list),1)
if __name__ =="__main__":
    unittest.main() 
        

