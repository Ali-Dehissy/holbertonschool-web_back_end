#!/usr/bin/env python3
"""
API ROUTE
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = getenv('AUTH_TYPE')
if auth:
    from api.v1.auth.auth import Auth
    auth = Auth()
    if getenv('AUTH_TYPE') == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """EMPTY HANDLER
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """AUTORIZATION HANDLER
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """FORBIDDEN HANDLER
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """REQUEST FILTERS """
    paths = ['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if auth is None:
        return
    if auth.require_auth(request.path, paths) is False:
        return
    if auth.authorization_header(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)