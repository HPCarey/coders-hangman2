import random
import time
import os
import sys
from words import words
from hangman import HANGMAN

# Global variables

lives = 6

guessed_letters = []

wrong_letters = []

game_word = ""

game_over = False





def get_word():
    """
    Will return a randomly selected word from the predefined
    list of words in the word.py file.
    """
    global game_word

    random.seed(time.time())
    game_word = random.choice(words)
    game_word = game_word.upper()


def display_word():
    """
    Displays the hidden word to user and the correct letters once guessed
    """
    global game_word
    global guessed_letters

    for i in range(0, len(game_word)):
        letter = game_word[i]
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n")


def display_hangman():
    """
    Prints out different stages of the hangman based on
    the user's number of lives.
    """
    global lives

    index = 6 - lives
    print(HANGMAN[index])



def validate_user_input():
    """
    Checks the user has typed only one alphabet character and not
    multiple charaters and/or numbers.
    Warns user if they choose a letter they have already chosen.
    """
    valid_input = False
    user_guess = ""
    while valid_input is False:
        user_guess = input("Guess a letter: \n")
        user_guess = user_guess.strip().upper()
        if len(user_guess) <= 0 or len(user_guess) > 1:
            os.system("clear")
            display_hangman()
            display_word()
            print(f"Incorrect guesses: {wrong_letters}\n ")
            print(f'You typed {user_guess}\n')
            print("Letter must be one character, not more or less.\n")
            print(f'You have {lives} lives.\n')
        elif user_guess.isalpha():
            if user_guess in guessed_letters or user_guess in wrong_letters:
                os.system("clear")
                display_hangman()
                display_word()
                print(f"Incorrect guesses: {wrong_letters}\n ")
                print(f'You have already guessed {user_guess}.\n')
                print(f'You have {lives} lives.\n')
            else:
                valid_input = True
        else:
            os.system("clear")
            display_hangman()
            display_word()
            print(f"Incorrect guesses: {wrong_letters}\n ")
            print(f'You typed {user_guess}\n')
            print("Letter must be an alphabet character\n")
            print(f'You have {lives} lives.\n')
    return user_guess


def validate_user_guess():
    """
    Checks whether user's guess is in the word and takes a life if not.
    If user guess is correct, appends user guess to guessed_letters variable.
    If user guess is incorrect, appends user guess to wrong_letters varable
    """
    global guessed_letters
    global wrong_letters
    global lives
    user_correct = False

    user_guess = validate_user_input()
    if user_guess in game_word:
        user_correct is True
        guessed_letters.append(user_guess)
    else:
        user_correct is False
        wrong_letters.append(user_guess)
        lives -= 1

    return user_correct


def check_game_over():
    """
    Checks for the status of the lives and the word letters to determine game over.
    If game over is true, calls the replay_game function.
    """
    global lives
    global game_over
    global guessed_letters
    global game_word

    if lives <= 0:
        game_over = True
        os.system("clear")
        display_hangman()
        display_word()
        print(f'Hard luck! You lost. The word was {game_word}\n')
        replay_game()
    else:
        word_guessed = True
        for letter in game_word:
            if letter not in guessed_letters:
                word_guessed = False
                break
        if word_guessed:
            game_over = True
            os.system("clear")
            display_hangman()
            display_word()
            print('You guessed the word! Congratulations\n')
            print(f'The word was {game_word}\n')
            replay_game()
    os.system("clear")


def replay_game():
    """
    Gives user an input option to either play another game or
    exit the programme.
    If user selects option to play again,
    resets global variables to empty values and resets lives to 6.
    """

    global lives
    global game_over
    global wrong_letters
    global guessed_letters
    global game_word
    restart_game = False

    while not restart_game:
        restart = input('Would you like to play again? Y/N \n')
        restart = restart.strip().upper()
        if restart == "Y":
            lives = 6
            guessed_letters = []
            wrong_letters = []
            game_word = ""
            game_over = False
            restart_game = True
            get_word()
        elif restart == "N":
            os.system("clear")
            print('OK, goodbye!\n')
            sys.exit()
        else:
            os.system("clear")
            display_hangman()
            display_word()
            print('You must type N or Y.\n')
            print(f'You typed {restart}. Please try again\n')


def main():
    """
    Calls all the functions in the order they are needed to run the game
    """
    global game_over
    print("Let's play Hangman!")
    get_word()

    while game_over is False:
        display_hangman()
        display_word()

        if len(wrong_letters) > 0:
            print(f"Incorrect guesses: {wrong_letters}\n ")
            print(f'You have {lives} lives.\n')
        validate_user_guess()
        check_game_over()


if __name__ == '__main__':
    """
    Will only be called when you run the python program
    from the terminal or an IDE like PyCharms
    """

    print("""Hello! Welcome to CODER'S HANGMAN!\n
Test your knowledge of programming related vocabulary!\n
Rules:
1. Type a letter and click enter to make a guess for the mystery word.
2. You have 6 lives.
3. Once you have run out of lives and you guess an incorrect letter,
you will lose the game and the full hangman will be displayed.
 \n""")

    input("PRESS ENTER TO START THE GAME.\n >>>\n")
    os.system("clear")
    main()
