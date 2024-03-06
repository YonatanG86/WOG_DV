from flask import Flask
from utilities.score import get_score, signal_handler
from utilities.utils import BAD_RETURN_CODE
import signal

app = Flask(__name__)


signal.signal(signal.SIGINT, signal_handler)


@app.route('/')
def score_server():
    score = get_score()
    if score == BAD_RETURN_CODE:
        _error_msg = "File not found"
        with open("html/error_template.html", "r") as error_template_file:
            html_response = error_template_file.read().format(ERROR=_error_msg)
    else:
        with open("html/score_template.html", "r") as score_template_file:
            html_response = score_template_file.read().format(SCORE=score)
    return html_response


if __name__ == '__main__':
    app.run(debug=True)
