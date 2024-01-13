FROM python:3.10-slim

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt update && apt install -y gnupg
RUN apt install -y nodejs
RUN apt install -y npm

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "app"]
