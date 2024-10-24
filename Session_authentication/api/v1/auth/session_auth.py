#!/usr/bin/env python3
"""
session authentication moduel
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create Session ID For User_id
        """
        if user_id is None or type(user_id) is not str:
            return None
        else:
            sessionID = str(uuid4())
            self.user_id_by_session_id[sessionID] = user_id
            return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None
        else:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        return User.get(self.user_id_for_session_id(session_id))

    def destroy_session(self, request=None):
        """deletes the user session and logout"""
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        session_id = self.session_cookie(request)
        if not self.user_id_for_session_id(session_id):
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
