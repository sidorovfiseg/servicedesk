from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi_mail import ConnectionConfig


class SMTPConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SMTP_")
    
    SERVER: str
    PORT: int
    USER: str
    PASSWORD: str

smtp_config = SMTPConfig()
    
email_config = ConnectionConfig(
    MAIL_USERNAME=smtp_config.USER,
    MAIL_SERVER=smtp_config.SERVER,
    MAIL_PORT=smtp_config.PORT,
    MAIL_PASSWORD=smtp_config.PASSWORD,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    MAIL_FROM=smtp_config.USER,
    MAIL_FROM_NAME="Autopatent"
)