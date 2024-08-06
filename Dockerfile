FROM python:3.9.6

WORKDIR /app

ENV BOT_TOKEN=DEFINE_TOKEN

COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

CMD [ "sh", "init.sh" ]