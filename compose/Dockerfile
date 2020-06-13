FROM python:3.8.3-slim-buster

WORKDIR /app
RUN apt-get update && apt-get -y upgrade

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY src /app


COPY compose/run.sh /run.sh
RUN sed -i 's/\r//' /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
