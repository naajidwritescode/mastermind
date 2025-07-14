# Generate a 4 color random code
# Give 6 color options
# Set a guess limit
# Allow the user to choose
# Check if they input is in a correct format
# Compare if they chose correct:
# Show current and incorrect positions as a hint
# If the digit/letter does not exist Current and Incorrect position = 0
# Show the result:
# If they chose correctly ----> win
# Give up/ exceed guess limit ----> lose
# Option to play again

# Learnings
# spilt method changes a string into a list based on a specified interval
# Continue means skip rest of the code in the loop
# for-else occurs when the loop doesn't iterate or there is a break, in that case else is executed.
# Zip: Makes two lists into tuples and compares the invidual items


import random

COLOR = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        random_code = random.choice(COLOR)
        code.append(random_code)
    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().strip().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Must guess {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLOR:
                print(f"Invalid color {color}. Try again")
                break
        else:
            break
    return guess


def check_code(guess, real_code):
    # check correct position

    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(
        f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print(
        f"Guess the code, length is {CODE_LENGTH} colors, choices are ['R', 'G', 'B', 'Y', 'W', 'O']")
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed in {attempts} tries.")
            break
        print(
            f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")
    else:
        print(f"You are out of attempts, code was {code}")


if __name__ == "__main__":
    game()
