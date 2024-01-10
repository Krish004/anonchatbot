FROM alpine

RUN apk add --no-cache tzdata

ENV TZ=Europe/Kiev

WORKDIR /home/tg

COPY ./ /home/tg

RUN apk add python3

RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED

RUN python -m ensurepip --upgrade \
&& pip3 install -r requirements.txt


CMD python3 main.py
