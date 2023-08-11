"""test_base_model for testing
    class, attributes and methods
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""
    def test_initial_attributes(self):
        """Testing attributes of an instance"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)

    def test_save(self):
        """Testing updated_at after making
        changes to the instance
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        new_updated_at = my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        """tests if the returned value is dictionary"""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(obj_dict, dict)
        for key, value in obj_dict.items():
            if key == "__class__":
                self.assertEqual(value, "BaseModel")
            elif key == "id":
                self.assertIsInstance(obj_dict[key], str)
            else:
                self.assertIsInstance(obj_dict[key], str)

    def test_obj_creation(self):
        """tests if the object is created correctly
        if a dictionary is passed to a constructor"""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        new_obj = BaseModel(**obj_dict)
        new_obj.my_number = 89
        my_model.my_number = 78
        self.assertIsInstance(new_obj.my_number, int)
        self.assertIsInstance(my_model.my_number, int)
        new_obj.save()
        my_model.save()
        self.assertNotEqual(my_model.my_number, new_obj.my_number)
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(my_model.id, new_obj.id)
        self.assertEqual(my_model.created_at, new_obj.created_at)
        self.assertNotEqual(my_model.updated_at, new_obj.updated_at)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(new_obj.created_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
