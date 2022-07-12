"""Module for Square Tests"""
import unittest
from models.square import Square
import pep8


class SquareTestSuite(unittest.TestCase):
    """Test suite for square subclass"""
    def setUP(self):
        """Initializing objs for testing"""
        self.squ0 = Square(5)
        self.squ1 = Square(2, 2)
        self.squ2 = Square(3, 1, 3)

    def test_a_pep8(self):
        """Test to check for pep8 format"""
        pep_8format = pep8.StyleGuide(quiet=True)
        result = pep_8format.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")

    def test_b_init(self):
        """testing cases for init of square"""
        
