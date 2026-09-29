
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Brand profile API routes.
"""

from flask import Blueprint, jsonify

profile_bp = Blueprint(
    "profile",
    __name__,
    url_prefix="/api/profile",
)


@profile_bp.route("/", methods=["GET"])
def get_profile():
    return jsonify({
        "success": True,
        "display_name": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
        "status": "ACTIVE",
        "platform": "DRRAJESHKHANDELWALIBCOFFICIAL",
        "connected_to": "SUPREMESETUHUB",
    }), 200
