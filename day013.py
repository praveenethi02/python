# #Discribe the problem
# def my_function():
#     for i in range(1,20):
#         if i == 20:
#             print("you got it")

# my_function()



#Reproduce the bug

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])