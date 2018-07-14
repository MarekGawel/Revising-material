from datetime import date
import  sys
from PyQt5 import QtCore, QtGui
from pygui import Ui_MainWindow







class Subject:

    def __init__(self, fileNameTopic, deadline, all_topics):

        self.fileNameTopic = fileNameTopic
        self.deadline = deadline
        self.all_topics = all_topics

    def replacingInFile(self, mainFile, what, to):
        file = open(mainFile, "r")
        tempFile = open("temp", "r+")

        char = ""
        while char != what:
            tempFile.write(char)
            char = file.readline(1)
        tempFile.write(to)
        tempFile.write(file.read())
        ############################
        file.close()
        final = open(mainFile, "w")
        tempFile.close()
        t = open("temp", 'r')
        final.write(t.read())

        t.close()
        final.close()
    def forToday(self, fileNameTopic, all_topics, fileNameLast):
        preprevious = []
        previous = []
        file = open(fileNameTopic, "r+")

        x = 0
        print("Now it's time for you to do topics: ")
        for line in range(all_topics):
            x += 1
            line = file.readline().split()

            if line[2] == "f":

                if x >= 3:
                    print(preprevious[0] + ". " + preprevious[3])
                    print(previous[0] + ". " + previous[3])
                    print(line[0] + ". " + line[3])

                elif x==2:
                    print(previous[0] + ". " + previous[3])
                    print(line[0] + ". " + line[3])
                else:
                    print(line[0] + ". " + line[3])
                    previous = file.readline().split()
                    print(previous[0] + ". " + previous[3])


                break

            preprevious = previous
            previous = line

        file.close()
        end = input("Are you done with your work for today? [y / n]")
        while end != "y":
            end = input("So study hard!")




    def after(self, fileNameTopic):
        rate = int(input("How do you feel about the last topic on scale 1-5?"))

        while rate > 5:
            rate = input("Wrong rate! You should choose number between 1 and 5")

        replacingInFile(fileNameTopic,"f", "t")

        replacingInFile(fileNameTopic, 0, rate)



    def howManyDays(self, deadline):
        currentDate = date.today()
        delta = deadline - currentDate
        print(delta.days)

    def theLeastRated(self, fileNameTopic, all_topics):
        f = open(fileNameTopic, 'r')
        bad = [5, 5, 5, '']
        worse = [5, 5, 5, '']
        theWorst = [5, 5, 5, '']
        for line in range(all_topics):
            line = f.readline().split()

            if line[1] < theWorst[1]:
                bad = worse
                worse = theWorst
                theWorst = line

            elif line[1] < worse[1]:
                bad = worse
                worse = line
            elif line[1] < bad[1]:
                bad = line
            else:
                continue

            x = 0
            if theWorst[1] != 5:
                print(str(theWorst[0]) + ". " + theWorst[3])
                print(str(worse[0]) + ". " + worse[3])
                print(str(bad[0]) + ". " + bad[3])
                x = 1
            elif worse[1] != 5:
                print(str(worse[0]) + ". " + str(worse[3]))
                print(str(bad[0]) + ". " + str(bad[3]))
                x = 2
            elif bad[1] != 5:
                print(str(bad[0]) + ". " + str(bad[3]))
            else:
                break
            if x == 1:
                in1 = int(input("Rate the first topic, that you've done today (scale 1-5): \n"))
                while in1 > 5:
                    in1 = input("Wrong rate! You should choose number between 1 and 5")

                Subject.replacingInFile(fileNameTopic, theWorst[1], in1)
                in1 = int(input("Rate the second topic, that you've done today (scale 1-5): \n"))
                while in1 > 5:
                    in1 = input("Wrong rate! You should choose number between 1 and 5")
                Subject.replacingInFile(fileNameTopic, worse[1], in1)
                in1 = int(input("Rate the third topic, that you've done today (scale 1-5): \n"))
                while in1 > 5:
                    in1 = input("Wrong rate! You should choose number between 1 and 5")
                Subject.replacingInFile(fileNameTopic, bad[1], in1)

    def meanAverage(self, fileNameTopic, all_topics):
        f = open(fileNameTopic, 'r')
        mean = 0
        for line in range(all_topics):
            line = f.readline().split()
            mean += line[1]
        mean = float(mean) / all_topics
        print(mean)


class MyWin:

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
