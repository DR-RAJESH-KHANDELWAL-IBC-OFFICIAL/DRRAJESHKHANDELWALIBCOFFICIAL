
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Standard API response helpers.
"""

from typing import Any, Optional


def success_response(
    message: str,
    data: Optional[Any] = None,
) -> dict:
    return {
        "success": True,
        "message": message,
        "data": data,
        "brand": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
    }


def error_response(
    message: str,
    error: Optional[Any] = None,
) -> dict:
    return {
        "success": False,
        "message": message,
        "error": error,
        "brand": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
    }
