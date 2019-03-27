FROM python:3.7.2-alpine
COPY ./src/requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /src
WORKDIR /src
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]