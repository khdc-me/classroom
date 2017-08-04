# Hangman  
In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.  
  
In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. In this exercise, we have to put it all together and add logic for handling guesses.  
  
Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:  
> Only let the user guess 6 times, and tell the user how many guesses they have left.  
> Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.  

Optional additions:  
1. When the player wins or loses, let them start a new game.  
1. Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!  
  
NOTE: Program randomly selects line from a [SOWPODS dictionary](http://norvig.com/ngrams/sowpods.txt) that is saved locally.
