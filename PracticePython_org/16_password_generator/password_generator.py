#
#    password generator
#
#    This program will generate easy or hard password, depending on user input
#        - if user wants an easy password, a word will be randomly pulled from the 'passwords' list
#        - if user wants a hard password, the program will generate a sequence of characters that:
#            1) is of length between 10 and 25 characters long
#            2) contains at least 2 special characters (!, @, #, $, %, ^, &, *, -, _)
#            3) contains at least 2 numbers
#            4) contains at least 2 capital letters
#

from random import choice, randint
from string import digits, ascii_uppercase, ascii_lowercase


def get_desired_password_strength():
    '''
        Ask user if he/she would like to generate an easy or hard password.
        
        returns string
    '''
    desired_password_strength = input("Would you like to generate and (e)asy or (h)ard password?\n")
    while desired_password_strength.lower() not in ('e', 'h'):
        # invalid input detected
        desired_password_strength = input("Please enter an e to generate an easy password, or an h to generate a hard password.\n")
    
    return desired_password_strength.lower()


def get_easy_password():
    '''
        Randomly select element from password_list[] and return it
        
        returns string
    '''
    # easy password list
    password_list = ["test", "password", "easy", "trust", "thisisstillafairlyeasypasswordtoguess"]

    return choice(password_list)


def get_valid_chars(char_set='whole_set'):
    '''
        Return valid/allowed characters
            - accepted values: lowers, uppers, ints, specs, whole_set
            
        returns string
    '''
    specs = "!@#$%^&*-_"
    
    if char_set == 'lowers':
        #string of all lowercase characters [a-z]
        return ascii_lowercase
    elif char_set == 'uppers':
        # string of all uppercase characters [A-Z]
        return ascii_uppercase
    elif char_set == 'ints':
        # string of all number characters [0-9]
        return digits
    elif char_set == 'specs':
        # string of all allowed special characters
        return specs
    else:
        # string of all allowed characters [a-zA-Z0-9!@#$%^&*-_]
        return ascii_lowercase + ascii_uppercase + digits + specs


def get_password_length():
    '''
        Randomly generate an integer between 10 and 25 (inclusive), and return it
    
        returns int
    '''
    return randint(10, 25)


def is_hard_password(passwd):
    '''
        Check that received string 'passwd' meets the following characteristics:
            1) contains at least 2 special characters (!, @, #, $, %, ^, &, *, -, _)
            2) contains at least 2 numbers
            3) contains at least 2 capital letters
            
        return boolean
    '''
    is_hard = True     # assume hard password    
    # check for 2 special characters
    if len([i for i in passwd if i in get_valid_chars("specs")]) < 2:
        is_hard = False

    # check for 2 numbers
    if is_hard == True  and len([i for i in passwd if i in get_valid_chars("ints")]) < 2:
        is_hard = False
        
    # check for 2 uppercase letters
    if is_hard == True and len([i for i in passwd if i in get_valid_chars("uppers")]) < 2:
        is_hard = False
        
    return is_hard


def get_hard_password():
    '''
        Generate a string with random characters from valid_password_char_list[] that is between 10 and 25
            (inclusive) characters in length 
            
        return string
    '''    
    valid_password_char_list = get_valid_chars()
    
    # determine length
    passwd_length = get_password_length()
    
    hard_password = ''.join([choice(valid_password_char_list) for i in range(0, passwd_length)])
    while is_hard_password(hard_password) == False:
        # password is not hard, generate a new one and loop through until one that matches conditions is generated
        hard_password = ''.join([choice(valid_password_char_list) for i in range(0, passwd_length)])
    
    return hard_password


def main():
    # program body
    if get_desired_password_strength() == 'e':
        print(get_easy_password())
    else:
        # user wants to generate a hard password
        print(get_hard_password())


if __name__ == '__main__':
    main()
