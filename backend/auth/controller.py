
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Authentication controller.
"""

from backend.response import success_response, error_response


def signin_controller():
    return error_response(
        message="Sign-in service is not configured yet."
    )


def signup_controller():
    return error_response(
        message="Sign-up service is not configured yet."
    )


def forgot_password_controller():
    return error_response(
        message="Forgot password service is not configured yet."
    )


def reset_password_controller():
    return error_response(
        message="Reset password service is not configured yet."
    )
