#!/usr/bin/python3
"""
Module user
Inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Public class attribute
        email: string - empty string
        password: string - empty string
        First_name: string - empty string
        Last_name: string - empty string
    """

    email = ""
    password = ""
    First_name = ""
    Last_name = ""
