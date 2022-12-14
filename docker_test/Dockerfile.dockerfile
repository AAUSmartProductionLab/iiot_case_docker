FROM python:3.10

ADD main.py .

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3 -m pip install -r /app/requirements.txt

COPY . /app

CMD ["python", "./main.py"]

