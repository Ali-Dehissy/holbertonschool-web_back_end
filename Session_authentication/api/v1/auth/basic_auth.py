#!/usr/bin/env python3
"""
basic auth
"""
import base64
from email.header import decode_header
from email.mime import base
from typing import Tuple
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    basic Auth
    """

    def extract_base64_authorization_header(self, authorization_header: str
                                            ) -> str:
        """
        return base64 auth header
        """
        if authorization_header is None:
            return None
        elif isinstance(authorization_header, str) is False:
            return None
        elif authorization_header[0:6] != "Basic ":
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        return decode value utf-8 string
        """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return base64.b64decode(base64_authorization_header
                                    ).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        return user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if decoded_base64_authorization_header.__contains__(":") is False:
            return None, None
        user_Credentials = decoded_base64_authorization_header.split(":")
        return (user_Credentials[0], user_Credentials[1])

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        """
        if (type(user_email) is not str or type(user_pwd) is not str):
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        if user[0].is_valid_password(user_pwd) and user:
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        return current user
        """
        try:
            header = self.authorization_header(request)
            base64_auth = self.extract_base64_authorization_header(header)
            decode_header = self.decode_base64_authorization_header(
                base64_auth)
            user_credentials = self.extract_user_credentials(
                decode_header)
            return self.user_object_from_credentials(
                user_credentials[0], user_credentials[1])
        except Exception:
            return None
