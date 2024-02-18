import random
from currency_converter import CurrencyConverter


name = "Currency Roulette"
dis = "try and guess the value of a random amount of USD in ILS"


def generate_number():
    _lower_bound = 1
    _upper_bound = 100

    return random.randrange(_lower_bound, _upper_bound)


def get_money_interval():
    _exchange_rate = CurrencyConverter().convert(1, 'USD', 'ILS')
    _random_usd = generate_number()
    print(f'The amount is ${_random_usd}')

    return round(_random_usd * _exchange_rate)


def get_guess_from_user(player_name):
    _is_error = True
    while _is_error:
        user_number = input(f'{player_name}, enter your guess in ILS (numbers only):')
        if user_number.isdigit():
            return int(user_number)


def compare_results(generated_number, difficulty_lv, user_guess):
    _gap = 10 - difficulty_lv
    return generated_number - _gap <= user_guess <= generated_number + _gap


def play(player_name, difficulty_lv):
    generated_number = get_money_interval()

    if isinstance(generated_number, str):
        print(generated_number)
        return

    user_guess = get_guess_from_user(player_name)
    return compare_results(generated_number, difficulty_lv, user_guess)
