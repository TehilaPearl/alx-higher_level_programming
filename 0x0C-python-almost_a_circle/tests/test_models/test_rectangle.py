"""Test Module for Rectangle"""
import unittest
from models.rectangle import Rectangle
import pep8


class RectangleInitTestSuite(unittest.TestCase):
    """Testing Rectangle subclass"""
    def setUp(self):
        """Initializing objects for test"""
        self.r0 = Rectangle(10, 2)
        self.r1 = Rectangle(2, 10)
        self.r2 = Rectangle(10, 2, 0, 0, 12)
        self.r3 = Rectangle(10, 2, 0, 0, -1)
        self.r4 = Rectangle(1, 2, 3, 4)

    def test_a_pep8(self):
        """Test to check for pep8 format"""
        pep_8format = pep8.StyleGuide(quiet=True)
        result = pep_8format.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")

    def test_b_init(self):
        """Test to return self.id from Rectangle"""
        # self.assertEqual(self.r0, 1)
        # self.assertEqual(self.r1, 2)
        # self.assertEqual(self.r2, 12)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(3)
        # self.assertEqual(self.r3, -1)

    def test_c_validating_attributes(self):
        """Test cases to validate"""
        self.assertTrue(self.r0)
        self.assertTrue(self.r1)
        self.assertTrue(self.r2)
        self.assertTrue(self.r3)
        self.assertTrue(self.r4)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            Rectangle(2)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(5.00, 7)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 0, 0, 0)

    def test_d_area(self):
        """Test cases for area"""
        res0 = Rectangle(10, 2)
        res1 = Rectangle(2, 10)
        res2 = Rectangle(10, 2, 0, 0, 12)
        res3 = Rectangle(1, 2, 3, 4)

        self.assertEqual(res0.area(), 20)
        self.assertEqual(res1.area(), 20)
        self.assertEqual(res2.area(), 20)
        self.assertEqual(res3.area(), 2)
        with self.assertRaises(AttributeError):
            Rectangle.area(3)
        with self.assertRaises(TypeError):
            Rectangle.area(-3, 4)
        with self.assertRaises(TypeError):
            Rectangle.area(5, "5")
        with self.assertRaises(TypeError):
            Rectangle.area(5.00, 7)
        with self.assertRaises(TypeError):
            Rectangle.area()
        with self.assertRaises(TypeError):
            Rectangle.area(0, 12)

    def test_e_Display0(self):
        """test cases for rect picture display"""
        with self.assertRaises(TypeError):
            Rectangle.display(0, 6)
        with self.assertRaises(TypeError):
            Rectangle.display(6, "2")
        with self.assertRaises(TypeError):
            Rectangle.display()
        with self.assertRaises(TypeError):
            Rectangle.display(0, 0)
        with self.assertRaises(TypeError):
            Rectangle.display(5.00, 2)

    def test_f_str(self):
        """Test cases for __str__"""
        res0 = Rectangle(4, 6, 2, 1, 12)
        res1 = Rectangle(5, 5, 1)

        # self.assertEqual(res0.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        # self.assertEqual(res1.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        with self.assertRaises(TypeError):
            Rectangle().__str__()
        with self.assertRaises(TypeError):
            Rectangle(0).__str__()
        with self.assertRaises(ValueError):
            Rectangle(-10, 2, 5).__str__()
        with self.assertRaises(TypeError):
            Rectangle(2, "3", 4, 5).__str__()

    def tearDown(self):
        """Cleaning up after myself"""
        del self.r0
        del self.r1
        del self.r2
        del self.r3
        del self.r4

if __name__ == "__main__":
    unittest.main()
    
