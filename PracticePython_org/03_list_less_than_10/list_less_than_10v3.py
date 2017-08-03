###
#    This program takes a list, asks user for a number (num), creates a second list containing
#        values from the first list that are less than the value the user provided.
#    It then and prints out the created list
#
#    The very last line, does the same thing, but in a 1-line version
###

# list
my_list = [1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89]
my_lt10_list = []

while True:
    try:
        num = int(input("Please enter a number (must be integer): "))
    except ValueError:
        print("Error: Please provide a whole number.")
        continue
    else:
        break
    
for value in my_list:
    if value < num:
        my_lt10_list.append(value)

print("This was done in 14 lines of code:")
print(my_lt10_list)

# 1 liner option
print("\nThis was done in 1 line of code:\n" + str([value for value in [1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89] if value < num]))
