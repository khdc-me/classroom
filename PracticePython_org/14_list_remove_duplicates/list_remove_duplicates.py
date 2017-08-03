###
# Program takes a list and returns a new list that only contains the unique elements from the
#    first list (no duplicate values)
#    - must be done in loop (set() is now allowed)
###

my_list = [0, 0, 1, 1, 23, 23, 23, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9, 9, 9]


###
# create a list of unique values found in received (my_list) list
###
def createNewList(ml):
    new_list = []
    
    for val in ml:
        if val not in new_list:
            # new, unique value detected
            new_list.append(val)
    
    return new_list


###
# Main program
###
print(createNewList(my_list))
