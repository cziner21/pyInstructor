import unittest, sys
import dashBoardViewModel

from PyQt4.QtGui import *


__author__ = 'Adam'


class TestDashBoard(unittest.TestCase) :
    def setUp(self):
        '''Create the GUI'''
        self.app = QApplication(sys.argv)
        self.form = dashBoardViewModel.DashBoard()

    def test_ValidateAddNewTopicsBoxTextShouldFail(self):

        self.form.ui.examTimeBox.text = ""

        result = self.form.ui.ValidateUserFilterTexts()

        self.assertEqual(result,False)


if __name__ == '__main__':
    unittest.main()