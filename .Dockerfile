FROM python:3.8.3

ENV APP_ENVIRONMENT=production

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

RUN mkdir -p /src

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "bash" ]

CMD [ "./dockerStartServer.sh" ]