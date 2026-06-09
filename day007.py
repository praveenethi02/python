
import random
#Hangman game stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
#word_list = ["ardvark", "baboon", "camel"]

import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False

lives = 6 

Display = []

for _ in range(len(chosen_word)):
    Display += "_"
print(Display)


while not end_of_game:  
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            Display[position]= letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0: 
            end_of_game = True
            print("You lose.")

    print(f"Word is : {Display}")

    if "_" not in Display:
        end_of_game = True
        print("You win.")


    print(stages[lives])
