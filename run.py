import random
from words import words

def get_word():
    word = random.choice(words)
    print(word)

def main():
    get_word()

main()