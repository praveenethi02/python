#Function with outputs

# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't enter a valid answer."

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return print(f"Result : {formated_f_name} {formated_l_name}")


# print(format_name(input("Enter first name : "),input("Enter last name : ")))

#exersize 1

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