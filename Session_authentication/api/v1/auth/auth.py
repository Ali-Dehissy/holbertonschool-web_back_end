#!/usr/bin/env python3
"""
API Auth
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Authethificaion
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Curret User
        """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a Req"""
        if request is None:
            return None
        if getenv('SESSION_NAME'):
            return request.cookies.get(getenv('SESSION_NAME'))
