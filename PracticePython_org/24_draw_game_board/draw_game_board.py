#
#    Draw a 'gameboard' according to dimensions that the user specifies
#

def get_dimensions():
    """
        Prompt user for board dimensions.
            - acceptable values for width and height are between 1
                and 9 (inclusive)
            - will produce board anywhere from 1x1 to 9x9
            
        Returns tuple (width, height)
    """
    width = input("How many squares wide (1 - 9):\n")
    while (not width.isnumeric()
            or (int(width) < 1 or int(width) > 9)):
        # invalid input detected
        width = input("Please indicate how wide you would like the game board to be (1 - 9):\n")
        
    height = input("How many squares high (1-9):\n")
    while (not height.isnumeric()
            or (int(width) < 1 or int(width) > 9)):
        # invalid input detected
        height = input("Please indicate how high you would like the game board to be (1 - 9):\n")
        
    return int(width), int(height)


def draw_horizonal_gridline(reps):
    print(" ---" * reps + " ")
    
    
def draw_vertical_gridline(reps):
    print("|" + "   |" * reps)


def draw_board(dims):
    """
        Draw board according to 'drims'
            - dims is tuple w/ values for number of squares wide (w) and
                number of squares high (h)
    """
    w, h = dims
    
    for i in range(h):
        if i == 0:
            draw_horizonal_gridline(w)
            draw_vertical_gridline(w)
            draw_horizonal_gridline(w)
        else:
            draw_vertical_gridline(w)
            draw_horizonal_gridline(w)
            
        

def main():
    dimensions = get_dimensions()
    
    draw_board(dimensions)
    

if __name__ == "__main__":
    main()
