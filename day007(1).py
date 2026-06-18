import random
import hangman_word

stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]

life = 6


chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Enter the guess letter : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You chosen letter {guess} not in word.So you miss one life.")
        life -= 1
        if life == 0:
            end_of_game = True
            print(f"You lose and correct word is {chosen_word}.")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(stages[6-life])