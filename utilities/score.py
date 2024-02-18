import os
from utilities.utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def _calculate_points(difficulty):
    return difficulty * 3 + 5


def add_score(difficulty):
    _score_from_file = get_score()
    _current_score = 0 if _score_from_file == 'File Error' else _score_from_file
    _current_score += _calculate_points(difficulty)

    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(_current_score))


def get_score():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    else:
        current_score = BAD_RETURN_CODE

    return current_score
