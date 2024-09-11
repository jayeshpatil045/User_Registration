import unittest
import user_registration 

class TestNameValidation(unittest.TestCase):

    def test_valid_name(self):
        """Test a valid name that starts with a capital letter and has at least 3 characters."""
        self.assertTrue(is_valid_first_name("Jayesh"))

    def test_invalid_name_lowercase(self):
        """Test a name that doesn't start with a capital letter."""
        self.assertFalse(is_valid_first_name("jayesh"))


if __name__ == "__main__":
    unittest.main()
