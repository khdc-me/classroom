###
#   Program asks user how many Fibonnaci numbers to generate
#        - gets number (num) from user (integer that is greater than 0)
#        - generates Fibonnaci sequence up to num
#        - Fibonnaci sequence is one where next number is sum of previous 2 numbers (ie: 0, 1, 1, 2, 3, 5, 6, ...)
#            NOTE: 1st two numbers in sequence will always be 0, 1
###

###
# prompt user for number
###
def getNum():
    num = input("How many numbers would you like to see in the Fibonnaci sequence (number must be greater than 0)?\n")
    while ( num.isnumeric()==False ) or (int(num)<0):
        num = input("Error: You must enter an integer that is greater than 0. Please try again.\n")
        
    return int(num)


###
# Generate Fibonnaci sequence
###
def getSequence(n):
    # sequence always starts w/ 0 and 1
    sequence = [0, 1]
    
    # only iterate if n is 2 or higher
    if n >= 2:
        for i in range(2, n):
            # insert new values
            sequence.append(sequence[-1]+sequence[-2])        
    
    return sequence[0:n]
    
    
###
# Main program
###
# prompt user for number
num = getNum()

print(getSequence(num))
