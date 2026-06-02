'''fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " pie")
    print(fruits.index(fruit))'''

#Get the student height

student_height = input("Enter the heights of students separated by spaces: ").split()
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
print(f"Average height : {avg_height}cm")
