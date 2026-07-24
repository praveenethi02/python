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


enemies = 1 

def increase_enemies():
    global enemies 
    # enemies += 1
    # print(f"enemise inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemise outside function: {enemies}")
