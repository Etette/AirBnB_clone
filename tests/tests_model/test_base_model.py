#!/usr/bin/python3
"""
Module test_base_model
Contains test for models.base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """
    Automated tests for basemodel
    """
    def test_obj_to_dict(self):
        """
        Should convert an object to a dictionary
        """
        model = BaseModel()
        dic = model.to_dict()

        self.assertTrue(type(dic), dict)
        self.assertIn("id", dic)
        self.assertIn("__class__", dic)
        self.assertIn("updated_at", dic)
        self.assertIn("created_at", dic)

    def test_init_values(self):
        """
        Should initialize base model with correct variable types
        """
        model = BaseModel()
        model.name = "Nehe"
        model.my_number = 99

        self.assertTrue(type(model.name), str)
        self.assertTrue(type(model), BaseModel)
        self.assertTrue(type(model.id), str)
        self.assertTrue(type(model.created_at), datetime)
        self.assertTrue(type(model.updated_at), datetime)
        self.assertTrue(model.name, "Nehe")
        self.assertTrue(model.my_number, 99)

    def test_kwargs(self):
        """
        Should create object using kwargs
        """
        model = BaseModel()
        dic = model.to_dict()
        base = BaseModel(dic)

        self.assertIsNotNone(base.id)
        self.assertTrue(type(base.id), str)
        self.assertTrue(type(base.created_at), datetime)
        self.assertTrue(type(base.created_at), datetime)
        self.assertTrue(type(base), BaseModel)

    def test_save_obj(self):
        """
        Should save a base model and change updated_at
        """
        model = BaseModel()
        self.assertNotEqual(model.created_at, model.updated_at)
        val1 = model.updated_at
        model.save()
        val2 = model.updated_at
        self.assertNotEqual(val1, val2)

    def test_base_has_methods(self):
        """
        Base model should have __init__, save __str__,
        to_dict methods
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_str_method(self):
        """"
        Should return proper string from __str__
        """
        model = BaseModel()
        s = model.__str__()
        self.assertIn("id", s)
        self.assertIn("created_at", s)
        self.assertIn("updated_at", s)
        self.assertIn("[BaseModel]", s)
        self.assertTrue(type(s), str)
        self.assertIsNotNone(s)


if __name__ == "__main__":
    unittest.main()
