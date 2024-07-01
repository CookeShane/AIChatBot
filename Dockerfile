FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["sh", "-c", "\
    python AIChatBot/manage.py makemigrations \
    python AIChatBot/manage.py migrate \
    python AIChatBot/manage.py populate_db \
    python AIChatBot/manage.py runserver 0.0.0.0:8000"]