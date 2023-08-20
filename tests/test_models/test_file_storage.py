#!/usr/bin/python3
"""Testing FileStorage module"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """testing class for file storage"""
    def setUp(self):
        """Set up testing environment"""
        self.storage = FileStorage()

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

    def test_reload(self):
        """Test the reload() method of FileStorage"""
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_save(self):
        """Test the save() method of FileStorage"""
        pass
