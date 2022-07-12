#!/usr/bin/python3
"""Base class 1.0"""
import json


class Base:
    """class Base of all classes in project 0x0c"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to convert to json str repr"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """return list repr of json str"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """cls method to save json str to file"""
        json_list = []
        for instance in list_objs:
            json_list.append(instance.to_dictionary())
        jsonRepr = cls.to_json_string(json_list)
        with open('{}.json.'.format(cls.__name__), mode='w') as a_file:
            if list_objs is None:
                json_list = []
                a_file.write(json_list)
            else:
                a_file.write(jsonRepr)

    @classmethod
    def create(cls, **dictionary):
        """Method to return an instance with attributes all set"""
        pass

    @classmethod
    def load_from_file(cls):
        """Method to return list of instances"""
        pass
    
