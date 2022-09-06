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
    print("Let's play Hangman!")
    while valid_input is False:
        letter = input("Guess a letter: \n")
        #CI VIDEO, TRY STATEMENT ?
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be one character, not more or less")
        elif letter.isalpha():
            valid_input = True
            user_guess = letter.strip().upper()
            play_hangman(user_guess)    
        else:
            print("Letter must be an alphabet character")
           

def play_hangman(user_guess):
    word = get_word()
    unknown_word = display_word(word)
    guessed_letters = []
    user_won = False
    print(f'You have seleceted: {user_guess}')
    print(f"the {unknown_word} is {word}")
    lives = 6
    print(f'Your guess: {guessed_letters} \n')
    print(f"Your word: {unknown_word}\n")
    if user_guess in guessed_letters:
        print(f"You've already guessed {user_guess}\n")
    elif user_guess in word:    
        print(f'Well done! {user_guess} is in the word')
        guessed_letters.append(user_guess)
    else:
        print("Hard luck. Try again!")
        guessed_letters.append(user_guess)
        lives -= 1 
    validate_user_input()    
   

       



def main():
    get_word()
    display_word('word')
    validate_user_input()

main()