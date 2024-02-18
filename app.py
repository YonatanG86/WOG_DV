import os

import games.guess_game as guess_game_f
import games.currency_roulette_game as currency_roulette_game_f
import games.memory_game as memory_game_f
from utilities.utils import screen_cleaner
from utilities.score import add_score


memory_game = {
    'name': memory_game_f.name,
    'dis': memory_game_f.dis,
    'run': memory_game_f.play
}
guess_game = {
    'name': guess_game_f.name,
    'dis': guess_game_f.dis,
    'run': guess_game_f.play
}
currency_game = {
    'name': currency_roulette_game_f.name,
    'dis': currency_roulette_game_f.dis,
    'run': currency_roulette_game_f.play
}

games = [memory_game, guess_game, currency_game]



def print_games():
    for index, game in enumerate(games):
        print(f'{index + 1} - {game["name"]} - {game["dis"]}')


def welcome():
    print(f'welcome to the World of Games: The Epic Journey')


def difficulty_lv(player_name):
    _difficulty_lv = 0
    while not (0 < _difficulty_lv < 6):
        _difficulty_lv = input(f'{player_name}, please select a difficulty level between 1 to 5: ')

        if not _difficulty_lv.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        _difficulty_lv = int(_difficulty_lv)

    return _difficulty_lv


def start_play():

    _player_name = input("What is your name? ")
    _player_name = "\033[1;31m" + _player_name + "\033[0m"

    _player_input_str = "None"
    _game_won = -1

    while _player_input_str.lower() != 'exit':

        print_games()

        _player_input_str = input(f'{_player_name}, choose a game you want to play (enter a number or exit): ')

        if not _player_input_str.isdigit():
            screen_cleaner()
            continue

        game_index = int(_player_input_str) - 1

        if 0 <= game_index < len(games):
            game_difficulty_lv = difficulty_lv(_player_name)
            _game_won = games[game_index]["run"](_player_name, game_difficulty_lv)
            screen_cleaner()

            if _game_won:
                add_score(game_difficulty_lv)
                print(f'Congratulation {_player_name}, you have a WON ')
            else:
                print(f'Better luck next time, {_player_name}. ')

    print("Goodbye")

