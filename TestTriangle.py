# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,4), 'Right', '3,5,3 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testIsocelesA(self):
        self.assertEqual(classifyTriangle(1,1,2), 'Isoceles', '1,1,2 should be isoceles')

    def testIsocelesB(self):
        self.assertEqual(classifyTriangle(2,1,1), 'Isoceles', '2,1,1 should be isoceles')

    def testIsocelesC(self):
        self.assertEqual(classifyTriangle(1,2,1), 'Isoceles', '1,2,1 should be isoceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(7,12,15), 'Scalene', '7,12,15 should be scalene')

    def testNegative(self):
        self.assertEqual(classifyTriangle(-1,2,3), 'InvalidInput', 'InvalidInput')

    def testNegatives(self):
        self.assertEqual(classifyTriangle(-1,-2,-3), 'InvalidInput', 'InvalidInput')

    def testGreaterThan(self):
        self.assertEqual(classifyTriangle(209,280,291), 'InvalidInput', 'InvalidInput')

    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(5,1,2), 'NotATriangle', 'NotATriangle')

    def testTypeCheck(self):
        self.assertEqual(classifyTriangle('a',1,2), 'InvalidInput', 'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

