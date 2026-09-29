
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Sign-in request and response models.
"""

from pydantic import BaseModel


class SignInRequest(BaseModel):
    username: str
    password: str


class SignInResponse(BaseModel):
    success: bool
    message: str
    access_token: str | None = None
    token_type: str = "bearer"


def create_signin_response(
    success: bool,
    message: str,
    access_token: str | None = None,
) -> SignInResponse:
    return SignInResponse(
        success=success,
        message=message,
        access_token=access_token,
    )
