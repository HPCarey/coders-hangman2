import random
from words import words

"""
Retrieves a random word from the words.py file
"""
def get_word():
    word = random.choice(words)
    return word.upper()


"""
Displays the hidden word to the user
"""
def display_word(word):
    unknown_word = "-" * len(word)
    print(f'Your word is {len(word)} letters long: {unknown_word}\n')
    return unknown_word

"""
Checks the user has typed only one alphabet character and not 
multiple charaters and/or numbers
"""
def validate_user_input():
    valid_input = False
    letter = ""
    while valid_input is False:
        letter = input("Guess a letter: \n")
        letter = letter.strip().upper()
        """
        CI VIDEO, TRY STATEMENT ?
        """
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be one character, not more or less")
        elif letter.isalpha():
            valid_input = True
            print("Input correct")    
        else:
            print("Letter must be an alphabet character")
    return letter        
         


def main():
    get_word()
    display_word('word')
    validate_user_input()

main()