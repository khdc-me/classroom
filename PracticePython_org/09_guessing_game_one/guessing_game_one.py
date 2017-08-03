###
# Program generates random number (rand_num) between 1 and 9 (inclusive), and
#        prompts user to guess (usr_guess) a number. THe program determines if
#        usr_guess is above, below, or equal to rand_num.
#    If user guessed the rand_num, program displays the number of tries it took user
#        to guess correctly, and immediately launches a new game.
#    IF user guessed above or below rand_num, the program lets user know and prompts
#        user for another guess.
#    User can quit out of game by typing 'exit' instead of a number when prompted for
#        a guess.
###

from random import randint

###
# reset number of guesses and let user know a new game has started
###
def resetGuesses():
    print("A New Game has started! Good luck!")
    
    return 0
    
    
###
# prompt user for guess and validate input
###
def getUserGuess():
    userGuess = input("Guess a number from 1 to 9 (including 1 & 9). Type 'exit' to end game.\n")
    
    if userGuess != "exit":
        # user did not exit, verify userGuess is a number between 1 and 9 (inclusive)
        while (userGuess.isnumeric()==False) or ( (int(userGuess)>9) or (int(userGuess)<1) ):
            userGuess = input("Error: Your guess must be 1, 2, 3...8, 9, or the word 'exit'. Please try again.\n")
    
    return userGuess


###
# Main Program
###
num_guesses = resetGuesses()
while True:
    # prompt user for guess    
    usr_guess = getUserGuess()
    
    if usr_guess.lower() == "exit":
        # user wants to quit out of program
        print("Thank you for playing. Good bye.")
        break

    if num_guesses == 0:
        # new game
        # generate random number
        rand_num = randint(1, 9)
        print("rand_num: " + str(rand_num))
    
    # compare guess against rand_num
    num_guesses += 1
    if int(usr_guess) > rand_num:
        print("Your guess is too high.\n")
    elif int(usr_guess) < rand_num:
        print("Your guess is too low.\n")
    else:
        # user guessed right
        if num_guesses == 1:
            print("You guessed the number right on your first try! Nice!")
        else:
            print("You guessed the number right in " + str(num_guesses) + " guesses.\n")

            # start new game
            num_guesses = resetGuesses()
