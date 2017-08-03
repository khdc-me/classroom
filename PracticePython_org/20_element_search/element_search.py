#
#    detect if value in list via binary search
#
#    A binary search takes a sorted list and chops it up by half in each iteration where value
#        is not found, until only 1 element remains.
#        - es: searching for 8 in [0,1,2,3,4,5,6,7,8,9]
#                - if even number of elements, middle will land between 2 elements, round down
#                - is 8 larger than 5? Yes, disregard all elements that are less than 6: 0 - 5
#                - repeat for remaining range [5,6,7,8,9]
#


def check_value_found(numeric_list, num):
    '''
        conduct binary search for num in numeric_list
    '''
    # determine mid-point index
    low_i = 1
    high_i = len(numeric_list)-2
    
    execute_binary_search = True
    while execute_binary_search:
        # declare mid point index
        mid_pt_i = (high_i + low_i) // 2
        mid_pt_elem = numeric_list[mid_pt_i]
        
        if not str(mid_pt_elem).isnumeric():
            # Error: string found inside of list
            raise ValueError("String found. Expecting list of numeric values.")
        else:
            # No strings found so far
            
            if high_i < low_i:
                # binary search concluded w/out finding num
                return False
            else:
                # continue to shorten segment where num could be found
                if mid_pt_elem > num:
                    # num is smaller than value at the mid point, set highest possible index at 1 location below mid_pt_i
                    high_i = mid_pt_i - 1
                elif mid_pt_elem < num:
                    # num is larger than value at the mid point, set lowest possible index at 1 location above mid_pt_i
                    low_i = mid_pt_i + 1
                else:        
                    # num found in list
                    return True


def check_is_list_element(numeric_list, search_value):
    '''
        Confirms whether search_value in numeric_list, using binary search algorithm.
        
        returns boolean
    '''    
    # discard duplicates and sort list
    sorted_list = sorted(set(numeric_list))
    
    if not str(search_value).isnumeric() and not search_value < 0:
        # non-numeric search_value
        raise ValueError("Expecting numeric search value.")
    else:
        if len(sorted_list) == 0:
            raise ValueError("Empty list received.")
        elif search_value < sorted_list[0] or search_value > sorted_list[-1]:
            # search_value is lower than or higer than any of the values on the list (automatically NOT in list)
            return False
        elif search_value == sorted_list[0] or search_value == sorted_list[-1]:
            # search_value found at first or last elements of sorterd_list
            return True
        else:
            # chop until only 1 element left
            return check_value_found(sorted_list, search_value)


def main():
    my_num_list = [-100, 0, 99, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 12, 12, 43,45, 46, 46, 48, 49, 50, 55, 2, 8, 100, 101]
    my_num = 4
    
    is_list_element = check_is_list_element(my_num_list, my_num)
    
    if is_list_element:
        print(str(my_num) + " is in list.")
    else:
        print(str(my_num) + " is NOT in list.")
        

if __name__ == '__main__':
    main()
