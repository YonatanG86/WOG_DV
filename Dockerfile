FROM python:3.9-slim
RUN pip3 install Flask

WORKDIR /app

COPY html /html
COPY static /static
COPY main_score.py /main_score.py
COPY Scores.txt /Scores.txt

EXPOSE 8777

CMD ["flask", "run"]