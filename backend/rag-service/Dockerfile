FROM python:3.11-slim

WORKDIR /opt/app-root/rag-service/

COPY requirements.txt /opt/app-root/rag-service/requirements.txt

RUN pip install --no-cache-dir -r /opt/app-root/rag-service/requirements.txt

COPY . /opt/app-root/rag-service/

ENV PYTHONPATH /opt/app-root/rag-service
ENV PYTHONUNBUFFERED=1



CMD ["gunicorn", "--config", "/opt/app-root/rag/app/config/gunicorn.conf.py"]