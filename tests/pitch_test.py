import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(
            "We compete in the growing defined market.", 
            "Business Pitches", 
            "2021-12-13T20:19:00Z", 
            0,
            0, 
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

if __name__ == "__main__":
    unittest.main()