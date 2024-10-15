#!/usr/bin/env python3
"""BASIC AUTH
"""
from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple
import base64
from models.user import User


class BasicAuth(Auth):
    """BASIC AUTH"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """BASE 64 return"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.split(' ')[0] != 'Basic':
            return None
        else:
            return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """BASE 64 method retun"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            in_bytes = base64.b64decode(base64_authorization_header)
            return in_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """USER MAIL RETURN"""
        if not decoded_base64_authorization_header:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            first_item = decoded_base64_authorization_header.split(':')[0]
            last_item = decoded_base64_authorization_header.split(':')[1]
            return (first_item, last_item)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """RETURN USER INSTANCE"""
        if not isinstance(user_email, str) or user_email is None:
            return None
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None
        attr = {'email': user_email}
        u = User()
        if not u.search(attr):
            return None
        user = u.search(attr)[0]
        if not user:
            return None
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """CURRENT USER"""
        auth_val = self.authorization_header(request)
        coded = self.extract_base64_authorization_header(auth_val)
        decoded = self.decode_base64_authorization_header(coded)
        user = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(user[0], user[1])