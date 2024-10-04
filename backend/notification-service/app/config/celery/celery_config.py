from pydantic_settings import BaseSettings, SettingsConfigDict
from celery import Celery

class CeleryConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="CELERY_")
    
    BROKER_URL: str
    RESULT_BACKEND: str
    
    
celery_config = CeleryConfig()

celery = Celery(
    "email_service",
    broker=celery_config.BROKER_URL,
    backend=celery_config.RESULT_BACKEND
)

celery.conf.update(
    task_routes={
        "tasks.send_verification_email": {"queue": "emails"},
        "tasks.send_password_reset_email": {"queue": "emails"},
    },
    task_serializer='json',
    accept_content=['json'],  # Указываем типы данных, которые принимает Celery
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)