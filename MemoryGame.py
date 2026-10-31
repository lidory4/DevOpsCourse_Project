import random
import time

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def show_sequence(sequence):
    print(sequence)
    time.sleep(0.7)

def clear_sequence():
    print("\033[A\033[K", end="")


def get_list_from_user(difficulty):
    while True:
        try:
            user_input = input("Write the numbers (the input format should be numbers separated by spaces): ")
            parts = user_input.split()
            player_numbers = []
            for part in parts:
                player_numbers.append(int(part))
            if len(parts) == difficulty:
                return player_numbers
        except ValueError:
            print("Please enter whole number only.") 
def is_list_equal(player_numbers, sequence):
    return player_numbers == sequence

def play(difficulty):
    sequence = generate_sequence(difficulty)
    show_sequence(sequence)
    clear_sequence()
    player_numbers = get_list_from_user(difficulty)
    return is_list_equal(player_numbers, sequence)