from flask import Flask
from utilities.score import get_score

app = Flask(__name__)


@app.route('/')
def score_server():
    score = get_score()
    if score == "File Error":
        with open("html/error_template.html", "r") as error_template_file:
            html_response = error_template_file.read().format(ERROR=score)
    else:
        with open("html/score_template.html", "r") as score_template_file:
            html_response = score_template_file.read().format(SCORE=score)
    return html_response


if __name__ == '__main__':
    app.run(debug=True)
