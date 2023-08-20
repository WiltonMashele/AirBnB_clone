#!/usr/bin/python3
"""
Unittest for state module
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Testing instances and methods from State class """

    my_state = State()

    def test_class_exists(self):
        """tests class existance"""
        cls = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.my_state)), cls)

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.my_state, State)

    def testHasAttributes(self):
        """verifying attributes"""
        self.assertTrue(hasattr(self.my_state, 'name'))
        self.assertTrue(hasattr(self.my_state, 'id'))
        self.assertTrue(hasattr(self.my_state, 'created_at'))
        self.assertTrue(hasattr(self.my_state, 'updated_at'))

    def test_types(self):
        """tests type of attributes"""
        self.assertIsInstance(self.my_state.name, str)
        self.assertIsInstance(self.my_state.id, str)
        self.assertIsInstance(self.my_state.created_at, datetime.datetime)
        self.assertIsInstance(self.my_state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
