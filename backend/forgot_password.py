
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Forgot password request and response models.
"""

from pydantic import BaseModel, EmailStr


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ForgotPasswordResponse(BaseModel):
    success: bool
    message: str


def create_forgot_password_response(
    success: bool,
    message: str,
) -> ForgotPasswordResponse:
    return ForgotPasswordResponse(
        success=success,
        message=message,
    )
