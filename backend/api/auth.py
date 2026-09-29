
"""
👑 DR RAJESH KHANDELWAL IBC OFFICIAL 👑
Authentication API routes.
"""

from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/signin", methods=["POST"])
def signin():
    return jsonify({
        "success": False,
        "message": "Sign-in service is not configured yet.",
    }), 501


@auth_bp.route("/signup", methods=["POST"])
def signup():
    return jsonify({
        "success": False,
        "message": "Sign-up service is not configured yet.",
    }), 501


@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    return jsonify({
        "success": False,
        "message": "Forgot password service is not configured yet.",
    }), 501


@auth_bp.route("/reset-password", methods=["POST"])
def reset_password():
    return jsonify({
        "success": False,
        "message": "Reset password service is not configured yet.",
    }), 501
