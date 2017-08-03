import datetime

###
#    Program calculates year in which user will turn 100 years old. 
#    It asks user for first name (fname), current age (age), and a number (num).
#   It prints the output <num> number of times.
###

###
#    Get input from user
#        - First Name
#        - Current Age
#        - Number of times for output to be displayed on screen
###
print("This program calculates the year in which you will turn 100.")

# Get first name (fname)
while True:
    fname = input("What is your first name? (letters only, please)\n")
    if fname.isalpha():
        break
    else:
        print("Error: Only letters allowed.Please try again.\n")

print("Thank you, " + fname)
# Get age (age)
while True:
    try:
        age = int(input("What is your current age? (positive numbers only, please)\n"))
    except ValueError:
        print("Error: Only numbers greater than 0 allowed. Please try again.\n")
    else: 
        if( age > 0 ):
            break
        else:
            print("Error: Only numbers greater than 0 allowed. Please try again.\n")
        
# Get number (num)
while True:
    try:
        num = int(input("How many times would you like to see the answer? (positive numbers only, please)\n"))
    except ValueError:
        print("Error: Only numbers greater than 0 allowed. Please try again.\n")
        continue
    else:
        if( int(num) > 0):
            break
        else:
            print("Error: Only numbers greater than 0 allowed. Please try again.\n")

###
#    output num times (for loop from 0 to num)
#        "fname, you will turn 100 in ((100 - age)+cur_yr)."
###
# Get current year (cur_year)
cur_yr = datetime.datetime.now()
for i in range(num):
    if age > 100:
        print(fname + ", you turned 100 years old in " + str((cur_yr.year - (age - 100))))
    elif age < 100:
        print(fname + ", you will turn 100 years old in " + str(((100 - age) + cur_yr.year)))
    else:
        print(fname + ", you turn 100 years old this year!")
