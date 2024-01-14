#!/usr/bin/python3
"""
Module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that handles users' information
    """
    def __init__(self)
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
