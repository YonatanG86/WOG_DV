import random

name = "Guess Game"
dis = "guess a random number according to the difficulty"


def generate_number(difficulty_lv):
    _lower_bound = 10 ** (difficulty_lv - 1)
    _upper_bound = (10 ** difficulty_lv) - 1

    return random.randrange(_lower_bound, _upper_bound + 1)


def get_guess_from_user(player_name):
    _is_error = True
    while _is_error:
        user_number = input(f'{player_name}, enter your guess (numbers only):')
        if user_number.isdigit():
            return int(user_number)


def compare_results(generated_number, user_guess):
    return generated_number == user_guess


def play(player_name, difficulty_lv):
    generated_number = generate_number(difficulty_lv)
    user_guess = get_guess_from_user(player_name)

    return compare_results(generated_number, user_guess)

