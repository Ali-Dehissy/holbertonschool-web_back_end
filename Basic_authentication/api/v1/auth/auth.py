#!/usr/bin/env python3
"""AUTH
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """API AUTH
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """PUBLIC"""
        special_character: str = '/'
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        last_item = path[-1]
        if last_item not in special_character:
            path += '/'
            if path in excluded_paths:
                return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """AUTHORIZATION HANDLER"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """CURRENT USER"""
        return None