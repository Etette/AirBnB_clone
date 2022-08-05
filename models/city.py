#!/usr/bin/python3
"""
Module city
Inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attribute
        state_id : string
        name : empty string
    """

    name = ""
    state_id = ""
