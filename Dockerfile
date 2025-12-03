FROM python:latest
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["tail", "-f", "/dev/null"]
