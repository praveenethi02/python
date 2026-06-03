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

#Even number sumation in list

num = int(input("Enter number : "))
no = num + 1
total = 0

for number in range(0,no):
    if(number%2==0):
        total+=total
    else:
        total+=0

print(total)



