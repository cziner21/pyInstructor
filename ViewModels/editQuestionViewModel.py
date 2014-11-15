#coding: utf8
from PyQt4.QtGui import *

from DataBase import mySQLDatabaseConfig as dbConfig2
from Views import addQuestionView


class EditQuestion(QMainWindow,addQuestionView.Ui_addQuestionWindow):
    def __init__(self,questionId,currentTopics,parent=None):
        super(EditQuestion,self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(u"Kérdés és válasz szerkesztése")

        self.myDbConfig2 = dbConfig2.MySqlDatabaseConfig()

        self.FillTopicsCombobox()
        self.answersCount = 0
        self.questionId = questionId

        self.currentTopics = currentTopics
        if self.currentTopics is not None:
            self.topicsComboBox.setCurrentIndex(self.currentTopics)

        self.addAnswerButton.clicked.connect(self.AddNewAnswer)
        self.sendButton.clicked.connect(self.UpdateQuestionAndAnswers)


        self.answersLineEditList = []
        self.answersCheckboxList = []

        self.newAnswersEditList = []
        self.newAnswersCheckboxList = []

        self.GetQuestion(questionId)

    def FillTopicsCombobox(self):
        _topicsList = self.myDbConfig2.GetTopicsName()
        self.topicsComboBox.addItems(_topicsList)


    def GetQuestion(self,questionId):
        currentQuestion = self.myDbConfig2.GetQuestionByQuestionId(questionId)
        self.questionTextEdit.setText(currentQuestion[0][1])

        self.GetAnswersForQuestion(questionId)



    def GetAnswersForQuestion(self,questionId):
        answerList = self.myDbConfig2.GetAnswersForQuestionByQuestionId(questionId)

        self.answerIdList = []
        for i in range(0,len(answerList)):
            self.answerIdList.append(answerList[i][0])

        self.answerTable.setRowCount(len(answerList))
        self.answerTable.setColumnCount(2)
        self.answersCount = len(answerList)

        for i in range(0,len(answerList)):

            answerLineEdit = QLineEdit()
            answerLineEdit.setText(answerList[i][1])
            print answerList[i][1]
            self.answersLineEditList.append(answerLineEdit)
            cbx = QCheckBox()
            if answerList[i][3] == 1:
                cbx.setChecked(True)
            else:
                cbx.setChecked(False)
            self.answersCheckboxList.append(cbx)

            self.answerTable.setCellWidget(i,0,answerLineEdit)
            self.answerTable.setColumnWidth(0,180)
            self.answerTable.setCellWidget(i,1,cbx)

    def AddNewAnswer(self):
        self.answersCount += 1

        self.answerTable.setRowCount(self.answersCount)

        questionLineEdit = QLineEdit()
        self.newAnswersEditList.append(questionLineEdit)
        cbx = QCheckBox()
        self.newAnswersCheckboxList.append(cbx)

        self.answerTable.setCellWidget(self.answersCount-1,0,questionLineEdit)
        self.answerTable.setColumnWidth(0,180)
        self.answerTable.setCellWidget(self.answersCount-1,1,cbx)

    def UpdateQuestionAndAnswers(self):
        answersList = []
        topics = unicode(self.topicsComboBox.currentText())
        topicsId = self.myDbConfig2.GetTopicsIndexByName(topics)


        newQuestion =  unicode(self.questionTextEdit.toPlainText())

        self.myDbConfig2.UpdateQuestions(self.questionId,newQuestion,topicsId)

        i = 0
        while (i < len(self.answerIdList)):
            for j in range(0,len(self.answersLineEditList)):
                if self.answersLineEditList[j].text() != "":
                    print unicode(self.answersLineEditList[j].text())
                    answerText =  unicode(self.answersLineEditList[j].text())

                    isItCorrect =  self.answersCheckboxList[j].isChecked()
                    self.myDbConfig2.UpdateAnswers(self.answerIdList[i],answerText,isItCorrect,topicsId)
                    i += 1

        if len(self.newAnswersEditList) != 0:

            for i in range(0,len(self.newAnswersEditList)):
                if self.newAnswersEditList[i].text() != "":
                    answerText =  unicode(self.newAnswersEditList[i].text())

                    isItCorrect =  self.newAnswersCheckboxList[i].isChecked()
                    self.myDbConfig2.InsertIntoAnswers(answerText,self.questionId,isItCorrect,topicsId)











