FROM python:3.10-slim

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y gnupg curl software-properties-common apt-transport-https
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y npm

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "app"]
