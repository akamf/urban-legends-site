FROM python:alpine

WORKDIR /app

COPY /app/.env .env

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY /app/requirements.txt requirements.txt
RUN  python3 -m pip install --upgrade pip && \
     python3 -m pip install -r requirements.txt

COPY /app/. .

EXPOSE 5000

# CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app:app" ]
CMD [ "python3", "app.py"]
