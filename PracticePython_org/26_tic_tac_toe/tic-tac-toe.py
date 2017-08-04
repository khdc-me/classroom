#
#    Draw a 'gameboard' according to dimensions that the user specifies
#
#    Currently 3x3 board, but coded in way that it is easy integrate
#        dynamic board dimensions
#

def reset_board(rows, cols):
    """
        Build/reset board: insert integer value for each position within
            rows x cols dimensions
            - [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
            
        returns list
    """
    board = []
    
    for i in range(rows):
        row = list(str(num + (cols * i)) for num in range(1, cols+1))
        board.append(row)
    
    return board


def draw_horizontal_gridline(cols):
    horizontal_gridline = " ---" * cols
    horizontal_gridline += " "
    
    print(horizontal_gridline)
    
    
def draw_vertical_gridline(board, cols, y_coord):
    """
        Draw rows that contain game_board values (player moves and position
            IDs)
    """
    vertical_gridline = ""
    
    for x_coord in range(cols):
        vertical_gridline += "| " + board[y_coord][x_coord] + " "

    vertical_gridline += "|"
    
    print(vertical_gridline)\


def draw_board(game_board, rows, cols):
    """
        Draw current board (numbers 1 - 9 if position is available; 'X' or 'O' if position taken)
    """
    for i in range(20):
        print("\n")
        
    for y in range(rows):
        if y == 0:
            draw_horizontal_gridline(cols)
            draw_vertical_gridline(game_board, cols, y)
            draw_horizontal_gridline(cols)
        else:
            draw_vertical_gridline(game_board, cols, y)
            draw_horizontal_gridline(cols)
            
            
def get_move(board, rows, cols, player):
    """
        Prompt user for position in which to place mark
        
        Checks that position is available
        
        returns string
    """
    available_positions = []
    
    if player == "player1":
        start_string = "Player 1"
        mark_string = "X"
    else:
        start_string = "Player 2"
        mark_string = "O"
    
    # Find available positions (those without an 'X' or and 'O')
    for y_coord in range(cols):
        for x_coord in range(rows):
            if board[y_coord][x_coord].isnumeric():
                available_positions.append(board[y_coord][x_coord])
                
    move = input(start_string + ", where would you like to place your " + mark_string + "? (q)uit | (r)estart:  ")
    while move not in available_positions and move.lower() not in ('q', 'r'):
        move = input("Error: Please select from the following available" \
                     + " positions: " + str(available_positions) + " (q)uit | (r)estart:  ")

    return move.lower()


def get_mark(player_num):
    """
        Determines whether mark to be placed into board is an 'X' or an 'O'
        
        returns string
    """
    if player_num == "player1":
        return 'X'
    else:
        return 'O'
    
    
def get_position_coordinates(board, pos):
    """
        Get the coordinates (row, col) of current move
            - coordinates used when checking for winning moves
    
        returns tuple
    """
    for i, row in enumerate(board):
        if pos in row:
            x, y = i, row.index(pos)
    
    return x, y
    
    
def make_move(player_num, board, position):
    """
        Place an 'X' or an 'O' (depending on the player) into the game board
        
        returns tuple
    """
    x_or_o = get_mark(player_num)
    x_coord, y_coord = get_position_coordinates(board, position)

    board[x_coord][y_coord] = x_or_o
    
    return board, x_coord, y_coord


def check_diagonal_win(board, rows, cols, x_coord, y_coord):
    """
        Check if player has three of his marks in the same row as 'x_coord'.
        
        return bool
    """ 
    # check diagonal positions from top-left to bottom-right
    if x_coord == y_coord:
        test = []
        x = 0
        y = 0
        
        while x < rows and y < cols:
            test.append(board[x][y])
            x += 1
            y += 1
            
        if len(set(test)) == 1:
            return True
    
    # check diagonal positions from bottom-left to top-right
    if ((x_coord == 0 and y_coord == cols-1)
        or (x_coord == 1 and y_coord == 1)
        or (x_coord == rows-1 and y_coord == 0)):
        test = []
        x = rows-1
        y = 0

        while x >=0 and y < cols:
            test.append(board[x][y])
            x -= 1
            y += 1

        if len(set(test)) == 1:
            return True

    return False


