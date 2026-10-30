import random

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess <= difficulty and guess >= 1:
                return guess
            else:
                print("Choose a number from 1 to " + str(difficulty))
        except ValueError:
            print("Please enter valid input")

def compare_results(secret_number,guess):
    return secret_number == guess

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number,guess)
