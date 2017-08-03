###
#    This program takes a list and prints out all of the elements whose value is less than 10
###

# list
my_list = [1, 1, 2, 3, 5, 8, 13,21, 34, 55, 89]

output = ""
count = 0
for value in my_list:
    if value < 10:
        if count == 0:
            # 1st value to be printed
            output += "[" + str(value)
            
            count += 1
        else:
            output += ", " + str(value)
            
output += "]" if count > 0 else "List contains no values lower than 10."

print(output)