def check_row_win(board, cols, x_coord):
    """
        Check if player has three of his marks in the same row as 'x_coord'.
        
        return bool
    """
    test = [val for val in board[x_coord]]
    if len(set(test)) == 1:
        return True
    else:
        return False


def check_column_win(board, rows, y_coord):
    """
        Check if player has three of his marks in the same column as 'y_coord'.
        
        return bool
    """
    test = []
    
    for x in range(rows):
        test.append(board[x][y_coord])

    if len(set(test)) == 1:
        return True
    else:
        return False


def check_for_win(board, rows, cols, x_coord, y_coord):
    """
        Check if where last move was placed and then check accordingly
            - ex: if last move placed at top-left position (x: 0, y: 0), check
                if this move won horizontally, vertically, or diagonally
                
        returns bool
    """
    # check if move is in diagonal position
    if (x_coord == y_coord    # all positions in diagonal from top-left to bottom-right
        or (x_coord == rows-1 and y_coord == 0) # bottom-left position
        or (x_coord == 0 and y_coord == cols-1)):   # top-right position
        if (check_diagonal_win(board, rows, cols, x_coord, y_coord)
            or check_row_win(board, cols, x_coord)
            or check_column_win(board, rows, y_coord)):
            return True
        else:
            return False
    else:
        # move is in row or column position
        if (check_row_win(board, cols, x_coord)
            or check_column_win(board, rows, y_coord)):
            return True
        else:
            return False

    # center position has been checked for diagonal wins but not row or column        
    if x_coord == 1 and y_coord == 1:
        if (check_row_win(board, cols, x_coord)
            or check_column_win(board, rows, y_coord)):
            return True
        else:
            return False
        
        
def switch_players(player):
    """
        Changes the player who is to make a move (place a mark on the board)
        
        returns string
    """
    if player == "player1":
        return "player2"
    else:
        return "player1"
    
    
def play_again():
    """
        Game has ended (either a win or a draw), prompt players if they would like to
            play another game or not
            
        returns bool
    """
    another_game = input("Would you like to play again? (y)es | (n)o  ")
    while another_game.lower() not in ('y', 'n'):
        another_game = input("Press y if you would like to play again, otherwise, press n:  ")
        
    if another_game.lower() == 'y':
        return True
    else:
        return False
            

def main():
    new_game = True
    quit_game = False
    
    rows = 3
    columns = 3
    
    while not quit_game:
        if new_game:
            # reset board and game variables
            game_board = reset_board(rows, columns)
            
            new_game = False
            curr_player = "player1"
            num_turns = 0
        else:
            # continue game        
            draw_board(game_board, rows, columns)
            move = get_move(game_board, rows, columns, curr_player)
                        
            num_turns += 1
            
            if move == 'r':
                # restart game
                new_game = True
                continue
            elif move == 'q':
                # quite game
                print("Thank you for playing, good bye!")
                quit_game = True
            else:
                # place mark
                game_board, x_coordinate, y_coordinate = make_move(curr_player, game_board, move)
                
                if num_turns >= 4:   # No need to check for win until each player has had 2 turns
                    is_winner = check_for_win(game_board, rows, columns, x_coordinate, y_coordinate)
                    
                    if is_winner:
                        draw_board(game_board, rows, columns)
                        print(curr_player + " has won!")
                        if play_again():
                            new_game = True
                        else:
                            print("Thank you for playing, good bye!")
                            quit_game = True

                if num_turns == 9:  # draw if all positions are taken and no winner identified
                    draw_board(game_board, rows, columns)
                    print("Game is a draw.")
                    if play_again():
                        new_game = True
                    else:
                        print("Thank you for playing, good bye!")
                        quit_game = True
                
                # no winner, no draw        
                # switch players        
                curr_player = switch_players(curr_player)               
                

if __name__ == "__main__":
    main()
