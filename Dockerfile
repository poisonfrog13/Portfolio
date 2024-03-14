FROM python:3.11-bullseye

WORKDIR /app

COPY . .

RUN pip install poetry && pip install -r requirements.txt

RUN python manage.py collectstatic

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]