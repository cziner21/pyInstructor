import unittest
import DataBaseConfig2
from ViewModels import examViewModel as myEV


class MyTestCase(unittest.TestCase):
    def __init__(self,parent=None):
        self.testExamViewModel = myEV.MainView()


    def test_something(self):
        self.assertEqual(True, False)

    def TopicsCombo(self):

        self.testExamViewModel.FillTopicsCombobox()
        self.assertEqual(2,self.testExamViewModel.examsTypeCombobox.count())

if __name__ == '__main__':
    unittest.main()
