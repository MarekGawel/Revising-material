#!/usr/bin/python3

from datetime import date, datetime
import sys
import time
from PyQt5 import QtWidgets

def ArrToStr(arr, i):
    str = ''
    while arr[i] != arr[-1]:
        str += arr[i] + ' '
        i += 1
    str += arr[i] + ' '
    return str


#######################################################################################################################
class Subject:

    def __init__(self, filelNameTopic, deadline, all_topics):

        self.filelNameTopic = self.filelNameTopic
        self.deadline = deadline
        self.all_topics = all_topics

    def replacingInFile(self, what, to):
        file = open(self.filelNameTopic, "r")
        tempFile = open("temp", "r+")

        char = ""
        while char != what:
            tempFile.write(char)
            char = file.readline(1)
        tempFile.write(to)
        tempFile.write(file.read())
        ############################
        file.close()
        final = open(self.filelNameTopic, "w")
        tempFile.close()
        t = open("temp", 'r')
        final.write(t.read())

        t.close()
        final.close()

    def forToday(self):
        preprevious = []
        previous = []
        file = open(self.filelNameTopic, "r+")

        x = 0
        print("Now it's time for you to do topics: ")
        for line in range(self.all_topics):
            x += 1
            line = file.readline().split()

            if line[2] == "f":

                if x >= 3:
                    print(preprevious[0] + ". " + ArrToStr(preprevious, 3))
                    print(previous[0] + ". " + ArrToStr(previous, 3))
                    print(line[0] + ". " + ArrToStr(line, 3))

                elif x == 2:
                    print(previous[0] + ". " + ArrToStr(previous, 3))
                    print(line[0] + ". " + ArrToStr(line, 3))
                else:
                    print(line[0] + ". " + ArrToStr(line, 3))
                    previous = file.readline().split()
                    print(previous[0] + ". " + ArrToStr(previous, 3))

                break

            preprevious = previous
            previous = line

        file.close()

        end = input("Are you done with your work for today? [y / n]\n")
        while end != "y":
            end = input("So study hard! \n How about now?")

    def after(self):
        rate = int(input("How do you feel about the last topic on scale 1-5?"))

        while rate > 5:
            rate = str(input("Wrong rate! You should choose number between 1 and 5"))

        Subject.replacingInFile(self,"f", "t")

        Subject.replacingInFile(self, '0', str(rate))

    def howManyDays(self, deadline):
        currentDate = date.today()
        delta = deadline - currentDate
        return str(delta.days)

    def theLeastRated(self):
        f = open(self.filelNameTopic, 'r')
        bad = [5, 5, 5, '']
        worse = [5, 5, 5, '']
        theWorst = [5, 5, 5, '']
        for line in range(self.all_topics):
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

                Subject.replacingInFile(self.filelNameTopic, theWorst[1], in1)
                in1 = int(input("Rate the second topic, that you've done today (scale 1-5): \n"))
                while in1 > 5:
                    in1 = input("Wrong rate! You should choose number between 1 and 5")
                Subject.replacingInFile(self.filelNameTopic, worse[1], in1)
                in1 = int(input("Rate the third topic, that you've done today (scale 1-5): \n"))
                while in1 > 5:
                    in1 = input("Wrong rate! You should choose number between 1 and 5")
                Subject.replacingInFile(self.filelNameTopic, bad[1], in1)

    def meanAverage(self):
        f = open(self.filelNameTopic, 'r')
        mean = 0
        for line in range(self.all_topics):
            line = f.readline().split()
            mean += int(line[1])
        mean = float(mean) / self.all_topics
        return str(mean)

    def letChoose(self):
        f = open(self.filelNameTopic, "r")
        print(f)
        first = (input("Now choose 3 topics by number:"))
        second = (input())
        third = (input("And the last one:"))
        f.close()
        file =  open(self.filelNameTopic, "r")
        a = file.readline(int(first))
        a.split()
        print(a[0] + a[3])
        a = file.readline(int(second))
        a.split()
        print(a[0] + a[3])
        a = file.readline(int(third))
        a.split()
        print(a[0] + a[3])


#######################################################################################################################

def filegenerating(name):
    f = open(name, "w")
    x = 1
    topic = input()

    while topic != 'q':
        f.write(str(x) + " 0 f" + topic)
        x += 1
        topic = input()
    f.close()


def addNew():
    name = "newFile"
    fnam = input("Do you have file with your topics, or do you want to create it? [1 / 2]")
    if fnam == '1':
        name = input("File name: ")

    else:
        filegenerating(name)

    dline = input("Now enter the date of your exam, by writing the year, month and the day, each one followed by space")
    dline.split()
    myDate = date(int(dline[0]), int(dline[1]), int(dline[2]))
    new = Subject(name, myDate, sum(1 for line in open(name)))


#######################################################################################################################

mat = Subject("list", date(2018, 9, 4), sum(1 for line in open("list")))

print(sys.version)
print("Welcome today! How can I help you?" + "\t \t \t \t \t \t \t")
print("1. Show me material for today." + "\t \t \t \t \t \t \t \t" + "Days to your exam:" + "\t" + mat.howManyDays(
   mat.deadline))
print("2. Show me my worst rated topics." + "\t \t \t \t \t \t \t" + "Your average:" + "\t" + mat.meanAverage(
   ))
print("\n Press q to quit.")

userIn = input()

if userIn == "q":
   sys.exit()
elif userIn == '1':
   mat.forToday()
   mat.after()
   if userIn == "q":
       sys.exit()

elif userIn == '2':
   mat.theLeastRated()
   if userIn == "q":
       sys.exit()
else:
   userIn = input('Wrong input!')
print("Thank you")
sys.exit()