FROM python:3.11-alpine

EXPOSE 5000

WORKDIR /app

COPY . .

RUN apk add --no-cache gcc musl-dev libffi-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del gcc musl-dev libffi-dev

CMD ["python", "run.py"]
