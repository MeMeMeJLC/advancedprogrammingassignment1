#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jeremy
#
# Created:     14/03/2016
# Copyright:   (c) jeremy 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from AdvancedProgrammingAssignment1 import Controller, Model
import unittest

class MainTest(unittest.TestCase):
    def test_write_data_1(self):
        self.assertEqual(Controller.do_quit)

    def test_load_data(self):
            self.assertTrue(data[3] == str, isString)

    def test_file_choose_error(self):
        self.assertRaises(file_error, Model.get_data_values, [not_a_file])


if __name__ == '__main__':
    unittest.main()
