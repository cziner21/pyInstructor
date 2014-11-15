#coding: utf8
import sys
import hashlib
import re   #regex modul

from PyQt4.QtGui import *

from DataBase import mySQLDatabaseConfig as dbConfig2
from Views import loginView
from ViewModels import dashBoardViewModel, forgotPasswordViewModel, signUpViewModel
import mssqlServerDatabaseConfig as dbConfig


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
        if self.Validate():
            myDbConfig = dbConfig2.MySqlDatabaseConfig()
            email = self.emailField.text()
            password = hashlib.sha512(self.passwordField.text()).hexdigest()

            if myDbConfig.TryToLogin(email,password):

            #if hashlib.sha512("self.passwordField.text()").hexdigest() ==

                self.otherWindow = dashBoardViewModel.DashBoard(email)
                self.otherWindow.show()
            else:
                QMessageBox.about(self, u"Hiba", u"Hibás név vagy jelszó!" )

    def Validate(self):
        error = ""
        validEmailPattern = "[^@]+@[^@]+\.[^@]+"

        if self.passwordField.text() == "":
            error += u"A jelszó nem lehet üres!\n"
        if self.emailField.text() == "":
            error += u"Az email cím nem lehet üres!\n"
        #print re.match(validEmailPattern,self.emailField.text())
        if self.emailField.text() != "" and re.match(validEmailPattern,self.emailField.text())==None:
            error += u"Nem érvényes email formátum!\n"
        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Login()
    form.show()
    app.exec_()