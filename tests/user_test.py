import unittest
from app.models import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            "John", 
            "Doe", 
            "johndoe@gmail.com", 
            "johndoe2340143", 
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))
    
    def test_password(self):
        self.assertTrue(self.new_user.password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('johndoe2340143'))

if __name__ == "__main__":
    unittest.main()