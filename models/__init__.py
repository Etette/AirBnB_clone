#!/usr/bin/python3
"""
Init file for models package
Create variable storage instance of file storage
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
