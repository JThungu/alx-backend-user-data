#!/usr/bin/env python3
""" User Session Module
"""
from typing import TypeVar, List, Iterable
from os import path
from models.base import Base
import uuid
import json


class UserSession(Base):
    """ Class User Session """
    def __init__(self, *args: list, **kwargs: dict):
        """ Initializes UserSession """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
