from config.celery import celery
from config.email import email_config
from fastapi_mail import MessageSchema, FastMail
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

class EmailService:
    def __init__(self) -> None:
        self.fm = FastMail(config=email_config)
        self.env = Environment(loader=FileSystemLoader(str(Path(__file__).parent.parent / "templates")))
    
    @celery.task
    def send_verification_email(self, email_data):
        template = self.env.get_template("account-verification.html")
        message = MessageSchema(
            subject="Подтверждение вашего email",
            recipients=email_data["email"],
            body=template.render(),
            subtype="html"
        )
        self.fm.send_message(message=message)
        
    @celery.task
    def send_password_reset_email(self, email_data):
        template = self.env.get_template("password-reset.html")
        message = MessageSchema(
            subject="Сброс пароля",
            recipients=email_data["email"],
            body=template.render(),
            subtype="html"
        )
        self.fm.send_message(message=message)
        
        
email_service = EmailService()