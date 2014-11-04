#coding: utf8
from Views import forgotPasswordView
from PySide.QtCore import *
from PyQt4.QtGui import *
import DataBaseConfig2 as dbConfig
import sys

class ForgotPassword(QMainWindow,forgotPasswordView.Ui_MainWindow):

    def __init__(self,parent=None):
        super(ForgotPassword,self).__init__(parent)
        self.setupUi(self)

        self.sendButton.clicked.connect(self.SendNewPasswordToUserEmail)

    def SendNewPasswordToUserEmail(self):
        print("Your new password is:")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ForgotPassword()
    form.show()
    app.exec_()