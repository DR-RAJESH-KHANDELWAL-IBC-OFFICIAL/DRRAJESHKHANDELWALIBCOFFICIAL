
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Sign-up request and response models.
"""

from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class SignUpResponse(BaseModel):
    success: bool
    message: str
    user_id: str | None = None
    display_name: str = "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑"
