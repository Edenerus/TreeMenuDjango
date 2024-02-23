FROM python:3.10 as app

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app/

COPY requirements.txt .

RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY app .

COPY entrypoint.sh .

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "-w", "4", "-b", "0.0.0.0:8000"]
