FROM python:3.10-slim

WORKDIR app/

COPY requirements.txt requirements.txt

COPY /usr/bin/node /usr/bin/node
COPY /usr/bin/nodejs /usr/bin/nodejs
COPY /usr/bin/npm /usr/bin/npm
COPY /usr/lib/nodejs /usr/lib/nodejs

RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-warn-script-location --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "app"]
