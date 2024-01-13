FROM python:3.10-slim

WORKDIR app/

COPY requirements.txt requirements.txt

COPY ./nodejs /usr/bin/nodejs
COPY ./node /usr/bin/node
COPY ./npm /usr/bin/npm
COPY ./nodejs_modules /usr/lib/nodejs

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "app"]
