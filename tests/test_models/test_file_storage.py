#!/usr/bin/python3
"""Testing FileStorage module"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """testing class for file storage"""
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """testing the returned __objects"""
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """Testing if the object is added"""
        initial_count = len(self.storage.all())
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), initial_count + 1)
        self.assertIn(obj, self.storage.all().values())
