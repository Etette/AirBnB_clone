#!/usr/bin/python3
"""
Init file for models package
Create variable storage instance of file storage
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
