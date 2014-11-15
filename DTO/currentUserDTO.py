#coding: utf8
from DataBase import mySQLDatabaseConfig as dbConfig2


class CurrentUser():
    def __init__(self,email):
        self.myDbConfig2 = dbConfig2.MySqlDatabaseConfig()
        currentuserDatas = self.myDbConfig2.GetUserInfoByEmail(email)
        for item in currentuserDatas:

            self.UserId = item[0]
            self.FirstName = item[1]
            self.LastName = item[2]
            self.Email = item[3]
            self.Registered = item[5]
            self.City = item[8]
            self.Address = item[9]
            self.Phone = item[10]
            self.Birthday = item[12]
            self.Privilidge = item[13]



    @property
    def FirstName(self):
        return self.FirstName

    @FirstName.setter
    def FirstName(self, value):
        self._FirstName = value

    @property
    def LastName(self):
        return self.LastName

    @LastName.setter
    def LastName(self, value):
        self._LastName = value

    @property
    def Email(self):
        return self.Email

    @Email.setter
    def Email(self, value):
        self._Email = value

    @property
    def City(self):
        return self.City

    @City.setter
    def City(self, value):
        self._City = value

    @property
    def Address(self):
        return self.Address

    @Address.setter
    def Address(self, value):
        self._Address = value

    @property
    def Phone(self):
        return self.Phone

    @Phone.setter
    def Phone(self, value):
        self._Phone = value

    @property
    def UserId(self):
        return self.UserId

    @UserId.setter
    def UserId(self, value):
        self._UserId = value

    @property
    def Birthday(self):
        return self.Birthday

    @Birthday.setter
    def Birthday(self, value):
        self._Birthday = value

    @property
    def Registered(self):
        return self.Registered

    @Registered.setter
    def Registered(self, value):
        self._Registered = value

    @property
    def Privilidge(self):
        return self.Privilidge

    @Privilidge.setter
    def Privilidge(self, value):
        self._Privilidge = value
