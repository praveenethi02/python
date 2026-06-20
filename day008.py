import caesor_cipher_logo
print(caesor_cipher_logo.logo)
'''def greet():
    print("This is new function")
    print("hello praveen")
    print("what is your daily shedule")

greet()'''


'''def greet_with_name(name):
    print(f"This is new function {name}")
    print(f"hello {name}")
    print(f"what is your daily shedule {name}")

greet_with_name("praveen")'''


'''def greet_with(name, location):
    print(f"This is new function {name}")
    print(f"hello {name}")
    print(f"what is your daily shedule in {location}")

greet_with("praveen", "matale")'''

'''def greet_with(name, location):
    print(f"This is new function {name}")
    print(f"hello {name}")
    print(f"what is your daily shedule in {location}")

greet_with(location = "matale", name = "praveen")'''


#Activity 1

'''import math

def paint_cal(height, width, cover):
    cans = (height*width)/cover
    round_up_cans = math.ceil(cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height : "))
test_w = int(input("Width : "))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)'''

#Activity 2

'''def prime_checker(number):
    is_prime = True
    for x in range(2,number):
        if number % x == 0:
            is_prime = False
        
    if is_prime:
        print("Prime!")

    else:
        print("Not prime!")

n = int(input())
prime_checker(number=n)'''

#Caesar Cipher game


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Normal method
'''def decrypt(plain_text, shift_amount):
    new_word = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        shift_a = (position - shift_amount)%26
        new_word = new_word + alphabet[shift_a]

    print(new_word)

def encrypt(plain_text, shift_amount):
    new_word = ""
    for letter in plain_text:
       position = alphabet.index(letter)
       shift_a = (position + shift_amount)%26
       
       new_word = new_word + alphabet[shift_a]

    print(new_word)
    
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(plain_text = text, shift_amount = shift)
else:
    print("Wrong enter!")
'''

#Good method
def caesar(plain_text, shift_amount, dir):
    if dir == "decode":
        new_word = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            shift_a = (position - shift_amount)%26
            new_word = new_word + alphabet[shift_a]
        print(new_word)
    elif dir == "encode":
        new_word = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            shift_a = (position + shift_amount)%26
            
            new_word = new_word + alphabet[shift_a]
        print(new_word)

caesar(plain_text = text, shift_amount = shift, dir = direction)