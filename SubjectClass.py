from datetime import date
from datetime import datetime
import sys
import time


def ArrToStr(arr, i):
    str = ''
    while arr[i] != arr[-1]:
        str += arr[i] + ' '
        i += 1
    str += arr[i] + ' '
    return str

#######################################################################################################################
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

    def forToday(self, fileNameTopic, all_topics):
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
                    print("lb1", preprevious[0] + ". " + ArrToStr(preprevious, 3))
                    print("lb2", previous[0] + ". " + ArrToStr(previous, 3))
                    print("lb3", line[0] + ". " + ArrToStr(line, 3))

                elif x == 2:
                    print("lb1", previous[0] + ". " + ArrToStr(previous, 3))
                    print("lb2", line[0] + ". " + ArrToStr(line, 3))
                else:
                    print("lb1", line[0] + ". " + ArrToStr(line, 3))
                    previous = file.readline().split()
                    print("lb1", previous[0] + ". " + ArrToStr(previous, 3))

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

        Subject.replacingInFile(mat, fileNameTopic, "f", "t")

        Subject.replacingInFile(mat, fileNameTopic, 0, rate)

    def howManyDays(self, deadline):
        currentDate = date.today()
        delta = deadline - currentDate
        return str(delta.days)

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
            mean += int(line[1])
        mean = float(mean) / all_topics
        return str(mean)
#######################################################################################################################

def filegenerating(name):
    f = open(name, "w")
    x = 1
    topic = input()

    while topic != 'q':
        f.write(str(x) + " 0 f" + topic)
        x +=1
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
    new  = Subject(name, myDate, sum(1 for line in open(name)))



#######################################################################################################################


mat = Subject("list", date(2018, 9, 4), sum(1 for line in open("list")))

print("Welcome today! How can I help you?" + "\t \t \t \t \t \t \t", end="\n", flush=True),
print("1. Show me material for today." + "\t \t \t \t \t \t \t \t" + "Days to your exam:" + "\t" + mat.howManyDays(
    mat.deadline), end="\n", flush=False),
print("2. Show me my worst rated topics." + "\t \t \t \t \t \t \t" + "Your average:" + "\t" + mat.meanAverage(
    mat.fileNameTopic, mat.all_topics), end="", flush=False),
print("\nPres q to quit.")

userIn = input()

if userIn == 'q':
    sys.exit()
elif userIn == '1':
    mat.forToday(mat.fileNameTopic, mat.all_topics)
    mat.after(mat.fileNameTopic)

elif userIn == "2":
    mat.theLeastRated(mat.fileNameTopic, mat.all_topics)
else:
    userIn = input('Wrong input!')
