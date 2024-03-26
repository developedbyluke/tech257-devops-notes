# User story 1
# As a user, I want to be able to guess a number and know if I got it correct or not, so that I can know if I won or not.

# Define/assign number to a variable called magic_number
magic_number = 24

# Ask user for input
guess = input("Guess the magic number: ")

# Check if this input matches a magic_number
is_correct = guess == magic_number

# Let the user know if the response was correct or not
if is_correct:
    print("You guessed the magic number!")
else:
    print("That isn't the magic number.")

# Allow the user 5 guesses
guesses = 1

while guesses < 5:
    guess = input(f"You have {5 - guesses} guesses remaining: ")

    if guess == magic_number:
        print("You guessed the magic number!")
        break

    guesses += 1

    if guesses == 5:
        print("You didn't guess the magic number...")
