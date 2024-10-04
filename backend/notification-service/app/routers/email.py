from fastapi import APIRouter
from schemas.email import VerificationRequest, PasswordResetRequest
from tasks.email import email_service

router = APIRouter()

@router.post("/verification")
async def send_verification_email(email_data: VerificationRequest):
    email_service.send_verification_email.delay(email_data)
    
    
@router.post("password-reset")
async def create_password_reset(email_data: PasswordResetRequest):
    email_service.send_password_reset_email.delay(email_data)