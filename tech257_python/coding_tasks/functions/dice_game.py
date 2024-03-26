"""
Make a die game:

Let's make a game that rolls a die and picks a winner.

Start the game with a welcome message and ask if the user is ready to play.

Get the user's name and start a loop (While loop recommended)

Use the random library and a method from that library to roll, a number 1-6

Store the number in a variable

Do the same for the computer

Compare the two numbers, whose was bigger? Tell the user! And end the game

Now add functionality to the game. Let the User and the CPU roll until one gets to 30. The one that gets there first is the winner!

Bonus: Want to play again?
"""
from random import randint, seed
from time import time

seed(time())

def compare_nums(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return -1


def roll_dice() -> int:
    return randint(1, 6)


input("Are you ready to play? Press enter to start.")

name = input("What is your name? ")

end_game = False

while end_game is False:
    print("Rolling dice...")
    user_num = roll_dice()
    cpu_num = roll_dice()

    if compare_nums(user_num, cpu_num) == -1:
        print("You rolled the same number as the computer.")
    elif compare_nums(user_num, cpu_num) == user_num:
        print("You rolled a higher number than the computer!")
    else:
        print("You rolled a lower number than the computer.")

    print("Now try to roll up to 30 quicker than the computer. Press enter to roll dice. ")

    score_to_reach = 30
    score_reached = False

    user_score = 0
    cpu_score = 0

    while score_reached is False:
        user_input = input()

        if user_input == '':
            user_num = roll_dice()
            cpu_num = roll_dice()

        print(f"You rolled {user_num} and the computer rolled {cpu_num}.")

        user_score += user_num
        cpu_score += cpu_num

        if user_score >= score_to_reach or cpu_score >= score_to_reach:
            score_reached = True

            if user_score == cpu_score:
                print("\nIt's a tie. You and the computer reached a score of 30 at the same time.")
            elif user_score > cpu_score:
                print("\nYou win! You reached 30 before the computer.")
            else:
                print("\nYou lose. The computer reached 30 first.")

    user_input = input("\nPlay again? (y/n) ")

    if user_input == "n":
        end_game = True
