word_list = ["ardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)

Display = []

for _ in range(len(chosen_word)):
    Display += "_"
print(Display)


end_of_game = False

while not end_of_game:  
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            Display[position]= letter
        

    print(f"Word is : {Display}")

    if "_" not in Display:
        end_of_game = True
        print("You win.")
