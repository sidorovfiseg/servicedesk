from pydantic import BaseModel, EmailStr

class VerificationRequest(BaseModel):
    email: EmailStr
    link: str


class PasswordResetRequest(BaseModel):
    email: EmailStr
    link: str