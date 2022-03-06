import unittest
from app.models import Comments

class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comments(
            "coding is thinking.", 
            "2022-o7-13T20:19:00Z", 
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

if __name__ == "__main__":
    unittest.main()