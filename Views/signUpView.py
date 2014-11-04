# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signUpView.ui'
#
# Created: Tue Nov 04 16:56:36 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(364, 240)
        MainWindow.setFixedSize(364,240) # méretezés letiltása
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(102, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(101, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lastNameField = QtGui.QLineEdit(self.centralwidget)
        self.lastNameField.setObjectName(_fromUtf8("lastNameField"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lastNameField)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.firstNameField = QtGui.QLineEdit(self.centralwidget)
        self.firstNameField.setObjectName(_fromUtf8("firstNameField"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.firstNameField)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.emailField = QtGui.QLineEdit(self.centralwidget)
        self.emailField.setObjectName(_fromUtf8("emailField"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.emailField)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.passwordField = QtGui.QLineEdit(self.centralwidget)
        self.passwordField.setObjectName(_fromUtf8("passwordField"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.passwordField)
        self.passwordField.setEchoMode(QtGui.QLineEdit.Password) #jelszó mező beállítása

        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.passwordAgainField = QtGui.QLineEdit(self.centralwidget)
        self.passwordAgainField.setObjectName(_fromUtf8("passwordAgainField"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.passwordAgainField)
        self.passwordAgainField.setEchoMode(QtGui.QLineEdit.Password) #jelszó mező újra beállítása
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(233, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 2)
        self.signUpButton = QtGui.QPushButton(self.centralwidget)
        self.signUpButton.setObjectName(_fromUtf8("signUpButton"))
        self.gridLayout.addWidget(self.signUpButton, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Regisztráció", None))
        self.label_6.setText(_translate("MainWindow", "Regisztráció", None))
        self.label.setText(_translate("MainWindow", "Vezetéknév:", None))
        self.label_2.setText(_translate("MainWindow", "Keresztnév:", None))
        self.label_3.setText(_translate("MainWindow", "Email:", None))
        self.label_4.setText(_translate("MainWindow", "Jelszó:", None))
        self.label_5.setText(_translate("MainWindow", "Jelszó újra:", None))
        self.signUpButton.setText(_translate("MainWindow", "Elküld", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

