"""file storage module"""
import json
import os


class FileStorage:
    """Defines a file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary that stores
        all objects saved
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        key must be a string. so this function grabs the class
        and ID of the object to make a key that will be used to
        store the object in __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file"""
        objects_dict = {}
        for key, obj in FileStorage.__objects.items():
            objects_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """deserialize the json file to __objects
        only if the json file exists. otherwise
        no exception is raised if the file does
        not exist.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
                class_map = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "City": City, "Amenity": Amenity, "State": State,
               "Review": Review}

                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    obj_cls = class_map.get(class_name)
                    if obj_cls is not None:
                        obj = obj_cls(**obj_data)
                        FileStorage.__objects[key] = obj
