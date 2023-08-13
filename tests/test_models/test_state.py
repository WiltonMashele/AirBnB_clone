#!/usr/bin/python3
"""
Unittest for the implementation of state
"""
import unittest
from models.state import State
from datetime import datetime

class TestState(unittest.TestCase):
    
    def setUp(self):
        """Set up testing instance."""
        self.state = State()

    def tearDown(self):
        """Tear down testing instance."""
        del self.state

    def test_instance(self):
        """Test if instance of State successfully created."""
        self.assertIsInstance(self.state, State)

    def test_id(self):
        """Test if id is correctly assigned."""
        self.assertEqual(type(self.state.id), str)

    def test_name_default(self):
        """Test default value of name attribute."""
        self.assertEqual(self.state.name, "")

    def test_created_at(self):
        """Test if created_at is datetime type."""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is datetime type."""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_to_dict(self):
        """Test if to_dict returns a dictionary representation of the instance."""
        state_dict = self.state.to_dict()
        self.assertEqual(type(state_dict), dict)
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("id" in state_dict)
        self.assertTrue("__class__" in state_dict)

if __name__ == '__main__':
    unittest.main()
