FROM python:3.11
RUN apt-get update
ADD . /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./

COPY ./entrypoint.sh ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
