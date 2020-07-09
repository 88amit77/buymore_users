FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

CMD ["cp", "serializers.py", "/usr/local/lib/python3.8/site-packages/djoser/serializers.py"]
