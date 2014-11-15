#coding: utf8
from ViewModels import addQuestionViewModel, dashBoardViewModel


class Admin():
    def __init__(self,parent=None):
        dViewM = dashBoardViewModel.DashBoard()

        dViewM.addNewQuestionButton.clicked.connect(self.AddNewQuestionAndAnsers)

    def AddNewQuestionAndAnsers(self):
        self.addQuestionWindow = addQuestionViewModel.Question()
        self.addQuestionWindow.show()



