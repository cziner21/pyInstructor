#coding: utf8
import pyodbc

class DataBaseConfig(object):

    def __init__(self):
        self.ConnectionString = 'DRIVER={SQL Server};SERVER=ADAMLT\SQLEXPRESS;DATABASE=szakdolgozat;'
        #self.ConnectionString = pyodbc.connect('DRIVER={SQL Server};SERVER=ADAMLT\SQLEXPRESS;DATABASE=szakdolgozat;')

    def GetTopicsName(self):
        """
        Témakörök nevének kigyűjtése
        @return: Témakörlista
        """

        try:
            topicsNameList = []
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("select * from topics")
            rows = Cursor.fetchall()
            for row in rows:
                topicsNameList.append(row.name)
            return topicsNameList
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetTopicsIndexByName(self,topicsName):
        """
        Témakörök idjainak kigyűjtése
        @return: Témakör id lista
        """

        try:
            topicsId = 0
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("select id from topics where name=?",topicsName)
            rows = Cursor.fetchall()
            for row in rows:
                topicsId = row.id
            return topicsId
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetQustionsByTopicsId(self,topicsId):
        """
        Kérdések listázása témakörönként
        @param topicsId: Témakör azonosító
        @return: Kérdések listája
        """

        try:
            questionList = []
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("select * from questions where topicId=?",topicsId)
            rows = Cursor.fetchall()
            for row in rows:
                questionList.append(row)
            return questionList
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetAnswersForQuestionByQuestionId(self,questionId):
        """
        Válaszok listázása kérdésenként
        @param questionId: Kérédés azonosító
        @return: Kérdéshez tartózó válaszok listája
        """
        try:
            connection = pyodbc.connect(self.ConnectionString)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select * from answers where questionId=?",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row)
            return answerList
        except Exception:
            print Exception.message
        finally:
            connection.close()


    def GetAnswersForTopicsByTopicsId(self,topicsId):
        """
        Válaszok listázása témakörönként
        @param topicsId: Témakör azonosító
        @return: Témakörhöz tartozó válaszok listája
        """
        try:
            connection = pyodbc.connect(self.ConnectionString)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select answerText from answers where topicsId=?",topicsId)
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row.answerText)
            return answerList
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetAnswerIdByAnswerId(self,answerText,questionId):
        """
        Válaszok idjainak listája
        @param topicsId: Témakör azonosító
        @return: Témakörhöz tartozó válaszok listája
        """
        try:
            connection = pyodbc.connect(self.ConnectionString)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select id from answers where answerText=? and questionId=?",answerText,questionId)
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row.id)
            return answerList
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetCorrectAnswersByQuestionId(self,questionId):
        """
        Jó válaszok idjainak listája
        @param topicsId: Témakör azonosító
        @param questionId: kérdés azonosító
        @return: Témakörhöz és kérdéshez tartozó válaszok listája
        """
        try:
            connection = pyodbc.connect(self.ConnectionString)
            correctAnswerList = []
            Cursor = connection.cursor()
            Cursor.execute("select * from correctAnswers where questionId=?",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                correctAnswerList.append(row)
            return correctAnswerList
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetUserAnswersByQuestionId(self,questionId):
        """
        User válaszainak  listája
        @param topicsId: Témakör azonosító
        @param questionId: kérdés azonosító
        @return: Témakörhöz és kérdéshez tartozó válaszok listája
        """
        try:
            connection = pyodbc.connect(self.ConnectionString)
            userAnswers = []
            Cursor = connection.cursor()
            Cursor.execute("select * from userAnswers where questionId=?",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                userAnswers.append(row)
            return userAnswers
        except Exception:
            print Exception.message
        finally:
            connection.close()

    #Insert
    def InsertIntoUserAnswers(self,answerId,topicsId,questionId):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("insert into userAnswers(answerId,topicsId,questionId) values(?,?,?)",answerId,topicsId,questionId)
            connection.commit()
        except Exception as e:
            print e.message
        finally:
            connection.close()

    def InsertIntoResults(self,result,examId,topicId,userId):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("insert into results(result,examId,topicID,userid) values(?,?,?,?)",result,examId,topicId,userId)
            connection.commit()
        except Exception:
            print Exception.message
        finally:
            connection.close()

    #Kapcsolótáblák feltöltése

    def InsertIntoTopicUserConn(self,topicId,userId):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("insert into topics_users_conn(topicId, userId) values(?,?)",topicId, userId)
            connection.commit()
        except Exception:
            print Exception.message
        finally:
            connection.close()

    #########################

    def InsertIntoExams(self,examDate,topicsId):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("insert into exams(examDate,topicsId) values(?,?)",examDate,topicsId)
            connection.commit()
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def MaxPointsForTopicsId(self,topicsId):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("select count(*) from correctAnswers where topicsId = ?",topicsId)
            rows = Cursor.fetchall()
            #for i in range(0,rows):
            return  rows
        except Exception:
            print Exception.message
        finally:
            connection.close()

    def GetLastExam(self):
        try:
            connection = pyodbc.connect(self.ConnectionString)
            Cursor = connection.cursor()
            Cursor.execute("SELECT TOP 1 * FROM exams ORDER BY id DESC")
            rows = Cursor.fetchall()
            for row in rows:
                id = row.id
            return  id
        except Exception:
            print Exception.message
        finally:
            connection.close()