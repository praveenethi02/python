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
print(no_item)

#edit item in a dictionary

progrmming_dictionary["Bug"] = "Edit the previous one"
print(progrmming_dictionary["Bug"])

#Loop through a dictionary

for key in progrmming_dictionary:
    print(key)
    print(progrmming_dictionary[key])'''

#Exercise 01
student_scores = {
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

