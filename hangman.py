import random
import string

from regex import A
# import words from file
from words import words
 
# get word from file and filter word with "-" and " " between the letters
def get_the_word(words):
    word = random.choice(words)   
    while "-" in word or " " in word:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = get_the_word(words)
    word_letters = set(word)  # store letter in set
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # put used letters in the used_letters set  
    lives = 5
    
    while len(word_letters) > 0 and lives > 0:
        print("*" * 7)
        print("Remaining lives: ", lives)
        print("Used word: ", "; ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess the letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print("")
                print("there is no such letter in this word bitch!")
        
        elif user_letter in used_letters:
            print("-" * 7, "\nYou already use this letter, please try another")
            print("-" * 7)
    
    if lives == 0:
        print("You died sorry, the word was ", word)
    else:
        print(f"You won, you gussed word '{word}'")        
        
        
hangman()