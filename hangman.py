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

def main():
    get_word()
    display_word('word')

main()