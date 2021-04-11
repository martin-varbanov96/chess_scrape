FROM python:3.8-alpine

EXPOSE 8000

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

ADD . /chess_games_ui

WORKDIR /chess_games_ui

RUN pip install django mysql mysqlclient

RUN python chess_games_ui/manage.py makemigrations

RUN python chess_games_ui/manage.py migrate

CMD [ "python", "chess_games_ui/manage.py", "runserver", "0.0.0.0:8000" ]
