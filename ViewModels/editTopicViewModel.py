#coding: utf8
import re

from PyQt4.QtGui import *

from DataBase import mySQLDatabaseConfig as dbConfig2
from Views import editTopicView


class EditTopic(QMainWindow,editTopicView.Ui_MainWindow):
    def __init__(self,topicId,parent=None):
        super(EditTopic,self).__init__(parent)
        self.setupUi(self)

        self.mysqlDatabase = dbConfig2.MySqlDatabaseConfig()
        self.topicId = topicId


        self.topicName = self.mysqlDatabase.GetTopicNameById(topicId)
        self.timeForExam = self.mysqlDatabase.GetExamTimeByTopicsId(topicId)

        self.editTopicNameBox.setText(self.topicName[0][0])
        #mivel a vizsga ideje db-ben másodpercben van, vissza kell alakítani perc formátumra
        self.timeForexamInMinutes = self.timeForExam / 60
        self.examTimeBox.setText(str(self.timeForexamInMinutes))

        self.editTopicButton.clicked.connect(self.UpdateTopicName)

    def Validate(self):
        error = ""

        validNameFormat = u"^[a-zA-Z+#\s]+$"
        validExamTimeFormat = u"^[1-9][0-9]*$" #az első karakter nem lehet 0

        if(self.editTopicNameBox.text() == ""):
            error += u"A téma neve nem lehet üres!\n"
        if(self.editTopicNameBox.text() != "" and re.match(validNameFormat,self.editTopicNameBox.text())==None):
            error += u"A téma neve csak az angol ábécé karaktereit tartalmazhatja, illetve a + és # szimbólumokat!\n"
        if (self.examTimeBox.text()== ""):
            error += u"Új téma felvételéhez a vizsga megadása is kötelező!\n"
        if (self.examTimeBox.text() != "" and re.match(validExamTimeFormat, self.examTimeBox.text()) == None):
            error += u"A vizsga idejének formátuma nem megfelelő!\nCsak számokat írhat be, és az első számjegy nem lehet 0!\n"

        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True

    def UpdateTopicName(self):
        if self.Validate():
            self.mysqlDatabase.UpdateTopic(self.topicId,self.editTopicNameBox.text(),int(self.examTimeBox.text()) * 60)
