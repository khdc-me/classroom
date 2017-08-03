###
# Rock, Paper, Scissors Game
###
import random

allowed_turns = ['r', 'p', 's']

###
# get full name of turn (r to rock, p to paper, etc)
###
def expandTurnName( t ):
    if t == 'r':
        etn = "Rock"
    elif t == 'p':
        etn = 'Paper'
    else:
        etn = 'Scissors'
        
    return etn

###
# compare turns and determine winner
###
def declareWinner( ht, pct ):
    if ht == pct:
        winner = "tie"
    elif ht == 'r' and pct == 'p':
        winner = "pc"    
    elif ht == 'p' and pct == 's':
        winner = "pc"  
    elif ht == 's' and pct == 'r':
        winner = "pc"
    else:
        winner = "human"
        
    return winner
    
# Game Loop, continue until user types "quit"
while True:
    # Get input from user
    print("Type r, p, or s to play; quit to exit.")
    h_turn = input("(r)ock, (p)aper, (s)cissors: ")
    
    # Check input
    while h_turn.lower() not in allowed_turns and h_turn.lower() != 'quit':
        # user has entered unexpected values
        print("Error: The only 4 options allowed are 'r', 'p', 's', and 'quit'.")
        h_turn = input("(r)ock, (p)aper, (s)cissors: ")
        
    if h_turn == 'quit':
        # player wants to exit program
        break
    else:
        # Computer's turn
        pc_turn = random.choice(allowed_turns)
        
        # Compare turns and report the winner        
        print("User: " + expandTurnName(h_turn))
        print("PC: "   + expandTurnName(pc_turn))
        
        print("Winner: " + declareWinner(h_turn, pc_turn))
    
    # prompt user if he/she wants to play again
    new_game = input("Would you like to play another game? (y)es or (n)o")
    while new_game.lower() != 'y' and new_game.lower() != 'n':
        print("Error: Only 'Y' for Yes or 'N' for No allowed")
        new_game = input("Would you like to play another game? (y)es or (n)o")
        
    if new_game == 'n':
        # user does not want to play again
        break
    else:
        # play again
        continue
