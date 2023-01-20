FROM alpine:latest

RUN mkdir -p /usr/src/bot

RUN apk add python3 firefox py3-pip

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz && \
    tar zxvf geckodriver-v0.30.0-linux32.tar.gz && \
    cp geckodriver /usr/local/bin/

RUN pip install -U discord.py selenium requests lxml mysql-connector-python

WORKDIR /usr/src/bot

COPY src .

CMD [ "python3", "main.py" ]