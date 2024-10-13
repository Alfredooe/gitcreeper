FROM python:3.12-slim-bookworm

ENV PYTHON_UNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apt update &&\
    apt install -y git &&\
    pip install --no-cache-dir -r requirements.txt &&\
    rm -rf /var/lib/apt/lists/*

COPY gitcreeper.py .

ENTRYPOINT ["python", "gitcreeper.py"]
