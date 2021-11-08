FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9 as runtime

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn --host 0.0.0.0 main:app
