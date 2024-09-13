import pytest
from user_registration import is_valid_name, is_valid_email, is_valid_mobile, is_valid_password

def test_valid_name():
    """Test a valid name that starts with a capital letter and has at least 3 characters."""
    assert is_valid_name("Jayesh", "first") == True
    assert is_valid_name("Patil", "last") == True

def test_invalid_name_lowercase():
    """Test a name that doesn't start with a capital letter."""
    assert is_valid_name("jayesh", "first") == False
    assert is_valid_name("patil", "last") == False

def test_valid_email():
    """Test a valid email format."""
    assert is_valid_email("abc.xyz@bl.co.in") == True
    assert is_valid_email("abc@yahoo.com") == True
    assert is_valid_email("abc-100@yahoo.com") == True
    assert is_valid_email("abc.100@yahoo.com") == True
    assert is_valid_email("abc111@abc.net") == True
    assert is_valid_email("abc111@abc.com") == True
    assert is_valid_email("abc.100@abc.com.au") == True
    assert is_valid_email("abc@gmail.com.com") == True
    assert is_valid_email("abc+100@gmail.com") == True

def test_invalid_email():
    """Test a invalid email"""
    assert is_valid_email("abc") == False 
    assert is_valid_email("abc@.com.my") == False 
    assert is_valid_email("abc123@.com") == False 
    assert is_valid_email("abc123@.com.com") == False 
    assert is_valid_email(".abc@abc.com") == False 
    assert is_valid_email("abc()*@gmail.com") == False 
    assert is_valid_email("abc@%*.com") == False 
    assert is_valid_email("abc..2002@gmail.com") == False 
    assert is_valid_email("abc.@gmail.com") == False 
    assert is_valid_email("abc@abc@gmail.com") == False 
    assert is_valid_email("abc@gmail.com.1a") == False 
    assert is_valid_email("abc@gmail.com.aa.au") == False

def test_valid_mobile():
    """Test a valid mobile number format."""
    assert is_valid_mobile("91 9370543097") == True

def test_invalid_mobile_():
    """Test an invalid mobile number """
    assert is_valid_mobile("9919819801") == False
    assert is_valid_mobile("919919819801") == False
    assert is_valid_mobile("91 937054309") == False

def test_valid_password():
    """Test a valid password with at least 8 characters, one uppercase letter, one numeric digit, and exactly one special character."""
    assert is_valid_password("Password1@") == True

def test_invalid_password():
    """Test an invalid password ."""
    assert is_valid_password("Pass1@") == False
    assert is_valid_password("password1@") == False
    assert is_valid_password("Password@") == False
    assert is_valid_password("Password123") == False
    assert is_valid_password("Password1@#") == False

if __name__ == "__main__":
    pytest.main()    
