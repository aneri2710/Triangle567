# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class Testtriangles(unittest.TestCase):
    """
    define multiple sets of tests as functions with names that begin
    """

    def testrighttrianglea(self):
        """ Test case for right triangles """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene', '3,4,5 is a Right triangle')

    def testrighttriangleb(self):
        """ Test case for right triangles """
        self.assertEqual(classify_triangle(3, 5, 4), 'Right Scalene', '3,5,3 is a Right triangle')

    def testrighttrianglec(self):
        """ Test case for right triangles """
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene', '5,3,4 is a Right triangle')

    def testequilateraltriangles(self):
        """ Test case for equilateral triangles """
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testisoscelesa(self):
        """ Test case for isosceles triangles """
        self.assertEqual(classify_triangle(1, 1, 2), 'Isosceles', '1,1,2 should be isoceles')

    def testisoscelesb(self):
        """ Test case for isosceles triangles """
        self.assertEqual(classify_triangle(2, 1, 1), 'Isosceles', '2,1,1 should be isoceles')

    def testisoscelesc(self):
        """ Test case for isosceles triangles """
        self.assertEqual(classify_triangle(1, 2, 1), 'Isosceles', '1,2,1 should be isoceles')

    def testscalene(self):
        """ Test case for scalene triangles """
        self.assertEqual(classify_triangle(7, 12, 15), 'Scalene', '7,12,15 should be scalene')

    def testnegative(self):
        """ Test case for negative inputs """
        self.assertEqual(classify_triangle(-1, 2, 3), 'InvalidInput', 'InvalidInput')

    def testnegatives(self):
        """ Test case for negative inputs """
        self.assertEqual(classify_triangle(-1, -2, -3), 'InvalidInput', 'InvalidInput')

    def testgreaterthan(self):
        """ Test case for greater than inputs """
        self.assertEqual(classify_triangle(209, 280, 291), 'InvalidInput', 'InvalidInput')

    def testinvalidtriangle(self):
        """ Test case for invalid triangles """
        self.assertEqual(classify_triangle(5, 1, 2), 'NotATriangle', 'NotATriangle')

    def testtypecheck(self):
        """ Test case for type check """
        self.assertEqual(classify_triangle('a', 1, 2), 'InvalidInput', 'InvalidInput')

    def testrightscalene(self):
        """ Test case for right scalene triangles """
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene', '3,4,5 should be scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
