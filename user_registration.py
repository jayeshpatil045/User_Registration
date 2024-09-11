'''

@Author: Jayesh Patil
@Date: 2024-09-11
@Last Modified by: Jayesh Patil
@Title: user_registration Problem


'''
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_first_name(first_name):
    """
        Description:
            Validates if the given first name starts with a capital letter and has a minimum of 3 characters.
    
            The function uses a regular expression to ensure that the name:
            - Starts with an uppercase letter (A-Z).
            - Contains at least 3 alphabetic characters.

        Parameters:
            name (str): The first name input by the user.

        Returns:
            True if the name is valid, False otherwise.
    """
    pattern = r"^[A-Z][a-zA-Z]{2,}$"
    if re.match(pattern, first_name):
        logging.info(f"Valid first name entered: {first_name}")
        return True
    else:
        logging.error(f"Invalid first name: {first_name}. It should start with a capital letter and be at least 3 characters long.")
        return False

def main():
    first_name = input("Enter your first name: ")
    is_valid_first_name(first_name)
if __name__ == "__main__":
   main()

