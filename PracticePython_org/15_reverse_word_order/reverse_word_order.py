###
#    Program takes a string w/ multiple words (sequence or characters separated by a space)
#        and prints out a string where the words have been reversed.
#        - ex: "My cat meows" would display as "meows cat My"
###

###
# Prompt user for input
###
def getSentence():
    sen = input("Please type a sentence you would like to see reversed (Must containe at least two words).\n")
    while ' ' not in sen:
        # invalid input detected
        sen = input("Error: A minimum of 2 words separated by 1 space is required. Please retype your sentence.\n")
    
    return sen


###
# Reverse words in string
###
def reverseWords(s):
    return ' '.join(s.split()[::-1])


###
# Main Program
###
sentence = getSentence()

print(reverseWords(sentence))
