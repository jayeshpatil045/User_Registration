import unittest
import user_registration 
from user_registration import is_valid_name

class TestNameValidation(unittest.TestCase):

    def test_valid_name(self):
        """Test a valid name that starts with a capital letter and has at least 3 characters."""
        self.assertTrue(is_valid_name("Jayesh","first"))
        self.assertTrue(is_valid_name("Patil","last"))

    def test_invalid_name_lowercase(self):
        """Test a name that doesn't start with a capital letter."""
        self.assertFalse(is_valid_name("jayesh","first"))
        self.assertFalse(is_valid_name("patil","last")) 

      


if __name__ == "__main__":
    unittest.main()
