#first chance

print("welcome the roller coster")
height = int(input("Enter your height in cm ? "))

if(height>=120):
    print("You can ride")
    age = int(input("Enter age : "))
    if(age<=12):
        print("pay $5")
    elif(age<=18):
        print("pay $6")
    else:
        print("pay $8")
else:
    print("you can not ride")

#even or odd
'''number = int(input("Enter the number :"))
final = number%2
if(final==1):
    print("Odd")
else:
    print("Even")'''

