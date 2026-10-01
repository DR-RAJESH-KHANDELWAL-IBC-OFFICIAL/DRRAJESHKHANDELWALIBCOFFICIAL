from __future__ import annotations

from urllib.parse import quote

import requests

from flask import (
    Flask,
    jsonify,
    request,
    Response,
)


# ============================================================
# APPLICATION
# ============================================================

app = Flask(__name__)


# ============================================================
# SUPREME CENTRAL API
# ============================================================

SUPREME_API_URL = (
    "https://supremesetuhub-3v4e.onrender.com"
)


# ============================================================
# SUPREME CENTRAL FRONTEND
# ============================================================
# LIVE FRONTEND IS SERVED FROM SUPREMESETUHUB
#
# No local HTML/CSS duplication.
# ============================================================

SUPREME_FRONTEND_URL = (
    SUPREME_API_URL
    + "/api/v1/frontend/supreme"
)


# ============================================================
# HTTP SETTINGS
# ============================================================

REQUEST_TIMEOUT = (
    60,
    60,
)

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/154.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,*/*;q=0.8"
    ),
}


# ============================================================
# CORS
# ============================================================

@app.after_request
def after_request(response):

    response.headers[
        "Access-Control-Allow-Origin"
    ] = "*"

    response.headers[
        "Access-Control-Allow-Headers"
    ] = (
        "Content-Type,Authorization"
    )

    response.headers[
        "Access-Control-Allow-Methods"
    ] = (
        "GET,PUT,POST,DELETE,OPTIONS"
    )

    return response


# ============================================================
# HOME PAGE
# ============================================================
# The home page loads the LIVE SUPREMESETUHUB frontend.
#
# IMPORTANT:
# The connection JSON is NOT returned from "/".
# ============================================================

@app.get("/")
def root():

    try:

        response = requests.get(
            SUPREME_FRONTEND_URL,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
        )

        content_type = response.headers.get(
            "Content-Type",
            "text/html; charset=utf-8",
        )

        return Response(
            response.content,
            status=response.status_code,
            content_type=content_type,
        )

    except requests.exceptions.Timeout:

        return jsonify({
            "success": False,
            "error": "SUPREME_FRONTEND_TIMEOUT",
            "message": (
                "SUPREMESETUHUB frontend "
                "did not respond within the timeout."
            ),
            "frontend_source": (
                SUPREME_FRONTEND_URL
            ),
        }), 502

    except requests.exceptions.ConnectionError as exc:

        return jsonify({
            "success": False,
            "error": "SUPREME_FRONTEND_CONNECTION_ERROR",
            "message": str(exc),
            "frontend_source": (
                SUPREME_FRONTEND_URL
            ),
        }), 502

    except requests.RequestException as exc:

        return jsonify({
            "success": False,
            "error": "SUPREME_FRONTEND_REQUEST_ERROR",
            "message": str(exc),
            "frontend_source": (
                SUPREME_FRONTEND_URL
            ),
        }), 502


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    return jsonify({

        "service": (
            "DRRAJESHKHANDELWALIBCOFFICIAL"
        ),

        "status": "healthy",

        "connected_to": (
            "SUPREMESETUHUB"
        ),

        "frontend_source": (
            SUPREME_FRONTEND_URL
        ),

        "architecture": (
            "SUPREME CENTRAL FRONTEND"
        ),

    }), 200


# ============================================================
# SUPREME CONNECTION
# ============================================================
# This endpoint is ONLY for connection information.
#
# It is intentionally separate from "/".
# ============================================================

@app.get("/supreme/connection")
def supreme_connection():

    return jsonify({

        "connected_to": (
            "SUPREMESETUHUB"
        ),

        "identity": (
            "👑 DR RAJESH KHANDELWAL IBC 👑"
        ),

        "message": (
            "👑 DR RAJESH KHANDELWAL IBC "
            "- Supreme Identity Profile 👑"
        ),

        "status": "ACTIVE",

    }), 200


# ============================================================
# SUPREME BRIDGE
# ============================================================

def call_supreme(endpoint: str):

    url = (
        SUPREME_API_URL.rstrip("/")
        + endpoint
    )

    try:

        response = requests.get(
            url,
            headers=REQUEST_HEADERS,
            timeout=(15, 30),
            allow_redirects=True,
        )

        try:

            payload = response.json()

        except ValueError:

            payload = {

                "error": (
                    "SUPREME returned "
                    "a non-JSON response"
                ),

                "status_code": (
                    response.status_code
                ),

                "content_type": (
                    response.headers.get(
                        "Content-Type",
                        ""
                    )
                ),

                "text": (
                    response.text[:2000]
                ),

            }

        return (
            response.status_code,
            payload,
        )

    except requests.exceptions.Timeout:

        return (
            504,
            {
                "error": (
                    "SUPREME request timeout"
                ),
                "upstream": (
                    SUPREME_API_URL
                ),
            },
        )

    except requests.exceptions.ConnectionError as exc:

        return (
            502,
            {
                "error": (
                    "SUPREME connection error"
                ),
                "message": str(exc),
                "upstream": (
                    SUPREME_API_URL
                ),
            },
        )

    except requests.RequestException as exc:

        return (
            502,
            {
                "error": str(exc),
                "upstream": (
                    SUPREME_API_URL
                ),
            },
        )


# ============================================================
# SUPREME STATUS
# ============================================================

@app.get("/supreme/bridge/status")
def bridge_status():

    status_code, payload = call_supreme(
        "/supreme/status"
    )

    return jsonify({

        "service": (
            "DRRAJESHKHANDELWALIBCOFFICIAL"
        ),

        "status": (
            "healthy"
            if status_code == 200
            else "bridge_error"
        ),

        "upstream": payload,

    }), status_code


# ============================================================
# SUPREME PROFILE
# ============================================================

@app.get("/supreme/bridge/profile")
def bridge_profile():

    status_code, payload = call_supreme(
        "/supreme/profile"
    )

    return jsonify({

        "service": (
            "DRRAJESHKHANDELWALIBCOFFICIAL"
        ),

        "status": (
            "healthy"
            if status_code == 200
            else "bridge_error"
        ),

        "profile": payload,

    }), status_code


# ============================================================
# SUPREME SEARCH
# ============================================================

@app.get("/supreme/bridge/search")
def bridge_search():

    query = request.args.get(
        "q",
        "",
    ).strip()

    if not query:

        return jsonify({
            "error": (
                "Missing q parameter"
            ),
        }), 400

    encoded_query = quote(
        query,
        safe="",
    )

    status_code, payload = call_supreme(
        "/supreme/search?q="
        + encoded_query
    )

    return jsonify({

        "service": (
            "DRRAJESHKHANDELWALIBCOFFICIAL"
        ),

        "status": (
            "healthy"
            if status_code == 200
            else "bridge_error"
        ),

        "results": payload,

    }), status_code


# ============================================================
# 404 ERROR
# ============================================================

@app.errorhandler(404)
def not_found(error):

    return jsonify({

        "error": "Not found",

        "message": (
            "The requested endpoint "
            "does not exist"
        ),

    }), 404


# ============================================================
# 500 ERROR
# ============================================================

@app.errorhandler(500)
def server_error(error):

    return jsonify({

        "error": "Server error",

        "message": (
            "Internal server error"
        ),

    }), 500


# ============================================================
# LOCAL RUN
# ============================================================

if __name__ == "__main__":

    import os

    port = int(
        os.getenv(
            "PORT",
            "10000",
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
    )
