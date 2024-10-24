#!/usr/bin/env python3
"""
new Flask view that handles all routes for the Session authentication.
"""
from flask import Flask, request, jsonify, abort
from api.v1.views import app_views
import os
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    handles all routes for the Session authentication
    """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400
    if pwd is None or len(pwd) == 0:
        return jsonify({"error": "password missing"}), 400

    try:
        search = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not search:
        return jsonify({"error": "no user found for this email"}), 404
    for user in search:
        if user.is_valid_password(pwd) is True:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            cookie = os.getenv('SESSION_NAME')
            response = jsonify(user.to_json())
            response.set_cookie(cookie, session_id)
            return response
        else:
            return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """
    Delete auth session and logout
    """
    from api.v1.app import auth

    deleted = auth.destroy_session(request)
    if not deleted:
        abort(404)

    return jsonify({}), 200
