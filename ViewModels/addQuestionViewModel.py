#coding: utf8
from DataBase import mySQLDatabaseConfig as dbConfig2
from Views import addQuestionView
#from ViewModels import examViewModel, forgotPasswordViewModel, signUpViewModel
from PyQt4.QtGui import *


class Question(QMainWindow,addQuestionView.Ui_addQuestionWindow):
    def __init__(self,parent=None):
        super(Question,self).__init__(parent)
        self.setupUi(self)
        #self.myDbConfig = dbConfig.DataBaseConfig()
        self.myDbConfig2 = dbConfig2.MySqlDatabaseConfig()

        self.FillTopicsCombobox()
        self.questionCount = 0





        self.addAnswerButton.clicked.connect(self.NewQuestion)
        self.sendButton.clicked.connect(self.AddQuestionAndAnswersToDataBase)


        self.answersLineEditList = []
        self.answersCheckboxList = []



        #self.answerTable.setRowCount(1)
        #self.answerTable.setColumnCount(1)

        """btn = QPushButton(self.answerTable)
        btn.setText('Add')
        self.answerTable.setCellWidget(0, 0, btn)
        self.answerTable.setCellWidget(0, 1, btn)"""
    #@classmethod
    #def ConstructorForEdit(cls,questionId):
    #    cls.GetQuestion(questionId)

    """def __init__(self,questionId,parent=None):
        super(Question,self).__init__(parent)
        self.setupUi(self)


        self.DataBase = dbConfig.MySqlDatabaseConfig()

        self.FillTopicsCombobox()
        self.answersCount = 0

        self.GetQuestion(questionId)

        self.addAnswerButton.clicked.connect(self.NewQuestion)
        self.sendButton.clicked.connect(self.AddQuestionAndAnswersToDataBase)

        self.answersLineEditList = []
        self.answersCheckboxList = []"""

    def GetQuestion(self,questionId):
        currentQuestion = self.myDbConfig2.GetQuestionByQuestionId(questionId)
        self.questionTextEdit.setText(currentQuestion[0][1])
        #self.questionTextEdit.setText(currentQuestion[i][j])
        #for i in range(0,len(currentQuestion)):
        #    for j in range(0,len(currentQuestion[i])):
                #self.questionTextEdit.setText(currentQuestion[i][j])
                #label = QLabel()
                #label.setText(str(questionList[i][j]))
                #self.questionsListTable.setCellWidget(i,j,label)


    #def GetAnswersForQuestion(self):

    def NewQuestion(self):
        self.questionCount += 1

        self.answerTable.setRowCount(self.questionCount)
        self.answerTable.setColumnCount(2)

        questionLineEdit = QLineEdit()
        self.answersLineEditList.append(questionLineEdit)
        cbx = QCheckBox()
        self.answersCheckboxList.append(cbx)


        self.answerTable.setCellWidget(self.questionCount-1,0,questionLineEdit)
        self.answerTable.setColumnWidth(0,180)
        self.answerTable.setCellWidget(self.questionCount-1,1,cbx)




        #questionLineEdit.textChanged.connect(self.valtozott)


        #questionLineEdit = QLineEdit(self.answerTable)
        #self.answerTable.setCellWidget(self.answersCount-1,0,questionLineEdit)

        #cbx = QCheckBox(self.answerTable)
        #self.answerTable.setCellWidget(self.answersCount-1,1,cbx)


        #print self.answerTable.rowCount()

    def FillTopicsCombobox(self):
        #_topicsList = self.myDbConfig.GetTopicsName()
        _topicsList = self.myDbConfig2.GetTopicsName()
        self.topicsComboBox.addItems(_topicsList)

    def AddQuestionAndAnswersToDataBase(self):
        answersList = []
        topics = unicode(self.topicsComboBox.currentText())
        topicsId = self.myDbConfig2.GetTopicsIndexByName(topics)
        print ("topicName = %s"%topics)
        print ("topicsId = %s"%topicsId)

        newQuestion =  unicode(self.questionTextEdit.toPlainText()) # TEXTeDIT értéke

        self.myDbConfig2.InsertIntoQuestions(newQuestion,topicsId)

        lastQuestionId = self.myDbConfig2.GetLastQuestion()


        for i in range(0,len(self.answersLineEditList)):
            if self.answersLineEditList[i].text() != "":
                answerText =  unicode(self.answersLineEditList[i].text())
                #answerText2 ="%s"%answerText
                #print answerText2
                isItCorrect =  self.answersCheckboxList[i].isChecked()
                self.myDbConfig2.InsertIntoAnswers(answerText,lastQuestionId,isItCorrect,topicsId)

        self.close()


        #insert into questions(questionText,topicsId) values(unicode(self.questionTextEdit.toPlainText()),topicsId)

        # get last questionId from question table -> lastQuestionId

        #for i in range(0,self.answerTable.rowCount()):
        #    print self.answerTable.itemAt(i,0)

            #insert into answers(answertext,questionId,isItCorrect) values(item[0],lastQuestionId,item[1])





"""if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Question()
    form.show()
    app.exec_()"""
