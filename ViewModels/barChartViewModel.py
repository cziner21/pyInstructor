#coding: utf8
from PyQt4.QtGui import *
import numpy as np
import matplotlib.pyplot as plt
from DataBase import mySQLDatabaseConfig as dbConfig2


class BarChart(QDialog):
    def __init__(self,userId,parent=None):
        super(BarChart, self).__init__(parent)

        dataBase = dbConfig2.MySqlDatabaseConfig()
        topicsList = dataBase.GetTopicsName()

        N = len(topicsList)
        userResults = dataBase.GetUserPointsByUserId(userId)
        topicIdsList = []
        userPoints = []
        for id in dataBase.GetTopicsList():
            topicIdsList.append(id[0])
        for i in range(0,len(userResults)):
            for j in range(0,len(topicIdsList)):
                if userResults[i][3] == topicIdsList[j]:
                    userPoints.append(userResults[i][1])
                else:
                    userPoints.append(0)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35       # the width of the bars

        fig, ax = plt.subplots()


        fig.canvas.set_window_title('myPointComparedToAverage_barChart')
        if not userPoints:
            for i in range(0,6):
                userPoints.append(0)
        print ("userpoints=")
        print userPoints
        rects1 = ax.bar(ind, userPoints, width, color='g')

        averagePoints = []

        for id in topicIdsList:
            point = dataBase.GetAveragePointsForTopicByTopicId(id)
            if point[0][0] != None:
                averagePoints.append(int(point[0][0]))
            else:
                averagePoints.append(0)

        print averagePoints

        rects2 = ax.bar(ind+width, averagePoints, width, color='r')

        # add some text for labels, title and axes ticks
        ax.set_ylabel(u'Pontok')
        ax.set_title(u'Pontjaim az átlaghoz viszonyítva')
        ax.set_xticks(ind+width)

        ax.set_xticklabels( (topicsList) )

        ax.legend( (rects1[0], rects2[0]), (u'Saját', u'Átlag') )

        def autolabel(rects):
            # attach some text labels
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                        ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.show()

