import random

#random integer and random float
'''random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love = random.randint(1, 100)
print(f"your love score is {love}")'''

#head or tail

'''chance = random.randint(0,1)
if(chance==1):
    print("Head")
else:
    print("Tail")'''

#variable list
'''states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
"Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", 
"Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", 
"Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
  
print(states_of_america[0])
print(states_of_america[1])

states_of_america[0] = "Delaware2"
print(states_of_america)

states_of_america.append("New state") #add the new item to end of the list
print(states_of_america)'''

#Geuss the name
names_string = input("Enter names separated by commas: ")
names = names_string.split(", ")

num_items = len(names)
random_chance = random.randint(0, num_items-1)
print(names[random_chance])
