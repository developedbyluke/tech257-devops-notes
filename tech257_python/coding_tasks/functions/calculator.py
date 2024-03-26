from math_operations import addition, subtraction, multiplication, division

choice = input("What operation do you want to perform? ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "addition":
    print("The result is:", addition(num1, num2))
elif choice == "subtraction":
    print("The result is:", subtraction(num1, num2))
elif choice == "multiplication()":
    print("The result is:", multiplication(num1, num2))
elif choice == "division()":
    print("The result is:", division(num1, num2))
else:
    print("Invalid choice.")
