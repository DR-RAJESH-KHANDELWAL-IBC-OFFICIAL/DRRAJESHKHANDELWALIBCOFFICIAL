
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Reset password request and response models.
"""

from pydantic import BaseModel


class ResetPasswordRequest(BaseModel):
    email: str
    reset_token: str
    new_password: str


class ResetPasswordResponse(BaseModel):
    success: bool
    message: str


def create_reset_password_response(
    success: bool,
    message: str,
) -> ResetPasswordResponse:
    return ResetPasswordResponse(
        success=success,
        message=message,
    )
