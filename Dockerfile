FROM python:3

WORKDIR /usr/src/app

RUN pip install requests

COPY ./getweather.py .

CMD [ "python", "./getweather.py" ]