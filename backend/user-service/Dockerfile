FROM python:3.12-slim

WORKDIR /opt/app-root/user-service/

COPY requirements.txt /opt/app-root/user-service/requirements.txt

RUN pip install --no-cache-dir -r /opt/app-root/user-service/requirements.txt

ENV PYTHONPATH /opt/app-root/user-service
ENV PYTHONBUFFERED=1


# Определяем команду для запуска контейнера
CMD ["gunicorn", "--config", "/opt/app-root/user-service/app/config/gunicorn.conf.py"]

