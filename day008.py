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

import math

def paint_cal(height, width, cover):
    cans = (height*width)/cover
    round_up_cans = math.ceil(cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height : "))
test_w = int(input("Width : "))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)