###
# Program asks user for a string (my_string) and determines if it is a palindrome
###

# Get string from user
my_string = input("Please enter a string.\n")

##########
# 1st/preferred solution
##########
if my_string == my_string[::-1]:
    print("Is a palindrome.")
else:
    print("Is not a palindrome.")
    
    
##########
# 2nd solution (using reversed() method)
##########
if my_string == ''.join(reversed(my_string)):
    print("Is a palindrome.")
else:
    print("Is not a palindrome.")


##########
# 3rd solution (when slicing is strictly required)
##########
# Find halfway point
halfway_pt = int(len(my_string)/2) if len(my_string) % 2 == 0 else int((len(my_string)-1)/2)
                             
# Create 2 substrings
left_half = my_string[0:halfway_pt]
right_half = my_string[-1:halfway_pt:-1]

# Prepare output
if left_half == right_half:
    print("Is a palindrome.")
else:
    print("Is not a palindrome.")
