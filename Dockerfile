FROM python:3.9

COPY ./web_app /web_app
COPY ./templates /templates
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

EXPOSE 80

CMD ["uvicorn", "web_app.main:app", "--host", "0.0.0.0", "--port", "80"]

