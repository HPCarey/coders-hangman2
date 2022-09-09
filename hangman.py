import random
import time

# Global variables

lives = 6

guessed_letters = []

wrong_letters = []

game_word = ""

game_over = False




"""
Will return a randomly selected word from our predefine
list of acceptable words
"""


def get_word():
    global game_word

    acceptable_words = [
        "data",
        "data",
    ]

    random.seed(time.time())
    game_word = random.choice(acceptable_words)
    game_word = game_word.upper()


"""
Displays the hidden word to user
"""


def display_word():
    global game_word
    global guessed_letters

    for i in range(0, len(game_word)):
        letter = game_word[i]
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


def display_hangman():
    global lives

    if lives == 6:
        print("+------------+")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 5:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 4:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 3:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           /")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 2:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 1:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|            |\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")
    elif lives == 0:
        print("+------------+")
        print("|            |")
        print("|            O")
        print("|           /|\\")
        print("|           / \\")
        print("|")
        print("|")
        print("+-------+")


def validate_user_input():
    valid_input = False
    user_guess = ""
    while valid_input is False:
        user_guess = input("Guess a letter: \n")
        user_guess = user_guess.strip().upper()
        if len(user_guess) <= 0 or len(user_guess) > 1:
            print("Letter must be one character, not more or less\n")
        elif user_guess.isalpha():
            if user_guess in guessed_letters or user_guess in wrong_letters:
                print(f'You have already guessed {user_guess}.\n')
            else:
                valid_input = True
        else:
            print("Letter must be an alphabet character\n")

    return user_guess


"""
Checks is user's guess is in the word and takes a life if not
"""


def validate_user_guess():
    global guessed_letters
    global wrong_letters
    global lives

    user_guess = validate_user_input()
    if user_guess in game_word:
        guessed_letters.append(user_guess)
        print(f'Correct! {user_guess} is in the word.\n')
    else:
        wrong_letters.append(user_guess)
        lives -= 1
        print(f'Hard luck {user_guess} is not in the word!\n')


"""
Checks for the status of the lives and the word letters to determine game over
"""


def check_game_over():
    global lives
    global game_over
    global guessed_letters
    global game_word

    if lives <= 0:
        game_over = True
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
            display_hangman()
            display_word()
            print('You guessed the word! Congratulations\n')
            print(f'The word was {game_word}\n')
            replay_game()


def replay_game():
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
            print('OK, goodbye')
            break
        else:
            print('You must type N or Y.\n')
            print(f'You typed {restart}. Please try again')


def main():
    global game_over
    print("Let's play Hangman!")
    get_word()

    while game_over is False:
        display_hangman()
        display_word()

        if len(wrong_letters) > 0:
            print(f"Incorrect guesses: {wrong_letters}\n ")

        validate_user_guess()
        check_game_over()
        
        


if __name__ == '__main__':
    """Will only be called when you run the python program from the terminal or an IDE like PyCharms"""
    main()
