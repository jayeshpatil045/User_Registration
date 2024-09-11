import unittest
from user_registration import is_valid_name ,is_valid_email,is_valid_mobile,is_valid_password

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
     
    def test_valid_mobile(self):
        """Test a valid mobile number format."""
        self.assertTrue(is_valid_mobile("91 9919819801"))

    def test_invalid_mobile_no_country_code(self):
        """Test an invalid mobile number without the country code."""
        self.assertFalse(is_valid_mobile("9919819801"))

    def test_invalid_mobile_no_space(self):
        """Test an invalid mobile number without space after country code."""
        self.assertFalse(is_valid_mobile("919919819801"))

    def test_invalid_mobile_too_short(self):
        """Test an invalid mobile number with less than 10 digits."""
        self.assertFalse(is_valid_mobile("91 99198198"))
        
    def test_valid_password(self):
        """Test a valid password with at least 8 characters and one uppercase letter."""
        self.assertTrue(is_valid_password("Password123"))

    def test_invalid_password_too_short(self):
        """Test an invalid password that is shorter than 8 characters."""
        self.assertFalse(is_valid_password("Pass1"))

    def test_invalid_password_no_uppercase(self):
        """Test an invalid password that has no uppercase letter."""
        self.assertFalse(is_valid_password("password123"))

    def test_invalid_password_no_uppercase_and_short(self):
        """Test an invalid password that is shorter than 8 characters and has no uppercase letter."""
        self.assertFalse(is_valid_password("pass1"))          
      


if __name__ == "__main__":
    unittest.main()
