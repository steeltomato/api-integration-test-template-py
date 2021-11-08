FROM python:3.9-slim

WORKDIR /apitest

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

CMD pytest -vv --junitxml=C:\path\to\out_report.xml .
