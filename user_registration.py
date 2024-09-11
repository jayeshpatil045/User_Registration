'''

@Author: Jayesh Patil
@Date: 2024-09-11
@Last Modified by: Jayesh Patil
@Title: user_registration Problem


'''
import re
import unittest
import logger

logger = logger.logger_init('user_registration')

def is_valid_name(name,name_type):
    """
        Description:
            Validates if the given first name and last name starts with a capital letter and has a minimum of 3 characters.
    
            The function uses a regular expression to ensure that the name:
            - Starts with an uppercase letter (A-Z).
            - Contains at least 3 alphabetic characters.

        Parameters:
            name (str): The name (first or last) input by the user.
            name_type (str): Specifies whether it's a first name or last name for logging purposes.

        Returns:
            True if the name is valid, False otherwise.
    """
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    if re.match(pattern, name):
        logger.info(f"Valid {name_type} name entered: {name}")
        return True
    else:
        logger.error(f"Invalid {name_type}: {name}. It should start with a capital letter and be at least 3 characters long.")
        return False
def is_valid_email(email):
    """
        Description:
            Validates the email based on the given format.
            Mandatory parts: abc, bl, co
            Optional parts: xyz, in
            Example: abc.xyz@bl.co.in
        Parameters:  
            email (str): The email input by the user. 
            
        Returns:
            True if the name is valid, False otherwise.     
            
    """
    pattern = r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$"
    if re.match(pattern, email):
        logger.info(f"Valid email entered: {email}")
        return True
    else:
        logger.error(f"Invalid email: {email}. Email should follow the format abc.xyz@bl.co.in")
        return False


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    
    valid_first_name = is_valid_name(first_name,"first")
    valid_last_name = is_valid_name(last_name,"Last")
    valid_email = is_valid_email(email)
    
    if valid_first_name and valid_last_name and valid_email:
        logger.info(f"User successfully registered with First Name: {first_name} and Last Name: {last_name} and email : {email}")
    else:
        logger.error(f"Registration failed due to invalid inputs.")    


if __name__ == "__main__":
   main()

