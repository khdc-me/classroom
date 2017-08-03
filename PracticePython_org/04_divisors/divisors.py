###
#   Program asks user for a number (num) and calculates all factors of that num.
###

print("This program will find all factors for the number that you provide.")
# Get num
while True:
    try:
        num = int(input("Please enter a number (integer greater than 0): "))
        
        if num > 0:
            # input as expected
            break
        else:
            print("Error: Number must be a whole, positive number. Please try again: ")
            continue
    except ValueError:
        print("Error: Number must be a whole, positive number. Please try again: ")
        continue
    else:
        break

# Create list of factors
factors = range(1, num+1)
print("Factors of " + str(num) + ": " + str([factor for factor in factors if num % factor == 0]))
