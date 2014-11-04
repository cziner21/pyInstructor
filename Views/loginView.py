# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginView.ui'
#
# Created: Mon Nov 03 20:40:46 2014
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
        MainWindow.resize(339, 186)
        MainWindow.setFixedSize(300,180) # méretezés letiltása
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/login/pythonLogoSmall.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.emailField = QtGui.QLineEdit(self.centralwidget)
        self.emailField.setObjectName(_fromUtf8("emailField"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.emailField)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passwordField = QtGui.QLineEdit(self.centralwidget)
        self.passwordField.setObjectName(_fromUtf8("passwordField"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwordField)
        self.passwordField.setEchoMode(QtGui.QLineEdit.Password) #jelszó mező beállítása
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 3)
        self.forgetPasswordLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.forgetPasswordLabel.setFont(font)
        self.forgetPasswordLabel.setObjectName(_fromUtf8("forgetPasswordLabel"))
        self.gridLayout.addWidget(self.forgetPasswordLabel, 2, 0, 1, 2)
        self.loginButton = QtGui.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/login/keywords1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginButton.setIcon(icon)
        self.loginButton.setIconSize(QtCore.QSize(32, 32))
        self.loginButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.gridLayout.addWidget(self.loginButton, 2, 2, 2, 1)
        self.registerLabel = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.registerLabel.setFont(font)
        self.registerLabel.setObjectName(_fromUtf8("registerLabel"))
        self.gridLayout.addWidget(self.registerLabel, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Bejelentkezés", None))
        self.label_4.setText(_translate("MainWindow", "pyInstructor", None))
        self.label.setText(_translate("MainWindow", "Email:", None))
        self.label_2.setText(_translate("MainWindow", "Jelszó:", None))
        self.forgetPasswordLabel.setText(_translate("MainWindow", "Elfelejtett jelszó", None))
        self.loginButton.setText(_translate("MainWindow", "Bejelentkezés", None))
        self.registerLabel.setText(_translate("MainWindow", "Regisztráció", None))

import loginResource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

