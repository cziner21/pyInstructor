#coding: utf8
from Views import loginView
from ViewModels import examViewModel, forgotPasswordViewModel, signUpViewModel
from PySide.QtCore import *
from PyQt4.QtGui import *
import DataBaseConfig2 as dbConfig
import sys

class Login(QMainWindow,loginView.Ui_MainWindow):

    def __init__(self,parent=None):

        super(Login,self).__init__(parent)
        self.setupUi(self)
        self.forgetPasswordLabel.mousePressEvent = self.ForgotPassword
        self.registerLabel.mousePressEvent = self.RegisterNewUser
        self.loginButton.clicked.connect(self.Dashboard)




    def ForgotPassword(self,event):
        self.forgotPasswordWindow = forgotPasswordViewModel.ForgotPassword()
        self.forgotPasswordWindow.show()

        """valtozo = unicode("nyeheheh")
        valtozo2 = u"király"
        QMessageBox.about(self, u"My message box", "Text1 = %s, Text2 = %s" % (
            valtozo, valtozo2))"""

    def RegisterNewUser(self,event):
        self.signUpWindow = signUpViewModel.SignUp()
        self.signUpWindow.show()

    def Dashboard(self):
        self.otherWindow = examViewModel.MainView()
        self.otherWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()