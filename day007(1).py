import random

word_list = ["apple", "banana", "orange"]

chosen_word = random.choice(word_list)
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

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")