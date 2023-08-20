#!/usr/bin/python3
"""
Unittest for city module
"""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Testing instances and methods from city class"""

    my_city = City()

    def test_class_exists(self):
        """testing the class existance"""
        cls = "<class 'models.city.City'>"
        self.assertEqual(str(type(self.my_city)), cls)

    def test_user_inheritance(self):
        """test if city is a subclass of BaseModel"""
        self.assertTrue(self.my_city, City)

    def testHasAttributes(self):
        """verifying attributes"""
        self.assertTrue(hasattr(self.my_city, 'state_id'))
        self.assertTrue(hasattr(self.my_city, 'name'))
        self.assertTrue(hasattr(self.my_city, 'id'))
        self.assertTrue(hasattr(self.my_city, 'created_at'))
        self.assertTrue(hasattr(self.my_city, 'updated_at'))

    def test_types(self):
        """testing the type of the attribute"""
        self.assertIsInstance(self.my_city.state_id, str)
        self.assertIsInstance(self.my_city.name, str)
        self.assertIsInstance(self.my_city.id, str)
        self.assertIsInstance(self.my_city.created_at, datetime.datetime)
        self.assertIsInstance(self.my_city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
