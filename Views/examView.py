# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'examView.ui'
#
# Created: Sun Nov 02 10:34:31 2014
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.maxPointLabelText = QtGui.QLabel(self.tab_2)
        self.maxPointLabelText.setObjectName(_fromUtf8("maxPointLabelText"))
        self.gridLayout_2.addWidget(self.maxPointLabelText, 0, 3, 1, 1)
        self.maxPointsLabel = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.maxPointsLabel.setFont(font)
        self.maxPointsLabel.setText(_fromUtf8(""))
        self.maxPointsLabel.setObjectName(_fromUtf8("maxPointsLabel"))
        self.gridLayout_2.addWidget(self.maxPointsLabel, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 6, 1, 1)
        self.examsTypeCombobox = QtGui.QComboBox(self.tab_2)
        self.examsTypeCombobox.setMaximumSize(QtCore.QSize(300, 25))
        self.examsTypeCombobox.setObjectName(_fromUtf8("examsTypeCombobox"))
        self.gridLayout_2.addWidget(self.examsTypeCombobox, 1, 0, 1, 1)
        self.startExamButton = QtGui.QPushButton(self.tab_2)
        self.startExamButton.setMaximumSize(QtCore.QSize(120, 25))
        self.startExamButton.setObjectName(_fromUtf8("startExamButton"))
        self.gridLayout_2.addWidget(self.startExamButton, 1, 1, 1, 1)
        self.yourResultLabelText = QtGui.QLabel(self.tab_2)
        self.yourResultLabelText.setObjectName(_fromUtf8("yourResultLabelText"))
        self.gridLayout_2.addWidget(self.yourResultLabelText, 1, 3, 1, 1)
        self.yourPointsLabel = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.yourPointsLabel.setFont(font)
        self.yourPointsLabel.setText(_fromUtf8(""))
        self.yourPointsLabel.setObjectName(_fromUtf8("yourPointsLabel"))
        self.gridLayout_2.addWidget(self.yourPointsLabel, 1, 4, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.tab_2)
        self.lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
""))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 6, 1, 1)
        spacerItem = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(73, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(198, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 3, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(138, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 5, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 756, 418))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.currentExamTableView = QtGui.QTableView(self.scrollAreaWidgetContents)
        self.currentExamTableView.setObjectName(_fromUtf8("currentExamTableView"))
        self.currentExamTableView.horizontalHeader().setVisible(False)
        self.currentExamTableView.horizontalHeader().setHighlightSections(False)
        self.currentExamTableView.verticalHeader().setHighlightSections(False)
        self.gridLayout_3.addWidget(self.currentExamTableView, 0, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(654, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        self.sendExamButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.sendExamButton.setObjectName(_fromUtf8("sendExamButton"))
        self.gridLayout_3.addWidget(self.sendExamButton, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 3, 0, 1, 7)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuKijelentkez_s = QtGui.QMenu(self.menubar)
        self.menuKijelentkez_s.setObjectName(_fromUtf8("menuKijelentkez_s"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuKijelentkez_s.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Profil", None))
        self.label.setText(_translate("MainWindow", "Válassz témakört:", None))
        self.maxPointLabelText.setText(_translate("MainWindow", "Elérhető maximális pontszám:", None))
        self.label_2.setText(_translate("MainWindow", "Hátralévő idő:", None))
        self.startExamButton.setText(_translate("MainWindow", "Vizsga indítása", None))
        self.yourResultLabelText.setText(_translate("MainWindow", "Pontszámod:", None))
        self.sendExamButton.setText(_translate("MainWindow", "Elküld", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vizsgázás", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Eredmények", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuKijelentkez_s.setTitle(_translate("MainWindow", "Kijelentkezés", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

