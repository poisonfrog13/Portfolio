FROM python:3.11-bullseye

WORKDIR /app

COPY . .

RUN pip install poetry && pip install -r requirements.txt

RUN python manage.py collectstatic

CMD ["gunicorn", "--config", "gunicorn.conf.py", "server.wsgi:application" ]