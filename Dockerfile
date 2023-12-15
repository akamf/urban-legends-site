FROM python:alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY /app/requirements.txt requirements.txt
RUN  python3 -m pip install --upgrade pip && \
     python3 -m pip install -r requirements.txt

COPY /app/. .

EXPOSE 5000

CMD [ "gunicorn", "wsgi:app", "-b", "0.0.0.0:5000" ]
