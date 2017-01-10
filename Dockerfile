FROM python:2.7

ADD ./ /app

RUN pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 80

CMD python app.py
