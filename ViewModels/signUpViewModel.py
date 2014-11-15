#coding: utf8
import re

from PyQt4.QtGui import *

from DataBase import mySQLDatabaseConfig as dbConfig
from Views import signUpView

class SignUp(QMainWindow,signUpView.Ui_MainWindow):

    def __init__(self,parent=None):
        super(SignUp,self).__init__(parent)
        self.setupUi(self)

        self.signUpButton.clicked.connect(self.AddUserToDatabase)

    def AddUserToDatabase(self):
        if self.Validate():
            myDbConfig = dbConfig.MySqlDatabaseConfig()
            lastName = unicode(self.lastNameField.text())
            firstName = unicode(self.firstNameField.text())
            email = self.emailField.text()
            password = self.passwordField.text()
            myDbConfig.InsertIntoUsers(firstName,lastName,email,password)

            QMessageBox.about(self, u"Siker", u"Sikeres hozzáadás")

            self.close()

    def Validate(self):
        error = ""
        validEmailPattern = "[^@]+@[^@]+\.[^@]+"
        # http://www.mkyong.com/regular-expressions/how-to-validate-password-with-regular-expression/
        validPasswordPattern = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[/+@#$%]).{8,20})"
        validNameFormat = u"^[a-zA-ZáéíöüóőúűÁÉÍÖÜÓŐÚŰ\s]+$"


        if self.firstNameField.text() == "":
            error += u"A keresztnév kitöltése kötelező!\n"
        if self.lastNameField.text() == "":
            error += u"A vezetéknév kitöltése kötelező!\n"
        if self.emailField.text() == "":
            error += u"Az email cím megadása kötelező!\n"
        if self.passwordAgainField.text() == "" or self.passwordField.text() == "":
            error += u"A jelszó és a jelszó újra mezők kitöltése kötelező!\n"
        if self.passwordField.text() != self.passwordAgainField.text():
            error += u"A két jelszó nem egyezik!\n"
        if self.emailField.text() != "" and re.match(validEmailPattern,self.emailField.text())==None:
            error += u"Nem érvényes email formátum!\n"
        if self.passwordField.text() != "" and re.match(validPasswordPattern,self.passwordField.text())==None:
            error += u"A jelszónak legalább 8 karakternek kell lennie és tartalmaznia kell:\n     legalább egy számot,\n     egy kisbetűt,\n     egy nagybetűt\n     és egy speciális karaktert a következők közül: /@#$% \n"
        if self.firstNameField.text() != "" and re.match(validNameFormat,self.firstNameField.text())==None:
            error += u"A keresztnév nem megengedett karaktereket tartalmaz!\n    (Csak a magyar ábécé karaktereit tartalmazhatja)\n"
        if self.lastNameField.text() != "" and re.match(validNameFormat,self.lastNameField.text())==None:
            error += u"A vezetéknév nem megengedett karaktereket tartalmaz!\n    (Csak a magyar ábécé karaktereit tartalmazhatja)\n"


        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True

