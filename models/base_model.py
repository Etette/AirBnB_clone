#!/usr/bin/python3
"""
Module base_model
Base_model defines all common attributes
and methods for other classes
"""


import uuid
from models import storage
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
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], time)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], time)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        string representation of the BaseModel class
        """
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates the attribute update_at with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the keys/values of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
