#!/usr/bin/python3
"""
Module base_model
Base_model defines all common attributes
and methods for other classes
"""


import models
from uuid import uuid4
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    defines the attributes required
    by the base model
    Attributes:
        __init__(self, *args, **kwargs)
        __str__(self)
        save(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the base_model
        accepts args and kwargs
        uid is a uuid of type str
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                            kwargs["created_at"], time)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                            kwargs["updated_at"], time)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the BaseModel class
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """
        updates the attribute update_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
