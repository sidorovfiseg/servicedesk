FROM python:3.12-slim

WORKDIR /opt/app-root/user-service/

COPY requirements.txt /opt/app-root/user-service/requirements.txt

RUN pip install --no-cache-dir -r /opt/app-root/user-service/requirements.txt

ENV PYTHONPATH /opt/app-root/user-service
ENV PYTHONBUFFERED=1

COPY entrypoint.sh /opt/app-root/user-service/entrypoint.sh
RUN chmod +x /opt/app-root/user-service/entrypoint.sh

# Определяем команду для запуска контейнера
CMD ["/opt/app-root/user-service/entrypoint.sh"]