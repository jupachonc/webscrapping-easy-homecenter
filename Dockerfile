FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host=0.0.0.0"]