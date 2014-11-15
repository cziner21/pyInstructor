# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addQuestionView.ui'
#
# Created: Sat Nov 08 13:38:50 2014
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

class Ui_addQuestionWindow(object):
    def setupUi(self, addQuestionWindow):
        addQuestionWindow.setObjectName(_fromUtf8("addQuestionWindow"))
        addQuestionWindow.resize(373, 428)
        addQuestionWindow.setFixedSize(337,428) # méretezés letiltása
        self.centralwidget = QtGui.QWidget(addQuestionWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(66, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.topicsComboBox = QtGui.QComboBox(self.centralwidget)
        self.topicsComboBox.setObjectName(_fromUtf8("topicsComboBox"))
        self.gridLayout_2.addWidget(self.topicsComboBox, 0, 2, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        self.questionTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.questionTextEdit.setObjectName(_fromUtf8("questionTextEdit"))
        self.gridLayout_2.addWidget(self.questionTextEdit, 1, 2, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(198, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 3)
        self.addAnswerButton = QtGui.QPushButton(self.centralwidget)
        self.addAnswerButton.setObjectName(_fromUtf8("addAnswerButton"))
        self.gridLayout_2.addWidget(self.addAnswerButton, 2, 3, 1, 2)
        self.answersScrollArea = QtGui.QScrollArea(self.centralwidget)
        self.answersScrollArea.setWidgetResizable(True)
        self.answersScrollArea.setObjectName(_fromUtf8("answersScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 353, 157))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.answerTable = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.answerTable.setObjectName(_fromUtf8("answerTable"))
        self.answerTable.setColumnCount(2)
        self.answerTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.answerTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.answerTable.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.answerTable, 0, 0, 1, 1)
        self.answersScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.answersScrollArea, 3, 0, 1, 5)
        spacerItem2 = QtGui.QSpacerItem(271, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 4)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.gridLayout_2.addWidget(self.sendButton, 4, 4, 1, 1)
        addQuestionWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(addQuestionWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        addQuestionWindow.setStatusBar(self.statusbar)

        self.retranslateUi(addQuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(addQuestionWindow)

    def retranslateUi(self, addQuestionWindow):
        addQuestionWindow.setWindowTitle(_translate("addQuestionWindow", "Kérdés hozzáadása", None))
        self.label_2.setText(_translate("addQuestionWindow", "Témakör:", None))
        self.label.setText(_translate("addQuestionWindow", "Kérdés szövege:", None))
        self.addAnswerButton.setText(_translate("addQuestionWindow", "Válasz hozzáadása", None))
        item = self.answerTable.horizontalHeaderItem(0)
        item.setText(_translate("addQuestionWindow", "Válasz szövege", None))
        item = self.answerTable.horizontalHeaderItem(1)
        item.setText(_translate("addQuestionWindow", "Helyes-e", None))
        self.sendButton.setText(_translate("addQuestionWindow", "Elküld", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    addQuestionWindow = QtGui.QMainWindow()
    ui = Ui_addQuestionWindow()
    ui.setupUi(addQuestionWindow)
    addQuestionWindow.show()
    sys.exit(app.exec_())

