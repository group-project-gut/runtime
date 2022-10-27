#Deriving the latest base image
FROM python:3.10-slim-buster

WORKDIR /

COPY "containers/entrypoint.sh" ./
COPY "main.py" "/runtime/main.py"
COPY "src" "/runtime/src"

ENTRYPOINT [ "/entrypoint.sh" ]
