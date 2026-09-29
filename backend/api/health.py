
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Health check API route.
"""

from flask import Blueprint, jsonify
from datetime import datetime, timezone

health_bp = Blueprint(
    "health",
    __name__,
    url_prefix="/api/health",
)


@health_bp.route("/", methods=["GET"])
def health_check():
    return jsonify({
        "success": True,
        "status": "HEALTHY",
        "brand": "👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }), 200
