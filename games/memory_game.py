import random
import time
import os

name = "Memory Game"
dis = "a list of numbers will appear for 1 second and you have to guess it back"


def generate_list(difficulty_lv):
    return [random.randint(1, 101) for _ in range(difficulty_lv)]


def get_guess_from_user(player_name, difficulty_lv):
    user_list = []
    for _ in range(0, difficulty_lv):
        user_number = input(f'{player_name}, enter your guess (numbers only):')
        if user_number.isdigit():
            user_list.append(int(user_number))
        else:
            print("Please guess a number")
    return user_list


def compare_results(generated_number, user_guess):
    return generated_number == user_guess


def play(player_name, difficulty_lv):
    generated_list = generate_list(difficulty_lv)
    print("Memorize the sequence...")
    print(generated_list)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_guess = get_guess_from_user(player_name, difficulty_lv)

    return compare_results(generated_list, user_guess)

