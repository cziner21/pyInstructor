#coding: utf8
import re
import datetime

from PySide.QtCore import *
from PyQt4.QtGui import *

from DTO import currentUserDTO, searchResultsDTO, userSearchDTO, topicsDTO
from DataBase import mySQLDatabaseConfig as dbConfig
from Views import dashBoardView
from ViewModels import addQuestionViewModel, barChartViewModel, aboutViewModel, editTopicViewModel, editUserViewModel, loadingViewModel


class DashBoard(QMainWindow, dashBoardView.Ui_MainWindow) :

    def __init__(self, email, parent = None) :
        super(DashBoard, self).__init__(parent)
        self.setupUi(self)

        #global variables
        self.CurrentQuestionSelectedId = -1
        self.SelectedTopicId = None
        self.TopicList = []


        self.DataBase = dbConfig.MySqlDatabaseConfig()

        self.User = currentUserDTO.CurrentUser(email)

        self.IsAdmin()

        self.welcomeLabel.setText(self.User.FirstName)

        self.currentTimeLabel.setText(str(datetime.datetime.now().date()))

        self.examButton.clicked.connect(self.Exam)
        self.profilButton.clicked.connect(self.Profil)
        self.adminButton.clicked.connect(self.Admin)
        self.resultsButton.clicked.connect(self.Results)
        self.logoutButton.clicked.connect(self.Logout)
        self.aboutButton.clicked.connect(self.About)
        self.addNewQuestionButton.clicked.connect(self.AddNewQuestionAndAnsers)
        self.myResultsBarChartButton.clicked.connect(self.ShowCurrentuserBarChart)
        self.showUserResultsBarChartButton.clicked.connect(self.ShowUsersbarChart)
        self.filterUsersButton.clicked.connect(self.SearchUsers)
        self.editQuestionButton.clicked.connect(self.EditQuestion)
        self.userEditButton.clicked.connect(self.EditOwnDatas)
        self.deleteQuestionButton.clicked.connect(self.DeleteQuestion)
        self.deleteTopicButton.clicked.connect(self.DeleteTopic)
        self.deleteUserButton.clicked.connect(self.DeleteUser)

        self.FillTopicsCombobox()

        self.stackedWidget.setCurrentIndex(1)



    def IsAdmin(self) :
        """
        Megvizsgáljuk a belépett felhasználó jogosultságát, ha adminisztrátor,
        akkor hozzáférhet az adminisztráció menüponthoz, különben nem.
        """
        if (self.User.Privilidge != 0) :
            self.adminButton.hide()
        else :
            self.adminButton.show()

    def Profil(self) :
        self.stackedWidget.setCurrentIndex(1)

        try :
            self.lastNameEditBox.setText(str(self.User.LastName))
            self.firstNameEditBox.setText(str(self.User.FirstName))
            self.emailEditBox.setText(str(self.User.Email))
            if self.User.City is not None :
                self.cityEditBox.setText(str(self.User.City))
            if self.User.Address is not None :
                self.addressEditBox.setText(str(self.User.Address))
            if self.User.Phone is not None :
                self.phoneEditBox.setText(str(self.User.Phone))
            if self.User.Birthday is not None :
                self.birthdayEditBox.setText(str(self.User.Birthday))
        except Exception as e :
            print e.args

    def Admin(self) :
        self.stackedWidget.setCurrentIndex(0)

        self.addNewQuestionButton.clicked.connect(self.AddNewQuestionAndAnsers)
        self.addNewTopicButton.clicked.connect(self.AddNewTopicToDatabase)

        self.refreshTopicButton.clicked.connect(self.FillQuestionListTable)

        self.editUserButton.clicked.connect(self.EditUser)
        self.editTopicButton.clicked.connect(self.EditTopic)

        self.FillQuestionListTable()

        self.FillTopicsTable()



    def Results(self) :
        self.stackedWidget.setCurrentIndex(3)

        self.filterResultButton.clicked.connect(self.SearchInResultsPage)

    def About(self) :
        self.aboutWindow = aboutViewModel.About()
        self.aboutWindow.show()



    def AddNewQuestionAndAnsers(self) :
        """
        Megnyilik az új kérdés hozzáadása ablak, ahol a kérdéshez tartozó válaszokat is meg lehet adni
        """
        self.addQuestionWindow = addQuestionViewModel.Question()
        self.addQuestionWindow.show()

    def EditQuestion(self) :
        from ViewModels import editQuestionViewModel

        self.editQuestionWindow = editQuestionViewModel.EditQuestion(self.CurrentQuestionSelectedId,
                                                                     self.topicListCombobox.currentIndex())
        self.editQuestionWindow.show()

    def DeleteQuestion(self):

        reply = QMessageBox.question(self, u"Megerősítés", u"Biztosan törölni szeretné az adott kérdést?",QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DataBase.DeleteQuestionById(self.CurrentQuestionSelectedId)




    def AddNewTopicToDatabase(self) :
        if (self.ValidateAddNewTopicsBoxText()) :
            self.DataBase.InsertIntoTopics(self.addNewTopicBox.text())

            self.topicListCombobox.clear()
            self.examsTypeCombobox.clear()
            self.FillTopicsCombobox()

            self.FillTopicsTable()

            #QMessageBox.about(self, u"Sikeres hozzáadás", u"A téma hozzáadása sikeresen megtörtént.")

    def ValidateAddNewTopicsBoxText(self) :
        error = ""
        validNameFormat = u"^[a-zA-Z+#\s]+$"

        if (self.addNewTopicBox.text() == "") :
            error += u"A téma neve nem lehet üres!\n"
        if (self.addNewTopicBox.text() != "" and re.match(validNameFormat, self.addNewTopicBox.text()) == None) :
            error += u"A téma neve csak az angol ábécé karaktereit tartalmazhatja, illetve a + és # szimbólumokat!\n"

        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else :
            return True

    def Logout(self) :
        """
        Kijelentkezés
        """
        self.close()

    def Exam(self) :
        self.stackedWidget.setCurrentIndex(2)
        self.UserAnswers = []

        print(u"User answers tartalma TABVÁLTÁS: %s"%self.UserAnswers)

        self.timer = QTimer()

        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        palette = self.lcdNumber.palette()
        palette.setColor(palette.WindowText, QColor(0, 255, 0))
        self.lcdNumber.setPalette(palette)
        self.start_time = 1800
        self.lcdNumber.display("%02d:%02d" % (self.start_time / 60, self.start_time % 60))



        #self.examsTypeCombobox.activated.connect(self.SelectedTopics)
        self.examsTypeCombobox.setCurrentIndex(0)
        self.GenerateQuizByTopic()
        self.examsTypeCombobox.currentIndexChanged.connect(self.GenerateQuizByTopic)
        self.currentExamTableView.setVisible(False)
        self.sendExamButton.setVisible(False)

        self.startExamButton.clicked.connect(self.SetupCountDown)
        self.timer.timeout.connect(self.updateLCD)

        self.sendExamButton.clicked.connect(self.SubmitAnswers)



        self.CurrentTopicId
        self.questionIds

    def SetupCountDown(self) :
        #Kapcsolótábla feltöltése
        self.DataBase.InsertIntoTopicUserConn(self.CurrentTopicId, self.User.UserId)

        self.currentExamTableView.setVisible(True)
        self.sendExamButton.setVisible(True)
        self.startExamButton.setEnabled(False)
        self.examsTypeCombobox.setEnabled(False)
        self.timer.stop()
        self.start_time = 1800
        self.lcdNumber.display("%02d:%02d" % (self.start_time / 60, self.start_time % 60))
        # Restart the timer
        self.timer.start(1000)

    def updateLCD(self) :
        # Update the lcd
        self.start_time -= 1
        if self.start_time >= 0 :
            self.lcdNumber.display("%02d:%02d" % (self.start_time / 60, self.start_time % 60))
        else :
            self.timer.stop()
            self.examsTypeCombobox.setEnabled(True)
            self.SubmitAnswers()
            self.sendExamButton.setEnabled(False)
            #self.startExamButton.setEnabled(True)
            #self.start_time = 5
            #self.lcd.display("%d:%02d" % (self.start_time/60,self.start_time % 60))

    def FillTopicsCombobox(self) :
        _topicsList = self.DataBase.GetTopicsName()


        #todo:teszt

        self.TopicList = self.DataBase.GetTopicsList()



        self.examsTypeCombobox.clear()
        self.topicListCombobox.clear()

        self.examsTypeCombobox.addItems(_topicsList)
        self.topicListCombobox.addItems(_topicsList)

    def GenerateQuizByTopic(self) :
        self.yourPointsLabel.setText("")
        self.maxPointsLabel.setText("")





        self.currentExamTableView.setVisible(False)
        self.sendExamButton.setVisible(False)

        self.startExamButton.setEnabled(True)
        model = QStandardItemModel(self.currentExamTableView)
        model.clear()

        _questionList = []
        _answerList = []
        questionListWithId = []
        questionIds = []


        #todo:hb
        #for topic in self.TopicList:
        #    if topic.


        topics = unicode(self.examsTypeCombobox.currentText())
        topicsId = self.DataBase.GetTopicsIndexByName(topics)
        self.CurrentTopicId = topicsId

        for item in self.DataBase.GetQustionsByTopicsId(topicsId) :

            _questionList.append(item[1])
            questionListWithId.append(item)


        for item in self.DataBase.GetQustionsByTopicsId(topicsId) :

            questionIds.append(item[0])

        self.questionIds = questionIds

        for question in questionListWithId :
            answer = self.DataBase.GetAnswersForQuestionByQuestionId(question[0])
            _answerList.append(answer)

        for i in range(len(questionListWithId)) :
            questionStandardItemQuestionRow = []
            questionStandardItemQuestionIdCell = QStandardItem("%d" % questionListWithId[i][0])
            questionStandardItemQuestionTextCell = QStandardItem("%d.) %s" % (i + 1, questionListWithId[i][1]))
            questionStandardItemEmptyCell = QStandardItem("")
            questionStandardItemQuestionRow.append(questionStandardItemQuestionIdCell)
            questionStandardItemQuestionRow.append(questionStandardItemQuestionTextCell)
            questionStandardItemQuestionRow.append(questionStandardItemEmptyCell)
            #questionStandardItemQuestionTextCell.appendColumn()
            questionStandardItemQuestionTextCell.setEditable(False)
            #model.appendColumn(questionStandardItemQuestionIdCell)
            model.appendRow(questionStandardItemQuestionRow)

            for j in range(len(_answerList)) :
                for k in range(len(_answerList[j])) :
                    if i == j :
                        answerRow = []
                        answerIndex = QStandardItem("%d" % _answerList[j][k][0])
                        answerText = QStandardItem(_answerList[j][k][1])
                        questionId = QStandardItem("%d" % _answerList[j][k][2])
                        answerRow.append(answerIndex)
                        answerRow.append(answerText)
                        answerRow.append(questionId)

                        answerText.setCheckable(True)
                        answerText.setEditable(False)
                        model.appendRow(answerRow)
                        #model.appendRow("")

        #myListView.setModel(model)
        #self.currentExamListView.setModel(model)
        self.currentExamTableView.setModel(model)
        self.currentExamTableView.setColumnHidden(0, True)
        self.currentExamTableView.setColumnHidden(2, True)
        self.currentExamTableView.verticalHeader().setVisible(False)

        #self.currentExamTableView.setColumnWidth(1,500)
        header = self.currentExamTableView.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)

    def SubmitAnswers(self) :
        self.timer.stop()
        self.examsTypeCombobox.setEnabled(True)

        maxPoint = len(self.questionIds)

        self.maxPointsLabel.setText("%d" % maxPoint)

        userPoints = 0

        __model = self.currentExamTableView.model()

        for row in range(__model.rowCount()) :
            for column in range(__model.columnCount()) :
                item = __model.item(row, column)

                if item.isCheckable and (item.checkState() == Qt.Checked) :
                    answersList = []
                    answerId = __model.item(row, 0)
                    questionId = __model.item(row, 2)

                    self.DataBase.InsertIntoUserAnswers(int(questionId.text()), int(answerId.text()))
                    answersList.append(int(answerId.text()))

                    answersList.append(int(questionId.text()))
                    self.UserAnswers.append(answersList)

        goodAnswersList = self.DataBase.GetCorrectAnswersByTopicId(self.CurrentTopicId)

        goodAnswers = []
        for answer in goodAnswersList:
            goodAnswers.append(answer[0])

        wrongAnswerIds = []
        correctAnswerids = []

        for userAnswer in self.UserAnswers :
            if userAnswer[0] not in goodAnswers:
                wrongAnswerIds.append(userAnswer[0])
            else:
                correctAnswerids.append(userAnswer[0])

        wrongQuestionIds = []
        if wrongAnswerIds:
            for id in wrongAnswerIds:
                kid = self.DataBase.GetQuestionIdByAnswerId(id)
                wrongQuestionIds.append(kid[0][0])

        correctQuestionIds = []
        if correctAnswerids:
            for id in correctAnswerids:
                kid = self.DataBase.GetQuestionIdByAnswerId(id)
                correctQuestionIds.append(kid[0][0])

        wrong = []
        if wrongQuestionIds:
            for item in wrongQuestionIds:
                if item not in wrong:
                    wrong.append(item)

        correct = []
        if correctQuestionIds:
            for item in correctQuestionIds:
                if item not in correct:
                    correct.append(item)

        countPoint = 0
        for i in correct:
            if i not in wrong:
                countPoint += 1

        userPoints = countPoint

        self.yourPointsLabel.setText("%d" % userPoints)

        self.DataBase.InsertIntoResults(userPoints, self.User.UserId, self.CurrentTopicId, datetime.datetime.today())

    def ShowCurrentuserBarChart(self) :
        barChart = barChartViewModel.BarChart(self.User.UserId)
        barChart.show()

    def ShowUsersbarChart(self) :
        barChart = barChartViewModel.BarChart(self.SelectedUserId)
        barChart.show()

    #Result részek vége

    #Admin részek

    def ValidateUserFilterTexts(self) :
        error = ""
        #http://stackoverflow.com/questions/19352956/yyyy-mm-dd-date-format-regular-expression
        validDateFormat = "\d{4}(?:-\d{1,2}){2}"
        validNameFormat = u"^[a-zA-ZáéíöüóőúűÁÉÍÖÜÓŐÚŰ\s]+$"
        validAddressFormat = u"^([a-zA-Z0-9áÁéÉíÍóÓöÖőŐúÚüÜűŰ \/.,-]{1,})$"
        validPhoneFormat = u"^([0-9 +]{1,50})$"
        validCityFormat = u"^([a-zA-ZáÁéÉíÍóÓöÖőŐúÚüÜűŰ]{1,})$"
        validEmailFormat = "[^@]+@[^@]+\.[^@]+"

        if self.lastNameFilterBox.text() != "" and re.match(validNameFormat, self.lastNameFilterBox.text()) == None :
            error += u"A vezetéknév mező nem megengedett karaktereket tartalmaz!\n     Helyes formátum: Kovács\n"
        if self.firstNameFilterBox.text() != "" and re.match(validNameFormat, self.firstNameFilterBox.text()) == None :
            error += u"A keresztnév mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Krisztina\n"
        if self.addressFilterBox.text() != "" and re.match(validAddressFormat, self.addressFilterBox.text()) == None :
            error += u"A cím mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Hungária körút 81. 3. emelet 18/A\n"
        if self.phoneFilterBox.text() != "" and re.match(validPhoneFormat, self.phoneFilterBox.text()) == None :
            error += u"A telefonszám mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 301234567\n"
        if self.cityFilterBox.text() != "" and re.match(validCityFormat, self.cityFilterBox.text()) == None :
            error += u"A város mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Budapest\n"
        if self.ageFilterBox.text() != "" and re.match(validDateFormat, self.ageFilterBox.text()) == None :
            error += u"A születési idő mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 1970-10-01\n"
        if self.registeredFilterBox.text() != "" and re.match(validDateFormat, self.registeredFilterBox.text()) == None :
            error += u"A regisztrálás dátuma mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 1970-10-01\n"
        if self.emailFilterBox.text() != "" and re.match(validEmailFormat, self.emailFilterBox.text()) == None :
            error += u"Az email mező nem megengedett karaktereket tartalmaz!\n     Helyes formátum: email@cim.com\n"

        if self.lessCheckbox.isChecked() and self.equalCheckbox.isChecked() and self.moreChecbox.isChecked() :
            error += u"A kisebb(<), a nagyobb(>) és az egyenlő(=) checkBox egyszerre együtt nem lehet bepipálva!\n"

        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else :
            return True


    def SearchUsers(self) :

        if self.ValidateUserFilterTexts() :

            #conditionList = []
            userFilterDatas = userSearchDTO.UserSearchDto()

            if self.lastNameFilterBox.text() != "" :
                userFilterDatas.LastName = self.lastNameFilterBox.text()
            if self.firstNameFilterBox.text() != "" :
                userFilterDatas.FirstName = self.firstNameFilterBox.text()
            if self.cityFilterBox.text() != "" :
                userFilterDatas.City = self.cityFilterBox.text()
            if self.ageFilterBox.text() != "" :
                userFilterDatas.Birthday = self.ageFilterBox.text()
            if self.addressFilterBox.text() != "" :
                userFilterDatas.Address = self.addressFilterBox.text()
            if self.emailFilterBox.text() != "" :
                userFilterDatas.Email = self.emailFilterBox.text()
            if self.phoneFilterBox.text() != "" :
                userFilterDatas.Phone = self.phoneFilterBox.text()
            if self.registeredFilterBox.text() != "" :

                userFilterDatas.Registered = self.registeredFilterBox.text()
            if self.ageFilterBox.text() != "" :

                userFilterDatas.Birthday = self.ageFilterBox.text()

            if self.lessCheckbox.isChecked() and self.equalCheckbox.isChecked() :
                userFilterDatas.LessOrEqual = True
            else :
                if self.moreChecbox.isChecked() and self.equalCheckbox.isChecked() :
                    userFilterDatas.MoreOrEqual = True
                else :
                    if self.lessCheckbox.isChecked() and self.moreChecbox.isChecked() :
                        userFilterDatas.NotEqual = True
                    else :
                        if self.lessCheckbox.isChecked() :
                            userFilterDatas.Less = True
                        else :
                            if self.moreChecbox.isChecked() :
                                userFilterDatas.More = True
                            else :
                                if self.equalCheckbox.isChecked() :
                                    userFilterDatas.Equal = True

            try :
                users = self.DataBase.FilterUsersByConditions(userFilterDatas)

                self.UserIdListResultPage = []
                self.UserListDto = []

                self.usersListTable.setRowCount(len(users))

                self.usersListTable.setColumnCount(9)

                for i in range(0, len(users)) :
                    self.UserIdListResultPage.append(users[i][0])
                    __currentUser = currentUserDTO.CurrentUser(users[i][2])
                    self.UserListDto.append(__currentUser)
                    for j in range(0, len(users[i])) :
                        label = QLabel()
                        if users[i][j] == None :
                            label.setText("")
                        else :
                            label.setText(str(users[i][j]))

                        if j == 8 :
                            if users[i][j] == 0 :
                                label.setText("Admin")
                            else :
                                label.setText(u"Felhasználó")
                        self.usersListTable.setCellWidget(i, j, label)


            except Exception as e :
                QMessageBox.about(self, u"Hiba", e.args)

            self.usersListTable.setColumnWidth(0, 25)
            self.usersListTable.setColumnWidth(1, 300)
            self.usersListTable.setColumnWidth(2, 200)
            self.usersListTable.setColumnWidth(3, 120)
            self.usersListTable.setColumnWidth(4, 150)
            self.usersListTable.setColumnWidth(5, 200)
            self.usersListTable.setColumnWidth(7, 75)
            self.usersListTable.setColumnWidth(8, 100)

            self.usersListTable.cellClicked.connect(self.SelectedUserInAdminArea)

    def ValidateResultPageFilters(self):
        error = ""

        validDateFormat = "\d{4}(?:-\d{1,2}){2}"
        validNameFormat = u"^[a-zA-ZáéíöüóőúűÁÉÍÖÜÓŐÚŰ\s]+$"
        validTopicFormat = u"^[a-zA-Z+#\s]+$"
        validEmailFormat = u"^[a-zA-Z0-9@.\s]+$"#"[^@]+@[^@]+\.[^@]+"
        validScoreFormat = "^[0-9]\d{0,2}$"

        if self.resultPageLastNameFilterBox.text() != "" and re.match(validNameFormat, self.resultPageLastNameFilterBox.text()) == None :
            error += u"A vezetéknév mező nem megengedett karaktereket tartalmaz!\n     Helyes formátum: Kovács\n"
        if self.resultPageFirstNameFilterBox.text() != "" and re.match(validNameFormat, self.resultPageFirstNameFilterBox.text()) == None :
            error += u"A keresztnév mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Krisztina\n"
        if self.topicsDateFilterBox.text() != "" and re.match(validDateFormat, self.topicsDateFilterBox.text()) == None :
            error += u"A vizsga dátuma mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 2014-10-01\n"
        if self.resultPageEmailFilterBox.text() != "" and re.match(validEmailFormat, self.resultPageEmailFilterBox.text()) == None :
            error += u"Az email mező nem megengedett karaktereket tartalmaz!\n"
        if (self.topicsFilterBox.text() != "" and re.match(validTopicFormat, self.topicsFilterBox.text()) == None) :
            error += u"A téma neve csak az angol ábécé karaktereit tartalmazhatja, illetve a + és # szimbólumokat!\n"
        if (self.scoreFilterBox.text() != "" and re.match(validScoreFormat, self.scoreFilterBox.text()) == None) :
            error += u"A pontszám mezőbe maximum 3 jegyű, pozitív egész számok kerülhetnek!\n"

        if self.resultLessCheckbox.isChecked() and self.resultEqualCheckbox.isChecked() and self.resultMoreCheckbox.isChecked() :
            error += u"A kisebb(<), a nagyobb(>) és az egyenlő(=) checkBox egyszerre együtt nem lehet bepipálva!\n"

        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else :
            return True

    def SearchInResultsPage(self):

        if self.ValidateResultPageFilters():
            conditionList = []
            userFilterDatas = searchResultsDTO.SearchInResults()

            if self.topicsFilterBox.text() != "":
                userFilterDatas.Topic = self.topicsFilterBox.text()
            if self.topicsDateFilterBox.text() != "":
                userFilterDatas.ExamDate = self.topicsDateFilterBox.text()
            if self.scoreFilterBox.text() != "":
                userFilterDatas.Result = self.scoreFilterBox.text()
            if self.resultPageEmailFilterBox.text() != "":
                userFilterDatas.Email = self.resultPageEmailFilterBox.text()
            if self.resultPageLastNameFilterBox.text() != "":
                userFilterDatas.LastName = self.resultPageLastNameFilterBox.text()
            if self.resultPageFirstNameFilterBox.text() != "":
                userFilterDatas.FirstName = self.resultPageFirstNameFilterBox.text()

            if self.resultLessCheckbox.isChecked() and self.resultEqualCheckbox.isChecked() :
                userFilterDatas.LessOrEqual = True
            else :
                    if self.resultMoreCheckbox.isChecked() and self.resultEqualCheckbox.isChecked() :
                        userFilterDatas.MoreOrEqual = True
                    else :
                        if self.resultLessCheckbox.isChecked() and self.resultMoreCheckbox.isChecked() :
                            userFilterDatas.NotEqual = True
                        else :
                            if self.resultLessCheckbox.isChecked() :
                                userFilterDatas.Less = True
                            else :
                                if self.resultMoreCheckbox.isChecked() :
                                    userFilterDatas.More = True
                                else :
                                    if self.resultEqualCheckbox.isChecked() :
                                        userFilterDatas.Equal = True

        try :
            loading = loadingViewModel.Loading()
            loading.show()

            users = self.DataBase.SearchInResultPage(userFilterDatas)


            self.UserIdListResultPage = []
            self.UserListDto = []

            self.usersResultsListTable.setRowCount(len(users))

            self.usersResultsListTable.setColumnCount(6)

            for i in range(0, len(users)) :
                self.UserIdListResultPage.append(users[i][0])
                __currentUser = currentUserDTO.CurrentUser(users[i][2])
                self.UserListDto.append(__currentUser)
                for j in range(0, len(users[i])) :
                    label = QLabel()
                    if users[i][j] == None :
                        label.setText("")
                    else :
                        label.setText(str(users[i][j]))


                    self.usersResultsListTable.setCellWidget(i, j, label)
            loading.close()


        except Exception as e :
            QMessageBox.about(self, u"Hiba", e.args)

        self.usersResultsListTable.setColumnWidth(0, 25)
        self.usersResultsListTable.setColumnWidth(1, 300)
        self.usersResultsListTable.setColumnWidth(2, 200)
        self.usersResultsListTable.setColumnWidth(3, 120)
        self.usersResultsListTable.setColumnWidth(4, 150)
        self.usersResultsListTable.setColumnWidth(5, 200)


        self.usersResultsListTable.cellClicked.connect(self.UserSelected)

    def UserSelected(self) :
        """
        Ha az eredmények menüpontban kiválasztunk egy felhasználót, akkor ha az oszlopdiagram gombra kattintunk
        megnyílik az oszlopdiagram az aktuálisan kiválasztott felhasználó eredményeimvel
        """
        row = self.usersResultsListTable.currentIndex().row()
        self.SelectedUserId = self.UserIdListResultPage[row]


    def SelectedUserInAdminArea(self) :
        row = self.usersListTable.currentIndex().row()
        self.SelecteduserDtoToEdit = self.UserListDto[row]



    def EditUser(self) :
        self.editUserWindow = editUserViewModel.EditUser(self.SelecteduserDtoToEdit)
        self.editUserWindow.show()


    def DeleteUser(self):
        reply = QMessageBox.question(self, u"Megerősítés", u"Biztosan törölni szeretné az adott felhsználót?",QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DataBase.DeleteUserById(self.SelecteduserDtoToEdit.UserId)

    #Admin részek vége

    def FillQuestionListTable(self) :
        topics = unicode(self.topicListCombobox.currentText())

        topicsId = self.DataBase.GetTopicsIndexByName(topics)

        questionList = self.DataBase.GetQustionsByTopicsId(topicsId)

        self.questionIdsList = []

        self.questionsListTable.setRowCount(len(questionList))
        self.questionsListTable.setColumnCount(2)

        for i in range(0, len(questionList)) :
            self.questionIdsList.append(questionList[i][0])
            for j in range(0, len(questionList[i])) :
                label = QLabel()
                label.setText(str(questionList[i][j]))
                self.questionsListTable.setCellWidget(i, j, label)

        self.questionsListTable.hideColumn(0)

        header = self.questionsListTable.horizontalHeader()
        header.setStretchLastSection(True)

        self.questionsListTable.cellClicked.connect(self.SelectedQuestionId)

    def SelectedQuestionId(self) :
        row = self.questionsListTable.currentIndex().row()
        self.CurrentQuestionSelectedId = self.questionIdsList[row]

        self.FillAnswersListTable()

    def FillTopicsTable(self) :

        topicsList = self.DataBase.GetTopicsList()
        self.topicsIdList = []

        self.topicsTable.setRowCount(len(topicsList))

        self.topicsTable.setColumnCount(2)

        for i in range(0, len(topicsList)) :
            self.topicsIdList.append(topicsList[i][0])
            for j in range(0, len(topicsList[i])) :
                label = QLabel()
                label.setText(str(topicsList[i][j]))
                self.topicsTable.setCellWidget(i, j, label)

        header = self.topicsTable.horizontalHeader()
        header.setStretchLastSection(True)

        self.topicsTable.cellClicked.connect(self.TopicSelected)

    def EditTopic(self) :
        if self.SelectedTopicId != None :
            self.editTopicWindow = editTopicViewModel.EditTopic(self.SelectedTopicId)
            self.editTopicWindow.show()

    def DeleteTopic(self):
        reply = QMessageBox.question(self, u"Megerősítés", u"Biztosan törölni szeretné az adott témát?",QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.DataBase.DeleteTopicById(self.SelectedTopicId)

    def TopicSelected(self) :
        row = self.topicsTable.currentIndex().row()
        self.SelectedTopicId = self.topicsIdList[row]

        questionList = self.DataBase.GetQustionsByTopicsId(self.SelectedTopicId)

        self.questionIdList = []

        self.questionsTable.setRowCount(len(questionList))
        self.questionsTable.setColumnCount(2)

        for i in range(0, len(questionList)) :
            self.questionIdList.append(questionList[i][0])
            for j in range(0, len(questionList[i])) :
                label = QLabel()
                label.setText(str(questionList[i][j]))
                self.questionsTable.setCellWidget(i, j, label)

        self.questionsTable.hideColumn(0)

        header = self.questionsTable.horizontalHeader()
        header.setStretchLastSection(True)

        self.questionsTable.cellClicked.connect(self.QuestionSelected)

    def FillAnswersListTable(self) :
        answerList = self.DataBase.GetAnswersForQuestionByQuestionId(self.CurrentQuestionSelectedId)



        self.answersListTable.setRowCount(len(answerList))
        self.answersListTable.setColumnCount(4)

        for i in range(0, len(answerList)) :
            for j in range(0, len(answerList[i])) :
                label = QLabel()
                checkBox = QCheckBox()
                if j != 3 :
                    if answerList[i][j] == None :
                        label.setText("")
                    else :
                        label.setText(str(answerList[i][j]))
                    self.answersListTable.setCellWidget(i, j, label)
                else :
                    if answerList[i][j] == 1 :
                        checkBox.setChecked(True)
                    else :
                        checkBox.setChecked(False)
                    checkBox.setDisabled(True)
                    self.answersListTable.setCellWidget(i, j, checkBox)

        self.answersListTable.hideColumn(0)
        self.answersListTable.hideColumn(2)
        self.answersListTable.setColumnWidth(1, 300)

    def QuestionSelected(self) :

        row = self.questionsTable.currentIndex().row()
        self.SelectedQuestionId = self.questionIdList[row]


        answerList = self.DataBase.GetAnswersForQuestionByQuestionId(self.SelectedQuestionId)

        self.answerIdList = []

        self.answersTable.setRowCount(len(answerList))
        self.answersTable.setColumnCount(4)

        for i in range(0, len(answerList)) :
            self.answerIdList.append(answerList[i][0])
            for j in range(0, len(answerList[i])) :
                label = QLabel()
                checkBox = QCheckBox()
                if j != 3 :
                    if answerList[i][j] == None :
                        label.setText("")
                    else :
                        label.setText(str(answerList[i][j]))
                    self.answersTable.setCellWidget(i, j, label)
                else :
                    if answerList[i][j] == 1 :
                        checkBox.setChecked(True)
                    else :
                        checkBox.setChecked(False)
                    checkBox.setDisabled(True)
                    self.answersTable.setCellWidget(i, j, checkBox)

        self.answersTable.hideColumn(0)
        self.answersTable.hideColumn(2)
        self.answersTable.setColumnWidth(1, 300)

        header = self.answersTable.horizontalHeader()
        header.setStretchLastSection(True)

    def EditOwnDatas(self):
        if self.ValidateCurrentUserDatas():

            firstName = unicode(self.firstNameEditBox.text())
            lastName = unicode(self.lastNameEditBox.text())
            email = unicode(self.emailEditBox.text())

            self.User.FirstName = firstName
            self.User.LastName = lastName
            self.User.Email = email
            self.User.City = unicode(self.cityEditBox.text())
            self.User.Address = unicode(self.addressEditBox.text())
            self.User.Phone = unicode(self.phoneEditBox.text())
            if self.birthdayEditBox.text() == "":
                 self.User.Birthday = None
            else:
                self.User.Birthday = unicode(self.birthdayEditBox.text())
            password = unicode(self.passwordEditBox.text())

            self.DataBase.UpdateOwnUserDataAndProfil(self.User,password)
            QMessageBox.about(self, u"Sikeres adatváltoztatás",u"Adatok sikeresen megváltoztatva.")

    def ValidateCurrentUserDatas(self):
        error = ""
        validEmailPattern = "[^@]+@[^@]+\.[^@]+"
        # http://www.mkyong.com/regular-expressions/how-to-validate-password-with-regular-expression/
        validPasswordPattern = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[/+@#$%]).{8,20})"
        validNameFormat = u"^[a-zA-ZáéíöüóőúűÁÉÍÖÜÓŐÚŰ\s]+$"
        validPhoneFormat = u"^([0-9 +]{1,50})$"
        validCityFormat = u"^([a-zA-ZáÁéÉíÍóÓöÖőŐúÚüÜűŰ]{1,})$"
        validAddressFormat = u"^([a-zA-Z0-9áÁéÉíÍóÓöÖőŐúÚüÜűŰ \/.,-]{1,})$"
        validDateFormat = "\d{4}(?:-\d{1,2}){2}"


        if self.firstNameEditBox.text() == "":
            error += u"A keresztnév kitöltése kötelező!\n"
        if self.lastNameEditBox.text() == "":
            error += u"A vezetéknév kitöltése kötelező!\n"
        if self.emailEditBox.text() == "":
            error += u"Az email cím megadása kötelező!\n"
        if self.passwordEditBox.text() == "" or self.passwordEditBox.text() == "":
            error += u"A jelszó és a jelszó újra mezők kitöltése kötelező!\n"
        if self.passwordEditBox.text() != self.passwordAgainEditBox.text():
            error += u"A két jelszó nem egyezik!\n"
        if self.emailEditBox.text() != "" and re.match(validEmailPattern,self.emailEditBox.text())==None:
            error += u"Nem érvényes email formátum!\n"
        if self.passwordEditBox.text() != "" and re.match(validPasswordPattern,self.passwordEditBox.text())==None:
            error += u"A jelszónak legalább 8 karakternek kell lennie és tartalmaznia kell:\n     legalább egy számot,\n     egy kisbetűt,\n     egy nagybetűt\n     és egy speciális karaktert a következők közül: /@#$% \n"
        if self.firstNameEditBox.text() != "" and re.match(validNameFormat,self.firstNameEditBox.text())==None:
            error += u"A keresztnév nem megengedett karaktereket tartalmaz!\n    (Csak a magyar ábécé karaktereit tartalmazhatja)\n"
        if self.lastNameEditBox.text() != "" and re.match(validNameFormat,self.lastNameEditBox.text())==None:
            error += u"A vezetéknév nem megengedett karaktereket tartalmaz!\n    (Csak a magyar ábécé karaktereit tartalmazhatja)\n"
        if self.addressEditBox.text()!="" and re.match(validAddressFormat,self.addressEditBox.text())==None:
            error += u"A cím mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Hungária körút 81. 3. emelet 18/A\n"
        if self.phoneEditBox.text()!="" and re.match(validPhoneFormat,self.phoneEditBox.text())==None:
            error += u"A telefonszám mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 301234567\n"
        if self.cityEditBox.text()!="" and re.match(validCityFormat,self.cityEditBox.text())==None:
            error += u"A város mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: Budapest\n"
        if self.birthdayEditBox.text()!="" and re.match(validDateFormat,self.birthdayEditBox.text())==None:
            error += u"A születési idő mező nem megengedett karaktereket tartalmaz!\n    Helyes formátum: 1970-10-01\n"


        if error :
            QMessageBox.about(self, u"Hiba", error)
            return False
        else:
            return True






