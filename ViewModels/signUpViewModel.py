#coding: utf8
from Views import signUpView
from PySide.QtCore import *
from PyQt4.QtGui import *
import DataBaseConfig2 as dbConfig
import sys

class SignUp(QMainWindow,signUpView.Ui_MainWindow):

    def __init__(self,parent=None):
        super(SignUp,self).__init__(parent)
        self.setupUi(self)

        self.signUpButton.clicked.connect(self.AddUserToDatabase)


    def AddUserToDatabase(self):
        print "new user"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SignUp()
    form.show()
    app.exec_()