FROM python:3

RUN mkdir -p /usr/src/bot

RUN python3 -m pip install -U discord.py selenium beautifulsoup4

WORKDIR /usr/src/bot

COPY . .

CMD [ "python3", "main.py" ]