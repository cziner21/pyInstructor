#coding: utf8
#from PySide import QtGui
from Views import examView
from PySide.QtCore import *
from PyQt4.QtGui import *
import DataBaseConfig2 as dbConfig
import sys
import math
import datetime

class MainView(QMainWindow,examView.Ui_MainWindow):

    def __init__(self,parent=None):

        super(MainView,self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.myDbConfig = dbConfig.DataBaseConfig()

        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        palette = self.lcdNumber.palette()
        palette.setColor(palette.WindowText, QColor(0, 255, 0))
        self.lcdNumber.setPalette(palette)
        self.start_time = 10
        self.lcdNumber.display("%02d:%02d" % (self.start_time/60,self.start_time % 60))

        self.FillTopicsCombobox()

        #self.examsTypeCombobox.activated.connect(self.SelectedTopics)
        self.examsTypeCombobox.setCurrentIndex(0)
        self.GenerateQuizByTopic()
        self.examsTypeCombobox.currentIndexChanged.connect(self.GenerateQuizByTopic)
        self.currentExamTableView.setVisible(False)
        self.sendExamButton.setVisible(False)

        self.startExamButton.clicked.connect(self.SetupCountDown)
        self.timer.timeout.connect(self.updateLCD)

        self.sendExamButton.clicked.connect(self.SubmitAnswers)

        self.UserAnswers = []

        self.CurrentTopicId
        self.questionIds

        #self.SetupCountDown()
        #self.examTimeRemaning.setSegmentStyle(QLCDNumber.Flat)
        #
        # foreground color
        #palette.setColor(palette.WindowText, QColor(0, 255, 0))
        #self.examTimeRemaning.setPalette(palette)
        #self.examTimeRemaning.display("30:00")



    def SetupCountDown(self):
        #Új rekord beszúrása az exams táblába az aktuális dátummal:
        self.myDbConfig.InsertIntoExams(datetime.datetime.now(),self.CurrentTopicId)

        #Aktuális témakör elérhető maximális pontszámának kiírása
        maxPoint = self.myDbConfig.MaxPointsForTopicsId(self.CurrentTopicId)
        self.maxPointsLabel.setText("%d"%maxPoint[0][0])

        self.currentExamTableView.setVisible(True)
        self.sendExamButton.setVisible(True)
        self.startExamButton.setEnabled(False)
        self.examsTypeCombobox.setEnabled(False)
        self.timer.stop()
        self.start_time = 10
        self.lcdNumber.display("%02d:%02d" % (self.start_time/60,self.start_time % 60))
        # Restart the timer
        self.timer.start(1000)

    def updateLCD(self):
        # Update the lcd
        self.start_time -= 1
        if self.start_time >= 0:
            self.lcdNumber.display("%02d:%02d" % (self.start_time/60,self.start_time % 60))
        else:
            self.timer.stop()
            self.examsTypeCombobox.setEnabled(True)
            self.SubmitAnswers()
            self.sendExamButton.setEnabled(False)
            #self.startExamButton.setEnabled(True)
            #self.start_time = 5
            #self.lcd.display("%d:%02d" % (self.start_time/60,self.start_time % 60))


    def FillTopicsCombobox(self):
        _topicsList = self.myDbConfig.GetTopicsName()
        self.examsTypeCombobox.addItems(_topicsList)

    def GenerateQuizByTopic(self):
        self.currentExamTableView.setVisible(False)
        self.sendExamButton.setVisible(False)

        self.startExamButton.setEnabled(True)
        model = QStandardItemModel(self.currentExamTableView)
        model.clear()

        _questionList = []
        _answerList = []
        questionListWithId = []
        questionIds = []

        topics = unicode(self.examsTypeCombobox.currentText())
        topicsId = self.myDbConfig.GetTopicsIndexByName(topics)
        self.CurrentTopicId = topicsId

        for item in self.myDbConfig.GetQustionsByTopicsId(topicsId):
            _questionList.append(item.questionText)
            questionListWithId.append(item)

        for item in self.myDbConfig.GetQustionsByTopicsId(topicsId):
            questionIds.append(item.id)

        self.questionIds = questionIds


        #for item in questionIds:
        #    awL = self.myDbConfig.GetAnswersForQuestionByQuestionId(item)
        #    _answerList.append(awL)

        for question in questionListWithId:
            answer = self.myDbConfig.GetAnswersForQuestionByQuestionId(question[0])
            _answerList.append(answer)


        for i in range(len(questionListWithId)):
            questionStandardItemQuestionRow = []
            questionStandardItemQuestionIdCell = QStandardItem("%d"%questionListWithId[i][0])
            questionStandardItemQuestionTextCell = QStandardItem("%d.) %s" %(i+1,questionListWithId[i][1]))
            questionStandardItemEmptyCell = QStandardItem("")
            questionStandardItemQuestionRow.append(questionStandardItemQuestionIdCell)
            questionStandardItemQuestionRow.append(questionStandardItemQuestionTextCell)
            questionStandardItemQuestionRow.append(questionStandardItemEmptyCell)
            #questionStandardItemQuestionTextCell.appendColumn()
            questionStandardItemQuestionTextCell.setEditable(False)
            #model.appendColumn(questionStandardItemQuestionIdCell)
            model.appendRow(questionStandardItemQuestionRow)

            for j in range(len(_answerList)):
                for k in range(len(_answerList[j])):
                    if i == j:
                            ll = []
                            answerIndex = QStandardItem("%d"%_answerList[j][k][0])
                            answerText = QStandardItem(_answerList[j][k][1])
                            questionId = QStandardItem("%d"%_answerList[j][k][2])
                            ll.append(answerIndex)
                            ll.append(answerText)
                            ll.append(questionId)

                            answerText.setCheckable(True)
                            answerText.setEditable(False)
                            model.appendRow(ll)
                            #model.appendRow("")

        #myListView.setModel(model)
        #self.currentExamListView.setModel(model)
        self.currentExamTableView.setModel(model)
        self.currentExamTableView.setColumnHidden(0,True)
        self.currentExamTableView.setColumnHidden(2,True)
        self.currentExamTableView.verticalHeader().setVisible(False)

        #self.currentExamTableView.setColumnWidth(1,500)
        header = self.currentExamTableView.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)
        #self.currentExamListView.setWordWrap(True)
        #self.scrollArea.setWidget(myListView)





        #for item in self.UserAnswers:
        #    self.answersid = self.myDbConfig.GetAnswerIdByAnswerText(item)

    def SubmitAnswers(self):
        self.timer.stop()
        self.examsTypeCombobox.setEnabled(True)

        _questionList = []
        _answerList = []
        questionIds = []

        myAnswersId = []
        qId = []

        userPoints = 0

        model = self.currentExamTableView.model()

        for row in range(model.rowCount()):
            for column in range(model.columnCount()):
                item = model.item(row,column)
                #print(unicode(item.text()))
                if item.isCheckable and (item.checkState() == Qt.Checked):

                    al = []
                    answerId = model.item(row,0)
                    questionId = model.item(row,2)
                    #print int(answerId.text())
                    #print int(questionId.text())
                    self.myDbConfig.InsertIntoUserAnswers(int(answerId.text()),int(self.CurrentTopicId),int(questionId.text()))
                    al.append(int(answerId.text()))
                    al.append(int(self.CurrentTopicId))
                    al.append(int(questionId.text()))
                    self.UserAnswers.append(al)
                    #al.append(answerId.text())
                    #al[questionId.text()] = answerId.text()
                    #al.append(questionId.text())
                    #print(item.text())
                    #print(unicode(item.text()))
                    #self.QuestionIds.append(questionId.text())
                    #self.UserAnswersId.append(al)
                    #self.UserAnswers.append(al)

        #for q, a in zip(self.QuestionIds, self.UserAnswersId):
        #   print '{0} - {1}.'.format(q, a)

        #print self.UserAnswers
        for questionId in self.questionIds:
            for correctAnswer in self.myDbConfig.GetCorrectAnswersByQuestionId(questionId):
                for userAnswer in self.UserAnswers:

                    if correctAnswer[2] == userAnswer[0] and correctAnswer[1] == userAnswer[2]:
                        userPoints += 1

        #print model.takeItem(0)
        maxPoint = self.myDbConfig.MaxPointsForTopicsId(self.CurrentTopicId)
        percentage = float(userPoints)/float(maxPoint[0][0]) * 100
        self.yourPointsLabel.setText("%d"%userPoints)

        lastExamId = self.myDbConfig.GetLastExam()
        self.myDbConfig.InsertIntoResults(userPoints,lastExamId,self.CurrentTopicId,17)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainView()
    form.show()
    app.exec_()


