FROM python:3.10-slim-buster
LABEL maintainer="sa5mchavez"
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000
EXPOSE 5432

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]