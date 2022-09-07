import random
from words import words
import string

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
        if len(letter) <= 0 or len(letter) > 1:
            print("Letter must be one character, not more or less")
        elif letter.isalpha():
            valid_input = True
            user_guess = letter.strip().upper()   
        else:
            print("Letter must be an alphabet character")
    return user_guess
           
def validate_user_guess():
    word = get_word()
    user_guess = validate_user_input()
    guessed_letters = []
    wrong_letters = []
    lives = 6
    
    if user_guess in word:
        guessed_letters.append(user_guess)
        print(f'Correct! {user_guess} is in the word.\n' )
    else:
        wrong_letters.append(user_guess)
        lives -= 1
        print(f'Hard luck! Your lives are {lives} \n')    

def play_hangman():
    word = get_word()
    user_guess = validate_user_input()
    guessed_letters = []
    wrong_letters = []
    lives = 6
    user_won = False
    #print(f'You have seleceted: {user_guess}')
    #print(f"the {unknown_word} is {word}")
    while len(unknown_word) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in unknown_word:
                unknown_word.remove(user_guess)
                print('')
            else:
                lives = lives - 1
                print("Hard luck. Try again!")
        elif user_guess in guessed_letters:
            print(f"You've already used: {user_guess}\n")
        else:
            print("Guess not valid")
        break



def main():
    get_word()
    display_word('word')
    validate_user_input()
    validate_user_guess()
    #play_hangman()

if __name__ == '__main__':
    """Will only be called when you run the python program from the terminal or an IDE like PyCharms"""
    main()    
