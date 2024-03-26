age = None

# SET VARIABLE user_prompt TO TRUE
user_prompt = True
# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
while user_prompt:
    age = input("What is your age? ")

    if age.isdigit() and int(age) <= 117:
        user_prompt = False
    else:
        if age.isdigit():
            print("Age cannot be greater than 117!")
        else:
            print("Age entered in invalid format!")

print(f"Your age is {age}")
