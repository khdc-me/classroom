###
# From a list, create a second list of only even elements from 1st in
#    1 line of code
###

my_list = [1, 4, 9, 16, 25, 36, 49, 50, 2, 100, 101, 105, 22]

even_nums_list = [num for num in my_list if num%2==0]

print(even_nums_list)
