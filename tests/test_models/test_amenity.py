#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    my_amenity = Amenity()

    def test_class_exists(self):
        """tests class existance"""
        cls = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.my_amenity)), cls)

    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.my_amenity, Amenity)

    def testHasAttributes(self):
        """verifying attributes"""
        self.assertTrue(hasattr(self.my_amenity, 'name'))
        self.assertTrue(hasattr(self.my_amenity, 'id'))
        self.assertTrue(hasattr(self.my_amenity, 'created_at'))
        self.assertTrue(hasattr(self.my_amenity, 'updated_at'))

    def test_types(self):
        """testing the type of attributes"""
        self.assertIsInstance(self.my_amenity.name, str)
        self.assertIsInstance(self.my_amenity.id, str)
        self.assertIsInstance(self.my_amenity.created_at, datetime.datetime)
        self.assertIsInstance(self.my_amenity.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
