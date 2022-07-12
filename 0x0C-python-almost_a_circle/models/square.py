#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set value of size"""
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """builtin to print string repr of instance"""
        result = "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                 self.id, self.x, self.y, self.size)
        return result

    def update(self, *args, **kwargs):
        """Pub method to assign and update attributes"""
        sqDict = {
            0: self.id,
            1: self.size,
            2: self.x,
            3: self.y
        }
        if args:
            for counter, value in enumerate(args):
                sqDict[counter] = value
                self.id, self.size, self.x, self.y = \
                    sqDict[0], sqDict[1], sqDict[2], sqDict[3]
        else:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'size' in kwargs:
                    self.size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y'in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        """Pub method to print str repr of sqr"""
        sqDict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return sqDict
    
