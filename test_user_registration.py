import unittest
from user_registration import is_valid_name ,is_valid_email

class TestNameValidation(unittest.TestCase):

    def test_valid_name(self):
        """Test a valid name that starts with a capital letter and has at least 3 characters."""
        self.assertTrue(is_valid_name("Jayesh","first"))
        self.assertTrue(is_valid_name("Patil","last"))

    def test_invalid_name_lowercase(self):
        """Test a name that doesn't start with a capital letter."""
        self.assertFalse(is_valid_name("jayesh","first"))
        self.assertFalse(is_valid_name("patil","last"))

    def test_valid_email(self):
        """Test a valid email format."""
        self.assertTrue(is_valid_email("abc.xyz@bl.co.in"))

    def test_invalid_email_missing_at(self):
        """Test an email missing the @ symbol."""
        self.assertFalse(is_valid_email("abc.xyzbl.co.in"))

    def test_invalid_email_missing_domain(self):
        """Test an email with no domain part after @."""
        self.assertFalse(is_valid_email("abc@.co.in"))

    def test_invalid_email_extra_dot(self):
        """Test an email with an extra dot."""
        self.assertFalse(is_valid_email("abc..xyz@bl.co.in"))
     

      


if __name__ == "__main__":
    unittest.main()
