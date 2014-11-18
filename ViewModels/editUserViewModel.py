#coding: utf8
import re

from PyQt4.QtGui import *
from DataBase import mySQLDatabaseConfig as dbConfig2

from Views import editUserView


class EditUser(QMainWindow,editUserView.Ui_MainWindow):
    def __init__(self,currentUserDto,parent=None):
        super(EditUser,self).__init__(parent)
        self.setupUi(self)

        self.mysqlDatabase = dbConfig2.MySqlDatabaseConfig()

        self.FillEditBoxes(currentUserDto)

        self.editUserButton.clicked.connect(self.UpdateUser)

        self.editedUserDatasDto = currentUserDto
        self.userId = currentUserDto.UserId


    def FillEditBoxes(self,currentUserDto):

        try:
            self.lastNameEditBox.setText(str(currentUserDto.LastName))
            self.firstNameEditBox.setText(str(currentUserDto.FirstName))
            self.emailEditBox.setText(str(currentUserDto.Email))
            if currentUserDto.City is not None:
                self.cityEditBox.setText(str(currentUserDto.City))
            if currentUserDto.Address is not None:
                self.addressEditBox.setText(str(currentUserDto.Address))
            if currentUserDto.Phone is not None:
                self.phoneEditBox.setText(str(currentUserDto.Phone))
            if currentUserDto.Birthday is not None:
                self.birthDayEditBox.setText(str(currentUserDto.Birthday))

            self.privilidgeEditComboBox.addItem("Admin")
            self.privilidgeEditComboBox.addItem(u"Felhasználó")

            if currentUserDto.Privilidge == 0:
                self.privilidgeEditComboBox.setCurrentIndex(0)
            else:
                self.privilidgeEditComboBox.setCurrentIndex(1)

        except Exception as e:
            print e.args

    def Validate(self):
        error = ""

        validDateFormat = "\d{4}(?:-\d{1,2}){2}"
        validNameFormat = u"^[a-zA-ZáéíöüóőúűÁÉÍÖÜÓŐÚŰ\s]+$"
        validAddressFormat = u"^([a-zA-Z0-9áÁéÉíÍóÓöÖőŐúÚüÜűŰ \/.,-]{1,})$"
        validPhoneFormat = u"^([0-9 +]{1,50})$"
        validCityFormat = u"^([a-zA-ZáÁéÉíÍóÓöÖőŐúÚüÜűŰ]{1,})$"
        validEmailFormat = "[^@]+@[^@]+\.[^@]+"

        if self.lastNameEditBox.text()!="" and re.match(validNameFormat,self.lastNameEditBox.text())==None:
            error += u"A vezetéknév mező nem megengedett karaktereket tartalmaz!\n     Helyes formátum: Kovács\n"
        if self.firstNameEditBox.text()!="" and re.match(validNameFormat,self.firstNameEditBox.text())==None:
            error += u"A keresztnév mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Krisztina\n"
        if self.addressEditBox.text()!="" and re.match(validAddressFormat,self.addressEditBox.text())==None:
            error += u"A cím mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Hungária körút 81. 3. emelet 18/A\n"
        if self.phoneEditBox.text()!="" and re.match(validPhoneFormat,self.phoneEditBox.text())==None:
            error += u"A telefonszám mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 301234567\n"
        if self.cityEditBox.text()!="" and re.match(validCityFormat,self.cityEditBox.text())==None:
            error += u"A város mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Budapest\n"
        if self.birthDayEditBox.text()!="" and re.match(validDateFormat,self.birthDayEditBox.text())==None:
            error += u"A születési idő mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 1970-10-01\n"
        if self.emailEditBox.text()!="" and re.match(validEmailFormat,self.emailEditBox.text())==None:
            error += u"Az email mező nem megengedett karaktereket tartalmaz!\n     Helyes formátum: email@cim.com\n"

        if self.lastNameEditBox.text() == "":
            error += u"A vezetéknév kitöltése kötelező!\n"
        if self.firstNameEditBox.text() == "":
            error += u"A keresztnév kitöltése kötelező!\n"
        if self.emailEditBox.text() == "":
            error += u"Az email kitöltése kötelező!\n"


        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True

    def UpdateUser(self):
        if self.Validate():

            self.editedUserDatasDto.Id = self.userId

            firstName = unicode(self.firstNameEditBox.text())
            lastName = unicode(self.lastNameEditBox.text())
            email = unicode(self.emailEditBox.text())
            city = unicode(self.cityEditBox.text())
            address = unicode(self.addressEditBox.text())
            phone = unicode(self.phoneEditBox.text())

            self.editedUserDatasDto.FistName = ""
            self.editedUserDatasDto.FistName = unicode(firstName)
            self.editedUserDatasDto.LastName = unicode(lastName)
            self.editedUserDatasDto.Email = unicode(email)
            self.editedUserDatasDto.City = unicode(city)
            self.editedUserDatasDto.Address = unicode(address)
            self.editedUserDatasDto.Phone = unicode(phone)
            if self.birthDayEditBox.text() == "":
                 self.editedUserDatasDto.Birthday = None
            else:
                self.editedUserDatasDto.Birthday = unicode(self.birthDayEditBox.text())
            if self.privilidgeEditComboBox.currentText() == "Admin":
                self.editedUserDatasDto.Privilidge = 0
            else:
                self.editedUserDatasDto.Privilidge = 1

            print self.editedUserDatasDto.FistName

            self.mysqlDatabase.UpdateUserAndProfil(self.editedUserDatasDto)



