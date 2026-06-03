import random

'''fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits.index(fruit))'''

#Get the student height

'''student_height = input("Enter the heights of students separated by spaces: ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
total_height = 0
num_of_students = 0
for height in student_height:
    total_height += height
    num_of_students += 1

avg_height = total_height / num_of_students
avg_height = round(avg_height)

print(f"Total height : {total_height}cm")
print(f"Number of students : {num_of_students}")
print(f"Average height : {avg_height}cm")'''

#Find the highest number in list

'''score = input("Enter the numbers : ").split()
max = 0
for n in range(0, len(score)):
    score[n]=int(score[n])
    if(max<score[n]):
        max = score[n]
    else:
        max=max

print(f"Max score is : {max}")'''

#range function in for loop

'''for number in range(1,10):
    print(number)          #when we added the range (1,10) in for loop print 1 - 9 num only.If we want the 10 we must added to range (1-11).

for number in range(1,10,3):
    print(number)      #output is 1 4 7'''  


#Get the total of list using for loop
'''total = 0
for num in range(1,101):
    total+=num

print(total)'''

#Calculate the even numbers sum in list using for loop

'''num = int(input("Enter number : "))
no = num + 1
total = 0

for number in range(1,no):
    if(number%2==0):
        total+=number
    else:
        total+=0

print(total)'''

#2nd method
'''num = int(input("Enter number : "))
no = num + 1
total = 0
for num in range(0,no,2):
    total+=num

print(total)'''

#PizzBuzz game 

'''num = int(input("Enter the number : "))
no = num + 1

for number in range(1,no):
    if(number%3==0 and number%5==0):
        print("PizzBuzz")
    elif(number%3==0):
        print("Pizz")
    elif(number%5==0):
        print("Buzz")
    else:
        print(number)'''

#Password Genarator (Day final project)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
'''password = ""

#Easy method  (chjj(*&143))

for char in range(1,nr_letters+1):
    rand_char = random.choice(letters)
    password = password + rand_char

for char in range(1,nr_symbols+1):
    rand_sym = random.choice(symbols)
    password = password + rand_sym

for char in range(1,nr_numbers+1):
    rand_num = random.choice(numbers)
    password = password + rand_num

print(f"Password : {password}")'''

#Hard Metod  
password_list = []


for char in range(1,nr_letters+1):
   password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
    password_list += (random.choice(symbols))
    
for char in range(1,nr_numbers+1):
   password_list += (random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

pw = ""

for char in password_list:  #list to varible
   pw += char

print(f"Password is : {pw}")
