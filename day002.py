'''a = str(12333)
print(type(a))
print(len(a))

print("hello"[2])

print(str(22)+str(23))'''

'''two_digit_num = input()
a = int(two_digit_num[0])
b = int(two_digit_num[1])
print(a + b)'''

#BMI calculator

'''h = float(input("Enter the height :"))
w = float(input("Enter the weight :"))

bmi = w/(h**2)

print("Your BMI value is " + str(bmi))'''

# //
'''print(8//2)
print(8/2)
print(type(8//2))
print(type(8/2))'''

#f-string

'''score = 80
height = 1.75
win = True
print(f"your score is {score}, height is {height}, win is {win}.")'''

#age claculator

'''age = input()
year = 90 - int(age)
weeks = year*52
print(f"you have {weeks} weeks only")'''

# Tip calculator

print("welcome the tip calculator")
x = float(input("Enter the total bill :$"))
y = int(input("what precentage tip do you like to give (10,12 or 15) : "))
z = int(input("How many people split the bill : "))

y2 = y/100
extra = x * y2
total = x + extra
last = total/z
last = round(last,2)

print(f"your tip is : ${last}")

