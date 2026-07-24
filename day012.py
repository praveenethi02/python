####################scope

# enemies = 1 
# def increase_enemies():
#     enemies = 2
#     print(f"enemise inside function: {enemies}")

# increase_enemies()
# print(f"enemise outside function: {enemies}")

#################Local scope

# def drink():
#     potion = 2
#     print(potion)

# drink()

################Global scope
# play = 10

# def dd():
#     poe = 2
#     print(play)

# dd()

#############################
# game_level = 3
# def create_enemy():
#     enemies = ["Skelton","Zombie","Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

#########################
# enemies = 1 

# def increase_enemies():
#     global enemies 
#     # enemies += 1
#     # print(f"enemise inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemise outside function: {enemies}")


#Day final project

# import random


# print("Wel come the number gessing game!")
# choose = input("I'm thinking of a number between 1 and 100.Choose a difficulty.Type 'easy' or 'hard' : ").lower()

# random_int = random.randint(1, 100)

# def game():
#     global choose
#     global random_int
#     if choose == "easy":
#         print("You have 10 attempts.")
#         gess = True
#         attempt = 10
#         while gess and attempt > 0:
#             enter = int(input("Make a guess : "))
#             if enter == random_int:
#                 print("You win!")
#                 gess == False

#             elif enter > random_int:
#                 print("Too high!")
#                 attempt -= 1

#             elif enter < random_int:
#                 print("Too low!")
#                 attempt -= 1

# game()


import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    random_int = random.randint(1, 100)
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if choose == "easy":
        attempts = 10
    elif choose == "hard":
        attempts = 5
    else:
        print("Invalid choice, defaulting to 5 attempts.")
        attempts = 5

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == random_int:
            print(f"You got it! The answer was {random_int}. You win! 🎉")
            return
        elif guess > random_int:
            print("Too high.")
        else:
            print("Too low.")
            
        attempts -= 1

    print(f"\nYou've run out of guesses! The number was {random_int}. Game over.")

game()