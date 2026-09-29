
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Application metadata.
"""

from backend.constants import BACKEND_NAME, BACKEND_VERSION, BACKEND_STATUS


APP_METADATA = {
    "name": BACKEND_NAME,
    "version": BACKEND_VERSION,
    "status": BACKEND_STATUS,
    "brand": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
    "platform": "DRRAJESHKHANDELWALIBCOFFICIAL",
    "central_hub": "SUPREMESETUHUB",
}


def get_metadata() -> dict:
    return APP_METADATA.copy()
