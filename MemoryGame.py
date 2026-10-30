import random
import os
import time

def generate_sequence(difficulty):
    sequence = []
    for i in range(difficulty):
        sequence.append(random.randint(1, 101))
    return sequence

def clear_sequence():
    print("\033[A\033[K", end="")

def show_sequence(sequence):
    print(sequence)
    time.sleep(0.7)
    clear_sequence()

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
            print("please enter whole number only") 
def is_list_equal(player_numbers, sequence):
    return player_numbers == sequence

print(is_list_equal([12, 7, 12], [12, 7, 12]))
print(is_list_equal([12, 7, 12], [7, 12, 12]))

#print(get_list_from_user(3))
#numbers = generate_sequence(2)
#show_sequence(numbers)
#clear_sequence()
