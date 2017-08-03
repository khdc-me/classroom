###
#    Program determines whether a given number (num) is odd or even
#    It alerts user if num is a multiple of 4
#    It determines if a second given number (factor) is a factor of the first
###

###
#    Get input from user
#        - Number to Test (num) if even or odd
#        - Number to Test (factor) if factor of num
###

# Get num
print("This program will indicate a number's parity (if even or odd).")
while True:
    try:
        num = int(input("Enter number whose parity you would like to test (must be a whole number): "))
    except ValueError:
        print("Error: This program only works w/ whole numbers. Please try again.\n")
        continue
    else:
        break

# Get factor
while True:
    try:
        factor = int(input("Enter number you to test if a factor of " + str(num) + ". Leave blank to ignore.") or False)
        
        if( factor == False ):
            # user does not care about checking if 2nd number is factor of 1st
            break
    except ValueError:
        print("Error: Number must be a whole number. Please try again.\n")
            
        continue
    else:
        # valid input
        break

# is num even; is num a multiple of 4
if( num % 2 == 0 ):
    output = str(num) + " is even"
    if( num % 4 == 0 ):
        output += " and a multiple of 4"
    output += "."
else:
    output = str(num) + " is odd."

# is 1st number (num) a multiple of the second (factor)
if factor:
    # user did provide a factor value
    output += "\n" + str(factor) + " is"
    output += " " if( num % factor == 0 ) else " not "
    output += "a factor of " + str(num) + "."
    
print (output)
