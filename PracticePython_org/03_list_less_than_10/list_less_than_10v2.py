###
#    This program takes a list, creates a second list containing values from
#        the first list that are less than 10, and prints out the list
#
#    The very last line, does the same thing, but in a 1-line version
###

# list
my_list = [1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89]
my_lt10_list = []

for value in my_list:
    if value < 10:
        my_lt10_list.append(value)

print("This was done in 14 lines of code:")
print(my_lt10_list)

# 1 liner option
print("\nThis was done in 1 line of code:\n" + str([value for value in [1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89] if value < 10]))
