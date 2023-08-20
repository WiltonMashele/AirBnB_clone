#!/usr/bin/python3
"""
Unittest for review module
"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Tests instances and methods from Review class"""

    my_review = Review()

    def test_class_exists(self):
        """tests class existance"""
        cls = "<class 'models.review.Review'>"
        self.assertEqual(str(type(self.my_review)), cls)

    def test_user_inheritance(self):
        """test if Review is a subclass of BaseModel"""
        self.assertIsInstance(self.my_review, Review)

    def testHasAttributes(self):
        """verifying attributes"""
        self.assertTrue(hasattr(self.my_review, 'place_id'))
        self.assertTrue(hasattr(self.my_review, 'user_id'))
        self.assertTrue(hasattr(self.my_review, 'text'))
        self.assertTrue(hasattr(self.my_review, 'id'))
        self.assertTrue(hasattr(self.my_review, 'created_at'))
        self.assertTrue(hasattr(self.my_review, 'updated_at'))

    def test_types(self):
        """tests the type of the attributes"""
        self.assertIsInstance(self.my_review.place_id, str)
        self.assertIsInstance(self.my_review.user_id, str)
        self.assertIsInstance(self.my_review.text, str)
        self.assertIsInstance(self.my_review.id, str)
        self.assertIsInstance(self.my_review.created_at, datetime.datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
