#first chance

'''print("welcome the roller coster")
height = int(input("Enter your height in cm ? "))

if(height>=120):
    print("You can ride")
    age = int(input("Enter age : "))
    photo = input("do you want aticket (y/n) :")
    if(photo=="y"):
        if(age<=12):
          print("pay $7")
        elif(age<=18):
          print("pay $8")
        elif(age<=45):
          print("pay $10")
        else:
           print("Free!")
    else:
        if(age<=12):
          print("pay $5")
        elif(age<=18):
          print("pay $6")
        elif(age<=45):
          print("pay $8")
        else:
           print("Free!")
else:
    print("you can not ride")'''

#even or odd
'''number = int(input("Enter the number :"))
final = number%2
if(final==1):
    print("Odd")
else:
    print("Even")'''

#BMI calculator

'''h = float(input(""))
w = float(input(""))

bmi = w/(h**2)
bmi = round(bmi , 2)

print(f"Your bmi value is {bmi}")
if(bmi<= 18.5):
    print("Underweight")
elif(bmi<= 25):
    print("weight")
elif(bmi<= 30):
    print("normal weight")
else:
    print("over weight")'''

#leap year

'''year = int(input(""))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not leap")
    else:
        print("leap year")
else:
    print("Not leap")'''

#pizza order

'''print("Welcome Pizza mart")
q = input("Choose size , S,M or L : ")
pep = input("Peparoni (Y/N) : ")
ec = input("Extra chees (Y/N) : ")

bill = 0
if (q == "S"):
    bill += 15
elif (q == "M"):
    bill += 20
else:
    bill += 25

if (pep == "Y"):
    if (q == "S"):
        bill += 2
    else:
        bill += 3
if (ec == "Y"):
    bill += 1
else:
    bill = bill

print(f"Full amount : ${bill}")'''


#Love calculator

'''print("____Welcome to love calculator!!!____")
boy = input("Enter boy name : ")
girl = input("Enter girl name : ")

name = boy + girl #create a combine name
l_name = name.lower()  #create a full lower case name (EthiPola -> ethipola)

t = l_name.count("t")   #get the letters count
r = l_name.count("r")
u = l_name.count("u")
e = l_name.count("e")

first_digit = t + r + u + e

l = l_name.count("l")
o = l_name.count("o")
v = l_name.count("v")

second_digit = l + o + v + e

final_digit = str(first_digit) + str(second_digit)

print(f"Your love precentage is : {final_digit}")'''

#day 3 last project
#Tressure island

print("____Welcome\" to Tressure island____\n____your mission find to tressure____")
d1 = input("what direction you want to go , left or right : ").lower()

if(d1=="left"):
    d2 = input("Swim or Wait : ").lower()
    if(d2=="wait"):
        d3 = input("red , blue or yellow : ").lower()
        if(d3=="yellow"):
          print("Congratulatin! You win!")
        else:
          print("Game over!")

    else:
        print("Game over!")
else:
    print("Game over!")







