#scope

enemies = 1 
def increase_enemies():
    enemies = 2
    print(f"enemise inside function: {enemies}")

increase_enemies()
print(f"enemise outside function: {enemies}")