#!/usr/bin/python3
"""
Module review
Inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attribute
        place_id: string - empty string
        user_id: string - empty string
        text: string empty string
    """
    place_id = ""
    user_id = ""
    text = ""
