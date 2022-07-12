"""Module for Base test"""
import unittest
from models.base import Base
import pep8


class BaseTestSuite(unittest.TestCase):
    """class to test creating instances of base"""
    def setUp(self):
        """Before every test suite begins"""
        self.b0 = Base()
        self.b1 = Base(2)
        self.b2 = Base(17)
        self.b3 = Base()

    def test_a_pep8(self):
        """test for pep8 conformity"""
        pep_8format = pep8.StyleGuide(quiet=True)
        res = pep_8format.check_files(['models/base.py'])
        self.assertEqual(res.total_errors, 0, "Found errors")

    def test_b_init(self):
        """Init test for Base"""
        # self.assertEqual(self.b0, 1)
        # self.assertEqual(self.b1, 2)
        # self.assertEqual(self.b2, 17)
        # self.assertEqual(self.b3, 2)
        # with self.assertRaises(ValueError):
        # Base(-3)
        # with self.assertRaises(TypeError):
        # Base(5.00)
        # with self.assertRaises(TypeError):
        # Base("8")

        # def test_b_to_json_string(self):
        # """Test check for json string"""

    def tearDown(self):
        """Clean up after yourself"""
        del self.b0
        del self.b1
        del self.b2
        del self.b3

if __name__ == "__main__":
        unittest.main()
        
