# #Discribe the problem
# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("you got it")

# my_function()



# #Reproduce the bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5)
# print(dice_imgs[dice_num])


# # play computer
# year = int(input("What's the your birth year ? "))
# if year > 1980 and year < 1994 :
#     print("You are a millenial.")
# elif(year >= 1994):
#     print("You are the gen Z.")


# #fix the error
# age = int(input("Enter your Age : "))
# if age > 18:
#     print(f"You can drive at age {age}")

# else:
#     print("You can not drive")


# #Print is your friend
# pages = 0
# word_per_page = 0
# pages = int(input("How many pages do you want to print? "))
# word_per_page = int(input("How many words per page? "))
# total_words = pages * word_per_page
# print(total_words)


# #use a dibugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)

#     print(b_list)

# mutate([1,2,3,5,8,13])


# # exersise 1

# number = int(input("Enter number : "))

# if number % 2 == 0 :
#     print("Even number")
# else:
#     print("Odd number")


# #exersise 2
# year = int(input("Enter year : "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#     print("Not leap year")

#exersise 3
target = int(input())
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)