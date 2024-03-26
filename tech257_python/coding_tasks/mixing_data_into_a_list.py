from datetime import datetime

monthsToIndexes = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

current_date = datetime.now()
current_year = current_date.year
current_month = current_date.month

name_str = input("What is your name? ")
age_int = int(input("How old are you? "))
month_str = input("What month were you born in? ")

user_details_list = [name_str, age_int, month_str]

birth_year = current_year - age_int
birth_month = monthsToIndexes[month_str]

if birth_month > current_month:
    birth_year = birth_year - 1

print(f"Your name is {user_details_list[0]}, you are {user_details_list[1]} years old and you were born in the month {user_details_list[2]}")

print(f"You were born in the year {birth_year}")

past_date = datetime(birth_year, birth_month, 1, 0, 0, 0)

difference = current_date - past_date

total_hours = difference.total_seconds() / 3600

print(f"You have been alive for around {round(total_hours)} hours.")

height = input("What is your height in cm? ")
user_details_list.append(float(height))
print(f"Your height is {user_details_list[-1]} cm.")
