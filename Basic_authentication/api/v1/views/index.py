#!/usr/bin/env python3
""" INDEX VIEWS
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      API STATUS
    """
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized
    Return:
      401 ERROR
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden
    Return:
      403 ERROR
    """
    abort(403)


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      NUMBER OF OBJECTS
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)