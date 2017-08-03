#
#    bulls and cows game
#
#    Similar game to Mastermind, where a code is generated and the user must guess the sequence
#        based on feedback.
#
#    The rules:
#        - Sequence is all numbers (0 - 9)
#        - Sequence is 4 characters in lengths (ie: 0000, 1111), 1234)
#        - User can select to have easy or hard combo (easy combo does not repeat numbers; hard combo can repeat)
#        - The player is awarded a 'bull' if a number they guess is in the right place
#        - The player is awarded a 'cow' if a number they guess is in the sequence, but in the wrong place
#
#    Game will keep track of number of guesses.
#    A player can view the instructions at any point by typing h (for help)
#    A player can view a summary of previous attempts by typing s (for summary)
#    A player can restart the game at any point by typing r (for restart)
#    A player can quit the game at any point by typing q (for quit)
#

from random import randint


def get_difficulty():
    '''
        Prompt user whether he/she wants an easy or hard sequence
        
        returns string
    '''
    desired_difficulty = input("Generate (e)asy or (h)ard 4-digit sequence? (help) | (q)uit\n")
    while desired_difficulty.lower() not in ('e', 'h', 'q', 'help'):
        # invalid input detected
        desired_difficulty = input("Please type e to generate an easy sequence, h to generate a hard sequence, help for help, or q to quit game.\n")
        
    if desired_difficulty.lower() == 'e':
        return 'easy'
    elif desired_difficulty.lower() == 'h':
        return 'hard'
    elif desired_difficulty.lower() == 'q':
        # user wants to quit program
        return "quit"
    else:
        # user wants to view help
        return 'help'
    
    
def get_new_sequence(easy_or_hard):
    '''
        Generate an easy or hard, 4-digit sequence for user to guess
        
        Easy sequence does not have any repeating digits, hard sequences can have repeating numbers
        
        returns list
    '''
    if easy_or_hard == 'easy':
        easy_seq = []
        
        while len(easy_seq) < 4:
            # get random digit
            randnum = randint(0, 9)
            
            if randnum not in easy_seq:
                # random digit is not already in sequence, add it
                easy_seq.append(randnum)
                        
        return easy_seq
    else:
        # generate list w/ 4 random digits
        return [randint(0, 9) for num in range(4)]
    


def get_guess():
    '''
        Prompt user for a guess
            - guess must be a 4-digit sequence
            - digits allowed: 0 - 9
        
        returns list
    '''
    guess_attempt = input("Enter a 4-digit sequence. (0 - 9, inclusive) | 'help' | (q)uit | (s)ummary\n")
    # check that input is:
    #    - 4 characters long and numeric
    #    - if not numeric, is it either 'help', 'q', or 's'
    while ( (len(guess_attempt) != 4 or not guess_attempt.isnumeric() ) \
            and guess_attempt not in ('q', 's', 'help') ):
        # invalid input detected
        guess_attempt = input("You must 4 numbers between 0 and 9 (0 and 9 included) to play. Type help to view game info, q to quit, or s to view your guess summary\n")
        
    if guess_attempt.isnumeric():
        return [int(num) for num in guess_attempt]
    else:
        # user did not guess
        return [guess_attempt.lower()]
    
    
def show_help():
    '''
        Display game information (help)
        
        return None
    '''
    for i in range(20):
        print("\n")
    print("========== GAME INFORMATION ==========")
    print("Bulls and Cows Game\n")
    print("Similar game to Mastermind, where a code is generated and the user must guess the sequence")
    print("based on feedback.\n")
    print("The rules:")
    print("     - Sequence is all numbers (0 - 9)")
    print("     - Sequence is 4 characters in lengths (ie: 0000, 1111), 1234)")
    print("     - User can select to have easy or hard combo (easy combo does not repeat numbers; hard combo can repeat)")
    print("     - The player is awarded a 'bull' if a number they guess is in the right place")
    print("     - The player is awarded a 'cow' if a number they guess is in the sequence, but in the wrong place\n")
    print("Game will keep track of number of guesses.")
    print("A player can view the instructions at any point by typing h (for help)")
    print("A player can view a summary of previous attempts by typing s (for summary)")
    print("A player can restart the game at any point by typing r (for restart)")
    print("A player can quit the game at any point by typing q (for quit)")
    print("======================================")
    
    
def show_summary(guess_log):
    '''
        Display history of guesses and how many bulls/cows each has received
        
        Returns None
    '''
    
    for i in range(20):
        print("\n")
    
    print("\n".join(guess_log))
    
    
def get_bulls_cows(target_sequence, guess_attempt):
    '''
        Looks guess_attempt elements in target_sequence
        
        Awards a bull for every element shared by target_sequence and guess_attempt, at the same index
        Awards a cow for every element shared by target_sequence and guess_attempt, at any index
    '''
    bulls = 0
    cows  = 0
    ga_list = []
    ts_list = []
    
    # check for bulls
    # both, target_sequence and guess_attempt, have a length of 4
    for ga,ts in zip(guess_attempt, target_sequence):
        if ga == ts:
            # common element, common index
            bulls += 1
        else:
            # different element at the same index
            #    place into temp lists and use for cows
            ga_list.append(ga)
            ts_list.append(ts)
    
    # check for cows
    for num in ga_list:
        if num in ts_list:
            # common element
            cows += 1
            ts_list.remove(num)     # remove from future iterations
            
    return { "bulls": bulls, "cows": cows }


def main():
    # main program
    quit_game = False
    new_game  = True
    
    while not quit_game:
        if new_game:
            # start new game
            difficulty = get_difficulty()
            if difficulty not in ('easy', 'hard'):
                # help or quit
                if difficulty == 'help':
                    show_help()
                else:
                    # quit
                    print("Thank you for playing. Good bye!")
                    quit_game = True
            else:
                # difficulty is easy or hard
                sequence = get_new_sequence(difficulty)
                
                num_guesses   = 0
                new_game      = False
                guess_history = ["New game"]
                
                print("New sequence generated: ****\n")                
                continue
        else:
            # continue current game
            # Let player know what sequence he/she is playing
            if difficulty == 'easy':
                print("easy sequence (numbers do not repeat)")
            else: 
                print("hard sequence (numbers may repeat)")
            
            # prompt for new guess    
            guess = get_guess()
            # check if first element in guess is numeric
            if not str(guess[0]).isnumeric():
                # user did something other than guess
                if 'q' in guess:
                    # quit
                    print("Thank you for playing. Good bye!")
                    quit_game = True
                elif 'help' in guess:
                    show_help()
                else:
                    # show summary
                    show_summary(guess_history)
            else:
                # increment number of guesses
                num_guesses += 1
                
                # award bulls and cows to guess
                bulls_cows = get_bulls_cows(sequence, guess)
                # check if winning guess
                if bulls_cows['bulls'] == 4:                    
                    # user guessed sequence
                    if num_guesses == 1:
                        print("Congratulations! You guessed the right sequence in a single try!")
                    else:
                        print("Congratulations! You guessed the right sequence in " + str(num_guesses) + " tries.")
                else:
                    # user did not guess sequence
                    # display bulls and cows on screen
                    print("Bulls: " + str(bulls_cows['bulls']) + " | Cows: " + str(bulls_cows["cows"]))
                    
                    # log guess into summary/history
                    guess_history.append("Guess # " + str(num_guesses) + " | " + str(guess) + " | Bulls: " + str(bulls_cows['bulls']) + " | Cows: " + str(bulls_cows['cows']))


if __name__ == '__main__':
    main()
