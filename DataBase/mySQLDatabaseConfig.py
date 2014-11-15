#coding: utf8
import MySQLdb
import hashlib, datetime
from PyQt4.QtGui import *
import logging, time

class MySqlDatabaseConfig(object):

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd= ''
        self.db = 'pyinstructor'

        dateTimeStamp = time.strftime('%Y%m%d%H%M%S')
        logFile = 'logs/' + dateTimeStamp + '.log'
        logging.basicConfig(filename=logFile,level=logging.DEBUG,format='%(asctime)s :\n %(message)s')

    #GET utasítások

    def GetTopicsName(self):
        """
        Témakörök nevének kigyűjtése
        @return: Témakörlista
        """

        try:
            topicsNameList = []
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select * from topics")
            rows = Cursor.fetchall()
            for row in rows:
                topicsNameList.append(row[1])
            #print topicsNameList
            return topicsNameList
        except Exception as e:
            print e.args
            logging.warning('Error while GetTopicName:\n    %s'%e.args)
        finally:
            connection.close()

    def GetTopicsIndexByName(self,topicsName):
        """
        Témakörök idjainak kigyűjtése
        @return: Témakör id lista
        """

        try:
            topicsId = 0
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select id from topics where name = %s",topicsName)
            rows = Cursor.fetchall()

            return rows[0][0]
        except Exception as e:
            print e.args
            logging.warning('Error while GetTopicsIndexByName:\n    %s'%e.args)
        finally:
            connection.close()

    def GetTopicNameById(self,topicId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select name from topics where id = %s",(topicId))
            row = Cursor.fetchall()

            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetTopicNameById:\n    %s'%e.args)
        finally:
            connection.close()

    def GetTopicsList(self):
        try:

            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select * from topics")
            rows = Cursor.fetchall()

            return rows
        except Exception as e:
            print e.args
            logging.warning('Error while GetTopicsList:\n    %s'%e.args)
        finally:
            connection.close()

    def GetQustionsByTopicsId(self,topicId):
        """
        Kérdések listázása témakörönként
        @param topicsId: Témakör azonosító
        @return: Kérdések listája
        """

        try:
            questionList = []
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select * from questions where topicId=%s",topicId)
            rows = Cursor.fetchall()
            for row in rows:
                questionList.append(row)
            return questionList
        except Exception as e:
            print e.args
            logging.warning('Error while GetQustionsByTopicsId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetQuestionByQuestionId(self,questionId):
        try:
            questionList = []
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select * from questions where id=%s",questionId)
            rows = Cursor.fetchall()

            return rows
        except Exception as e:
            print e.args
            logging.warning('Error while GetQuestionByQuestionId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetAnswersForQuestionByQuestionId(self,questionId):
        """
        Válaszok listázása kérdésenként
        @param questionId: Kérédés azonosító
        @return: Kérdéshez tartózó válaszok listája
        """
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select * from answers where questionId=%s",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row)
            return answerList
        except Exception as e:
            print e.args
            logging.warning('Error while GetAnswersForQuestionByQuestionId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetAnswersForTopicsByTopicsId(self,topicId):
        """
        Válaszok listázása témakörönként
        @param topicsId: Témakör azonosító
        @return: Témakörhöz tartozó válaszok listája
        """
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select answerText from answers where topicId=%s",topicId)
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row.answerText)
            return answerList
        except Exception as e:
            print e.args
            logging.warning('Error while GetAnswersForTopicsByTopicsId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetAnswerIdByQuestionId(self,answerText,questionId):
        """
        Válaszok idjainak listája
        @param topicsId: Témakör azonosító
        @return: Témakörhöz tartozó válaszok listája
        """
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            answerList = []
            Cursor = connection.cursor()
            Cursor.execute("select id from answers where answerText=%s and questionId=%s",(answerText,questionId))
            rows = Cursor.fetchall()
            for row in rows:
                answerList.append(row.id)
            return answerList
        except Exception as e:
            print e.args
            logging.warning('Error while GetAnswerIdByQuestionId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetCorrectAnswersByQuestionId(self,questionId):
        """
        Jó válaszok idjainak listája
        @param questionId: kérdés azonosító
        @return: Témakörhöz és kérdéshez tartozó válaszok listája
        """
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            correctAnswerList = []
            Cursor = connection.cursor()
            Cursor.execute("select * from answers where questionId=%s and isItCorrect=1",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                correctAnswerList.append(row)
            return correctAnswerList
        except Exception as e:
            print e.args
            logging.warning('Error while GetCorrectAnswersByQuestionId:\n    %s'%e.args)
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
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            userAnswers = []
            Cursor = connection.cursor()
            Cursor.execute("select * from userAnswers where questionId=%s",questionId)
            rows = Cursor.fetchall()
            for row in rows:
                userAnswers.append(row)
            return userAnswers
        except Exception as e:
            print e.args
            logging.warning('Error while GetUserAnswersByQuestionId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetLastQuestion(self):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("SELECT id FROM questions order by id desc limit 1")
            rows = Cursor.fetchall()
            for row in rows:
                result = row[0]
            return result
        except Exception as e:
            print e.args
            logging.warning('Error while GetLastQuestion:\n    %s'%e.args)

        finally:
            connection.close()

    def GetMaxPointForTopicByTopicsId(self,topicId):
        """A témakörhöz tartó maximális pontszám lekérése"""

        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute("select count(*) from answers where topicId = %s and isItCorrect=1",topicId)
            rows = Cursor.fetchall()
            #for i in range(0,rows):
            return  rows
        except Exception as e:
            print e.args
            logging.warning('Error while GetMaxPointForTopicByTopicsId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetUserInfoByEmail(self,email):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("select * from users u inner join profil p on u.id = p.userId where email = %s",(email))
            row = Cursor.fetchall()
            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetUserInfoByEmail:\n    %s'%e.args)
        finally:
            connection.close()

    def GetUserPrivilidgeById(self,userId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("select privilidge from profil where userId = %s",(userId))
            row = Cursor.fetchall()
            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetUserPrivilidgeById:\n    %s'%e.args)
        finally:
            connection.close()

    def FilterUsersByConditions(self,userFilterDatas):
        try:

            #year = userS.Birthday.to
            #days_per_year = 365.24

            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            sql = "select u.id,concat(lastName,' ',firstName) as fullName, email, registered, city, address, phone, birthday, privilidge from users u inner join profil p on u.id = p.userId where 1 = 1 "

            #ha megadja életkornak pl, hogy 30, akkor born = datetime.datetime.now-30 és birthday < born

            #if userS.Birthday != '':
            #    born = datetime.datetime.today() - datetime.timedelta(days=(days_per_year*int(userS.Birthday)))
            #print born

            if userFilterDatas.City != '':
                sql += "AND city like '%s' "% ('%' + userFilterDatas.City + '%')
            if userFilterDatas.LastName != '':
                sql += "AND lastName like '%s' "%('%' + userFilterDatas.LastName + '%')
            if userFilterDatas.FirstName != '':
                sql += "AND firstName like '%s' "%('%' + userFilterDatas.FirstName + '%')
            if userFilterDatas.Email != '':
                sql += "AND email like '%s' "%('%' + userFilterDatas.Email + '%')
            if userFilterDatas.Birthday != ''and userFilterDatas.MoreOrEqual != False:
                sql += "AND birthday >= '%s' "% userFilterDatas.Birthday
            if userFilterDatas.Birthday != '' and userFilterDatas.LessOrEqual != False:
                sql += "AND birthday <= '%s' "%userFilterDatas.Birthday
            if userFilterDatas.Birthday != '' and userFilterDatas.Less != False:
                sql += "AND birthday < '%s' "%userFilterDatas.Birthday
            if userFilterDatas.Birthday != '' and userFilterDatas.More != False:
                sql += "AND birthday > '%s' "%userFilterDatas.Birthday
            if userFilterDatas.Birthday != '' and userFilterDatas.Equal != False:
                sql += "AND birthday = '%s' "%userFilterDatas.Birthday
            if userFilterDatas.Birthday != '' and userFilterDatas.NotEqual != False:
                sql += "AND birthday <> '%s' "%userFilterDatas.Birthday
            if userFilterDatas.Address != '':
                sql += "AND address like '%s' "%('%' + userFilterDatas.Address + '%')
            if userFilterDatas.Phone != '':
                sql += "AND phone like '%s' "%('%' + userFilterDatas.Phone + '%')
            if userFilterDatas.Registered != '' and userFilterDatas.MoreOrEqual != False:
                sql += "AND registered >= '%s' "%userFilterDatas.Registered
            if userFilterDatas.Registered != '' and userFilterDatas.LessOrEqual != False:
                sql += "AND registered <= '%s' "%userFilterDatas.Registered
            if userFilterDatas.Registered != '' and userFilterDatas.Less != False:
                sql += "AND registered < '%s' "%userFilterDatas.Registered
            if userFilterDatas.Registered != '' and userFilterDatas.More != False:
                sql += "AND registered > '%s' "%userFilterDatas.Registered
            if userFilterDatas.Registered != '' and userFilterDatas.Equal != False:
                sql += "AND registered = '%s' "%userFilterDatas.Registered
            if userFilterDatas.Registered != '' and userFilterDatas.NotEqual != False:
                sql += "AND registered <> '%s' "%userFilterDatas.Registered



            sql += "order by fullName"

            Cursor.execute(sql)#,('%' + userS.City + '%','%' + userS.LastName + '%','%' + userS.FirstName + '%','%' + userS.Email + '%','%' + userS.Address + '%','%' + userS.Phone + '%',userS.Registered))
            rows = Cursor.fetchall()

            return rows


        except Exception as e:
            print e.args
            logging.warning('Error while searching in admin page:\n    %s'%e.args)
        finally:
            connection.close()
            logging.info('Searching in admin page:\n    %s'%sql)

    def SearchInResultPage(self,userFilterDatas):
        try:

            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            #sql = "select u.id,concat(lastName,' ',firstName) as fullName, email, t.name as TopicName, r.result, r.examDate, r.id from users u inner join results r on u.id = r.userId inner join topics_user_conn tuc on u.id = tuc.usersId inner join topics t on tuc.topicsId = t.id where 1 = 1 "

            #sql = "SELECT u.id, concat(lastName,' ',firstName) as fullName, email,t.name as TopicName, _subQuery.result,_subQuery.lastExam FROM users u inner join (SELECT id, userId as subUser, topicId as subTopic,result, MAX(examDate) as lastExam FROM results GROUP BY id ORDER BY MAX(examDate) DESC ) _subQuery on _subQuery.subUser = u.id inner join topics t on t.id = _subQuery.subTopic where 1=1 "

            sql = "SELECT u.id,concat(lastName,' ',firstName) as fullName, email, t.name as TopicName, _subQuery.result, _subQuery.examDate  from (SELECT r1.* FROM results r1 JOIN (SELECT userId, topicId, MAX(id) id FROM results GROUP BY userId, topicId) r2 ON r1.id = r2.id AND r1.userId = r2.userId) as _subQuery inner join users u on u.id =_subQuery.userId inner join topics t on _subQuery.topicId = t.id where 1 = 1  "

            if userFilterDatas.LastName != '':
                sql += "AND lastName like '%s' "%('%' + userFilterDatas.LastName + '%')
            if userFilterDatas.FirstName != '':
                sql += "AND firstName like '%s' "%('%' + userFilterDatas.FirstName + '%')
            if userFilterDatas.Email != '':
                sql += "AND email like '%s' "%('%' + userFilterDatas.Email + '%')
            if userFilterDatas.Topic != '':
                sql += "AND t.name like '%s' "%('%' + userFilterDatas.Topic + '%')
            if userFilterDatas.ExamDate != '' and userFilterDatas.MoreOrEqual != False:
                sql += "AND _subQuery.examDate >= '%s' "%userFilterDatas.ExamDate
            if userFilterDatas.ExamDate != '' and userFilterDatas.LessOrEqual != False:
                sql += "AND _subQuery.examDate <= '%s' "%userFilterDatas.ExamDate
            if userFilterDatas.ExamDate != '' and userFilterDatas.Less != False:
                sql += "AND _subQuery.examDate < '%s' "%userFilterDatas.Registered
            if userFilterDatas.ExamDate != '' and userFilterDatas.More != False:
                sql += "AND _subQuery.examDate > '%s' "%userFilterDatas.ExamDate
            if userFilterDatas.ExamDate != '' and userFilterDatas.Equal != False:
                sql += "AND _subQuery.examDate = '%s' "%userFilterDatas.ExamDate
            if userFilterDatas.ExamDate != '' and userFilterDatas.NotEqual != False:
                sql += "AND _subQuery.examDate <> '%s' "%userFilterDatas.ExamDate
            if userFilterDatas.Result != '' and userFilterDatas.MoreOrEqual != False:
                sql += "AND _subQuery.result >= '%s' "%userFilterDatas.Result
            if userFilterDatas.Result != '' and userFilterDatas.LessOrEqual != False:
                sql += "AND _subQuery.result <= '%s' "%userFilterDatas.Result
            if userFilterDatas.Result != '' and userFilterDatas.Less != False:
                sql += "AND _subQuery.result < '%s' "%userFilterDatas.Result
            if userFilterDatas.Result != '' and userFilterDatas.More != False:
                sql += "AND _subQuery.result > '%s' "%userFilterDatas.Result
            if userFilterDatas.Result != '' and userFilterDatas.Equal != False:
                sql += "AND _subQuery.result = '%s' "%userFilterDatas.Result
            if userFilterDatas.Result != '' and userFilterDatas.NotEqual != False:
                sql += "AND _subQuery.result <> '%s' "%userFilterDatas.Result



            #sql += "group by fullname, t.name, r.id order by r.id desc "



            Cursor.execute(sql)
            rows = Cursor.fetchall()

            return rows

        except Exception as e:
            print e.args
            logging.warning('Error while searching in admin page:\n    %s'%e.args)
        finally:
            connection.close()
            logging.info('Searching in resut page:\n    %s'%sql)

    def GetUserPointsByUserId(self,userId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("select * from results where userId = %s order by id desc limit 1",(userId))
            row = Cursor.fetchall()
            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetUserPointsByUserId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetAveragePointsForTopicByTopicId(self,topicId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("select avg(result) from results where topicId = %s",(topicId))
            row = Cursor.fetchall()
            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetAveragePointsForTopicByTopicId:\n    %s'%e.args)
        finally:
            connection.close()

    def GetUserList(self):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("SELECT * FROM userlist")
            row = Cursor.fetchall()
            return row
        except Exception as e:
            print e.args
            logging.warning('Error while GetUserList:\n    %s'%e.args)
        finally:
            connection.close()


    def TryToLogin(self,email,password):
        """
        Megnézzük, hogy létezik-e az adott felhasználó, és ha igen, akkor jó belépési adatokat adott-e meg.
        @param email: felhasználó email címe
        @param password: felhasználó jelszava
        @return:
        """
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
           

            hexhash = hashlib.sha512(password).hexdigest()


            Cursor.execute("select * from users where email = %s and password = %s",(email,hexhash))
            row = Cursor.fetchall()
            if len(row) < 1 :
                return False
            else:
                return True

        except Exception as e:
            print e.args
            logging.warning('Error while TryToLogin:\n    %s'%e.args)
        finally:
            connection.close()
            logging.info('User entered:\n   %s'%email)

    # INSERT utasítások

    def InsertIntoUsers(self, firstName,lastName, email, password):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            hexhash = hashlib.sha512(password).hexdigest()

            Cursor.execute("CALL sp_InsertIntoUsers(%s,%s,%s,%s)",(firstName,lastName,email,hexhash))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while InsertIntoUsers:\n    %s'%e.args)
        finally:
            Cursor.close()
            connection.close()
            logging.info('New User inserted:\n  %s %s %s'%(lastName,firstName,email))

    def UpdateQuestions(self,questionId,questionText,topicId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            cursor.execute("CALL sp_UpdateQuestions(%s,%s,%s)",(questionId,questionText,topicId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while UpdateQuestions:\n    %s'%e.args)
        finally:
            connection.close()
            logging.info('Question updated:\n   %s to %s'%(questionId,questionText))

    def UpdateAnswers(self,answerId,answerText,isItCorrect,topicId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            cursor.execute("CALL sp_UpdateAnswers(%s,%s,%s,%s)",(answerId,answerText,isItCorrect,topicId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while UpdateAnswers:\n    %s'%e.args)
        finally:
            connection.close()

    def NewPassword(self,userId, password):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            print "password hash előtt"
            print password
            hexhash = hashlib.sha512(password).hexdigest()
            print hexhash


            cursor.execute("update users set password = %s where id = %s",(hexhash,userId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while NewPassword:\n    %s'%e.args)
        finally:
            connection.close()

    def UpdateUserAndProfil(self,editUserDto):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            print editUserDto.FirstName
            cursor.execute("CALL sp_UpdateUserAndProfil(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(editUserDto.Id,editUserDto.FirstName,editUserDto.LastName,editUserDto.Email,editUserDto.City,editUserDto.Address,editUserDto.Phone,editUserDto.Birthday,editUserDto.Privilidge))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while UpdateUserAndProfil:\n    %s'%e.args)
        finally:
            connection.close()

    def UpdateOwnUserDataAndProfil(self,userDto,password):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            hexhash = hashlib.sha512(password).hexdigest()

            Cursor.execute("CALL sp_UpdateOwnuserDataAndProfil(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(userDto.UserId,userDto.FirstName,userDto.LastName,userDto.Email,hexhash,userDto.City,userDto.Address,userDto.Phone,userDto.Birthday))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while UpdateOwnUserDataAndProfil:\n    %s'%e.args)
        finally:
            connection.close()

    def DeleteUserById(self,userId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("CALL sp_DeleteUser(%s)",(userId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while DeleteUserById:\n    %s'%e.args)
        finally:
            connection.close()

    def DeleteTopicById(self,topicId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("CALL sp_DeleteTopic(%s)",(topicId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while DeleteTopicById:\n    %s'%e.args)
        finally:
            connection.close()

    def DeleteQuestionById(self,questionId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("CALL sp_DeleteQuestion(%s)",(questionId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while DeleteQuestionById:\n    %s'%e.args)
        finally:
            connection.close()

    def DeleteAnswerById(self,answerId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute("CALL sp_DeleteAnswer(%s)",(answerId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while DeleteAnswerById:\n    %s'%e.args)
        finally:
            connection.close()

    def UpdateTopic(self,topicId,topicName):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            cursor.execute("update topics set name = %s where id = %s",(topicName,topicId))

            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while UpdateTopic:\n    %s'%e.args)
        finally:
            connection.close()

    def InsertIntoTopics(self,topicName):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()

            cursor.execute("insert into topics(name) values(%s)",(topicName))
            connection.commit()

        except Exception as e:
            print e.args
            logging.warning('Error while topic insert: %s'%e.args)
        finally:
            connection.close()
            logging.info('New topic inserted: %s'%topicName)

    def InsertIntoQuestions(self,questionText,topicId):

        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()
            cursor.execute("insert into questions(questionText,topicId) values(%s,%s)",(questionText,topicId))

            connection.commit()
        except Exception as e:
            print e.args
            logging.waning('Error while question isnert: %s'%e.args)
        finally:
            connection.close()
            logging.info('New question inserted: %s'%questionText)

    def InsertIntoAnswers(self,answerText,questionId,isItCorrect,topicId):

        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            cursor = connection.cursor()

            print questionId

            if isItCorrect:
                cursor.execute('''insert into answers(answerText,questionId,isItCorrect,topicId) values (%s,%s,%s,%s)''',(answerText,questionId,isItCorrect,topicId))
            else:
                cursor.execute('''insert into answers(answerText,questionId,topicId) values (%s,%s,%s)''',(answerText,questionId,topicId))

            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while InsertIntoAnswers:\n    %s'%e.args)
        finally:
            connection.close()

    def InsertIntoTopicUserConn(self,topicId,userId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()

            Cursor.execute('''insert into topics_user_conn(topicsId,usersId) values (%s,%s)''',(topicId,userId))
            connection.commit()
        except Exception as e:
            print e.args
            logging.warning('Error while InsertIntoTopicUserConn:\n    %s'%e.args)
        finally:
            connection.close()

    def InsertIntoUserAnswers(self,questionId,answerId):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute('''insert into userAnswers(questionId,answerId) values(%s,%s)''',(questionId,answerId))
            connection.commit()
        except Exception as e:
            print e.message
            logging.warning('Error while InsertIntoUserAnswers:\n    %s'%e.args)
        finally:
            connection.close()

    def InsertIntoResults(self,result,userId,topicID,examDate):
        try:
            connection = MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db)
            Cursor = connection.cursor()
            Cursor.execute('''insert into results(result,userId,topicID,examDate) values(%s,%s,%s,%s)''',(result,userId,topicID,examDate))
            connection.commit()
        except Exception as e:
            print e.arg
            logging.warning('Error while InsertIntoResults:\n    %s'%e.args)
        finally:
            connection.close()






