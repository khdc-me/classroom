###
#   Program randomly generates 2 lists (rand_list_1, rand_list_2) and returns a
#        3rd list (common_values) of values that exist in both of generated lists
###

from random import randint

# Generate a list w/ a random size (limit of 100 elements)
#    - list contains only integers that are smaller than 50 (0 - 49)
def generate_new_list():
    return([randint(0, 49) for i in range(randint(0,99))])

# define lists
list_1 = generate_new_list()
list_2 = generate_new_list()
list_3 = list(set(list_1) & set(list_2))

print(list_1)
print(list_2)
print(list_3)

# "1-liner option"
print(list(set([randint(0,99) for i in range(randint(1,100))]) & set([randint(0,99) for i in range(randint(1,100))])))
