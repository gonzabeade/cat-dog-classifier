FROM python:3.8

RUN mkdir -p /app

EXPOSE 8080

COPY ["main.py", "requirements.txt", "/app/"]
ADD models/my-model /app/model

RUN python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/main.py", "0.0.0.0", "8080", "/app/model"]

# python /app/main.py 127.0.0.1 8000 /app/model/my-model