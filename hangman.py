import random
from words import words
import string

#Global variables

lives = 6

guessed_letters = []

wrong_letters = []

game_over = False



"""
Retrieves a random word from the words.py file
"""
def get_word():
    word = random.choice(words)
    return word.upper()


"""
Displays the hidden word to the user
"""
"""def display_word(word):
    unknown_word = "-" * len(word)
    print(f'Your word is {len(word)} letters long: {unknown_word}\n')
    return unknown_word"""

"""
Displays the hidden word to user
"""
def display_word():
    word = get_word()
    letter = ""
    global guessed_letters

    for i in range(0, len(word)):
        letter = word[i]
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")        

"""
Checks the user has typed only one alphabet character and not 
multiple charaters and/or numbers.
Warns user if they choose a letter they have already chosen.
"""
def validate_user_input():
    valid_input = False
    letter = ""
    while valid_input is False:
        letter = input("Guess a letter: \n")
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be one character, not more or less")
        elif letter.isalpha():
            if letter in guessed_letters or letter in wrong_letters:
                print(f'You have already guessed {letter}. Try a different one.\n')
            else:
                valid_input = True
                user_guess = letter.strip().upper()   
        else:
            print("Letter must be an alphabet character")
    return user_guess

"""
Checks is user's guess is in the word and takes a life if not
"""         
def validate_user_guess():
    word = get_word()
    user_guess = validate_user_input()
    global guessed_letters
    global wrong_letters
    global lives 
    
    if user_guess in word:
        guessed_letters.append(user_guess)
        print(f'Correct! {user_guess} is in the word.\n')
    else:
        wrong_letters.append(user_guess)
        lives -= 1
        print(f'Hard luck {user_guess} is not in the word!\n') 
    print(f'You have {lives} lives remaining \n')
    print(f'correct {guessed_letters}\n')
    print(f'wrong {wrong_letters}\n')   

"""
Checks for the status of the lives and the word letters to determine game over
"""
def check_game_over():
    global lives
    global game_over
    global guessed_letters
    word = get_word()
    user_guess = validate_user_input()

    if lives <= 0:
        game_over = True
        print(f'Hard luck! You lost. The word was {word}\n')
    else:
        word_guessed = True
        for user_guess in word:
            if user_guess not in guessed_letters:
                word_guessed = False
                break
        if word_guessed:
            game_over = True
            print('You guessed the word! Congratulations\n')    


def main():
    global game_over
    global lives
    global guessed_letters
    global wrong_letters

    game_over = False
    print("Let's play Hangman!")
    get_word()
    
    while game_over is False:
        display_word()
        
        if len(wrong_letters) > 0:
            print(f"Incorrect guesses: {wrong_letters}\n ")
        validate_user_input()
        validate_user_guess()
        check_game_over()
    
main()    
