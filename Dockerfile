#Deriving the latest base image
FROM python:3.10-slim-buster

WORKDIR /

COPY "main.py" "/runtime/main.py"
COPY "requirements.txt" "/runtime/requirements.txt"
COPY "src" "/runtime/src"

RUN pip install -r /runtime/requirements.txt

ENTRYPOINT [ "/runtime/main.py" ]
