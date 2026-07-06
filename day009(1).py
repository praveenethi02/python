
from turtle import clear


progrmming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving items from the dictionary
'''print(progrmming_dictionary["Bug"])

#Add the new item to dictionary
progrmming_dictionary["Loop"] = "New key and value"

print(progrmming_dictionary)

#create a empty dictionary

no_item = {}
print(no_item)'''

#edit item in a dictionary

'''progrmming_dictionary["Bug"] = "Edit the previous one"
print(progrmming_dictionary["Bug"])'''

#Loop through a dictionary

''' for key in progrmming_dictionary:
    print(key)
    print(progrmming_dictionary[key])'''

#Exercise 01
'''student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for marks in student_scores:
    score = student_scores[marks]
    if score >= 75:
        student_grades[marks] = "A"
    elif score > 50:
        student_grades[marks] = "B"
    elif score > 25:
        student_grades[marks] = "C"
    else:
        student_grades[marks] = "Fail"

print(student_grades)

'''
#Nesting
'''capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}'''

#Nesting a list in a dictionary
'''travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}'''

#Nesting a dictionary in a dictionary
'''travel_log = {
    
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}'''

#Nesting a dictionary in a list
'''travel_log = [
    {"country": "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12},
    {"country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5},
]'''

#Exercise 02
'''country = input("Enter the country you have visited: ")
visits = int(input(f"How many times you have visited {country}: "))
list_of_cities = eval(input())
travel_log = [
    {"country": "France",
     "visits": 12,
     "cities_visited": ["Paris", "Lille", "Dijon"]
     },
    {"country": "Germany",
        "visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
        },]
def add_new_country(name, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)



add_new_country(country, visits, list_of_cities)
print(f"I have been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities_visited'][0]}")'''

#final project day 009

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))

    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        clear()
        find_highest_bidder(bids)

    elif should_continue == "yes":
        clear()