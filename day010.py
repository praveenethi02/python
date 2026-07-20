#Function with outputs

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't enter a valid answer."

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return print(f"Result : {formated_f_name} {formated_l_name}")


# print(format_name(input("Enter first name : "),input("Enter last name : ")))

#exersize 1
"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
                return "leap_year"
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
            return "leap_year"
    else:
        print("Not leap year.")


def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = month_days[month-1]

    if is_leap(year) == "leap_year" :
        if month == 2:
            return day + 1

        else:
            return day

    else:
        return day
    
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year,month)
print(days)
"""

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide 
}

num1 = int(input("Enter first number : "))

for symble in operations:
    print(symble)

operation_symble = input("Pick an operation from the line above : ")

num2 = int(input("Enter second number : "))

calculation_function = operations[operation_symble]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symble} {num2} = {first_answer}")

operation_symble = input("Pick an operation from the line above : ")
num3 = int(input("Enter another number : "))
calculation_function = operations[operation_symble]
second_answer = calculation_function(first_answer, num3)

print(f"{first_answer} {operation_symble} {num3} = {second_answer}")
