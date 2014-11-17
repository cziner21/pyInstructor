#coding: utf8
from PyQt4.QtGui import *

from Views import forgotPasswordView
from DataBase import mySQLDatabaseConfig as dbConfig
import smtplib, re, random, string


class ForgotPassword(QMainWindow,forgotPasswordView.Ui_MainWindow):

    def __init__(self,parent=None):
        super(ForgotPassword,self).__init__(parent)
        self.setupUi(self)

        self.sendButton.clicked.connect(self.SendNewPasswordToUserEmail)

    def SendNewPasswordToUserEmail(self):
        if self.Validate():
            __dataBase = dbConfig.MySqlDatabaseConfig()

            userDatas = __dataBase.GetUserInfoByEmail(self.emailField.text())

            if userDatas > 0:

                newPassword = self.PasswordGenerator()
                print newPassword

                __dataBase.NewPassword(userDatas[0][0],newPassword)

                emailTo = self.emailField.text()


                to = '%s'%emailTo
                gmail_user = 'pyinstructor@gmail.com'
                gmail_pwd = 'PtiCis+31'
                smtpserver = smtplib.SMTP("smtp.gmail.com",587)
                smtpserver.ehlo()
                smtpserver.starttls()
                smtpserver.ehlo
                smtpserver.login(gmail_user, gmail_pwd)
                header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:pyInstructor uj jelszo \n'
                print header
                msg = header + '\nSzia!\nUj jelszot igenyeltel a pyInstructor programhoz.\nUj jelszavad: '+newPassword+ '\n\n'
                smtpserver.sendmail(gmail_user, to, msg)
                print u'Jelszó sikeresen kiküldve!'
                smtpserver.close()

    def Validate(self):
        error = ""
        validEmailPattern = "[^@]+@[^@]+\.[^@]+"

        if self.emailField.text() == "":
            error += u"Az email cím megadása kötelező!\n"

        if self.emailField.text() != "" and re.match(validEmailPattern,self.emailField.text())==None:
            error += u"Nem érvényes email formátum!\n"

        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True

    def PasswordGenerator(self,size=8, chars=string.ascii_uppercase + string.digits +string.ascii_lowercase):
        return ''.join(random.choice(chars) for _ in range(size)).encode('utf-8')
