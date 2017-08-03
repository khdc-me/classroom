###
#   Program creates a list that consists of the first and last elements of a given list of numbers
###

# initial list
my_list = [5, 10, 15, 20, 25]


###
# Receives a list and confirm that all elements are integers
###
def isValidList(l):
    return all(isinstance(elem, int) for elem in l)


###
# Create second list from 1st and last elements in given list
###
def createNewList(l):
    # check list length
    if len(l) > 1:
        return [l[0], l[-1]]
    else:
        # only 1 element, return original list
        return l
        

###
# Main Program
###
if isValidList(my_list):
    # all list elements are integers
    #create new list & output confirmation
    new_list = createNewList(my_list)
    print("new_list: " + str(new_list))
else:
    # invalid list (non-integer value detected)
    print("Error: All values in list must be integers. At least 1 element/value is not.")
