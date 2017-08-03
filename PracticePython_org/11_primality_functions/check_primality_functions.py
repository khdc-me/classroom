###
#   Program asks user for a number (num) and reports whether it is a prime
#        number or not
###

###
# Get a number from the user
###
def getNum():
    # Get num
    number = input("Please enter a number (integer that is greater than 0):\n")
    while (number.isnumeric() == False) or (int(number) < 1):
        # invalid input detected, reprompt user for input until valid input
        number = input("Error: The number you provide must be a whole number (1, 2, 3, etc) that is greater than 0: Please try again.\n")
    
    return number


###
# Determine if given number is a prime number or not
###
def isPrimeNum(n):
    # find all combination of factors
    factors = [[factor, int(n/factor)] for factor in range(1, int(n**0.5)+1) if n % factor == 0]
    
    # if more than one pair of factors, it is not a prime number
    return False if len(factors) > 1 else True

###
# Main Program
###
print("This program will tell you if a given number is a prime number or not.")
num = int(getNum())

# get number from user
if isPrimeNum(num):
    print(str(num) + " is a prime number.")
else:
    print(str(num) + " is not a prime number.")
