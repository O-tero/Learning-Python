FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install python dependencies
COPY requirements.txt /app/pipfile
RUN pip install --upgrade pip
RUN pipenv install --no-cache-dir -r pipfile

# run migrations

RUN pipenv install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "executable" ]["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
