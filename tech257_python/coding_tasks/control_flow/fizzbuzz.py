nums = input("What numbers would you like to use for Fizz and Buzz? e.g. 3 5\n")
nums = nums.split(" ")

num1 = int(nums[0])
num2 = int(nums[1])


def is_fizz_buzz(number):
    return number % num1 == 0 and number % num2 == 0


def is_fizz(number):
    return number % num1 == 0


def is_buzz(number):
    return number % num2 == 0


for num in range(1, 101):
    if is_fizz_buzz(num):
        print("FizzBuzz")
    elif is_fizz(num):
        print("Fizz")
    elif is_buzz(num):
        print("Buzz")
    else:
        print(num)
