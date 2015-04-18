# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutView.ui'
#
# Created: Tue Nov 11 20:33:57 2014
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

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        #AboutWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        AboutWindow.setObjectName(_fromUtf8("AboutWindow"))
        AboutWindow.resize(318, 396)
        AboutWindow.setFixedSize(318,396) # méretezés letiltása

        AboutWindow.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:0.666, y1:1, x2:0, y2:0, stop:0.101695 rgba(28, 151, 151, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.centralwidget = QtGui.QWidget(AboutWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"    \n"
"    background-color: transparent;\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 46, 13))
        self.label_2.setStyleSheet(_fromUtf8("QLabel{\n"
"background-color: transparent\n"
"}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 291, 251))
        self.label_3.setStyleSheet(_fromUtf8("QLabel{\n"
"background-color: transparent\n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        AboutWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AboutWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(_translate("AboutWindow", "A programról", None))
        self.label.setText(_translate("AboutWindow", "pyInstructor", None))
        self.label_2.setText(_translate("AboutWindow", "v1.06", None))
        self.label_3.setText(_translate("AboutWindow", "<html><head/><body><p>A <span style=\" font-weight:600;\">pyInstructor</span> egy python nyelven készült<br/><br/>vizsgáztató program,melynek fő célja, hogy<br/><br/>megkönnyítse a programtervező informatikusok<br/><br/>helyzetetét az álláskeresésben. </p><p><br/></p><p>Github repository: <a href=\"https://github.com/cziner21/pyInstructor\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/cziner21/pyInstructor</span></a></p><p><br/></p><p>Készítette: <span style=\" font-weight:600;\">Cziner Ádám</span><br/>Email:<a href=\"mailto:cziner.adam@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">cziner.adam@gmail.com</span></a></p></body></html>", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AboutWindow = QtGui.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())

