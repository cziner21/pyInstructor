#coding: utf8
import unittest
import MySQLdb
import hashlib
from DataBase import mySQLDatabaseConfig
__author__ = 'Adam'


class TestMySqlDatabaseConfig(unittest.TestCase) :
    #region TryToLoginTests
    def test_TryToLoginShouldFailWithWrongEmail(self):
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        email = "valotlan@valotlan.hu"
        password = "Demo123+"

        result = self.ClassToTest.TryToLogin(email,password)

        self.assertEqual(result,False)

    def test_TryToLoginShouldFailWithWrongPassword(self):
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        email = "user@user.hu"
        password = "Demo153+"

        result = self.ClassToTest.TryToLogin(email,password)

        self.assertEqual(result,False)

    def test_TryToLoginWorksAsExpected(self):
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        email = "admin@admin.hu"
        password = "Demo123+"

        result = self.ClassToTest.TryToLogin(email,password)

        self.assertEqual(result,True)

    #endregion

    #region GetTopicsIndexByName test

    def test_GetTopicsIndexByNameShouldFailWithWrongTopicName(self):
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        topicsName = "notExists"

        result = self.ClassToTest.GetTopicsIndexByName(topicsName)

        self.assertIsNone(result)

    def test_GetTopicsIndexByNameWorksAsExpected(self):
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        topicsName = "C#"

        result = self.ClassToTest.GetTopicsIndexByName(topicsName)

        self.assertEqual(result,48)

    #endregion


    def test_InsertIntoUsersWorksAsExpected(self):
        """
        Ezzel a teszt metódussal 3 dolgot is tesztelünk, új user hozzáadását az adatbázishoz,
        user adatainak lekérdezését email alapján,
        illetve user törlését id alapján

        """
        self.ClassToTest = mySQLDatabaseConfig.MySqlDatabaseConfig()
        testfirstName = u"Tesztkeresztnév"
        testlastName = u"Tesztvezetéknév"
        testEmail = u"tesztmailcim@tesztmail.com"
        testPassword = u"Alma14+3"

        self.ClassToTest.InsertIntoUsers(testfirstName,testlastName,testEmail,testPassword)

        result = self.ClassToTest.GetUserInfoByEmail(testEmail)[0]

        self.assertIsNotNone(result)

        userToDelete = result[0]

        self.ClassToTest.DeleteUserById(userToDelete)


if __name__ == '__main__':
    unittest.main()
