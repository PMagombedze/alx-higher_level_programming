#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """unittest class for max_integer"""
    def moduleTest(self):
        """check module docsting"""
        d = __import__('6-max_integer').__doc__
        self.assertTrue(len(d) > 1)

    def docstringTest(self):
        """check function docstring"""
        e = max_integer.__doc__
        self.assertTrue(len(e) > 1)

    def emptyTest(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(max_integer(e))

    def noArgsTest(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def oneElementTest(self):
        """Tests for only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def posEndTest(self):
        """Tests for all positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def posMiddleTest(self):
        """Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def negTest(self):
        """Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def begPostTest(self):
        """Tests for all positive with max at beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)
        
    def nonIntTest(self):
        """Tests for non-int"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

    
    def negativeTest(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def noneTest(self):
        """Tests for none arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
