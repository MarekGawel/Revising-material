from datetime import date


def replacingInFile( mainFile, secondFile, progressFile, what, to, ):
    file = open(mainFile, "r")
    tempFile = open(secondFile, "w")
    #############################
    noob = open(progressFile, 'r')
    whichLine = int(noob.readline())
    noob.close()
    #############################
    word = ""
    line = ""
    x = 0
    for line in range(whichLine - 1):
        line = file.readline().split()
        tempFile.write(str(line))



    # while word != what:
    #     char = file.readline(1)
    #
    #     if char == ' ':
    #         line = line + word + ' '
    #         word = ''
    #
    #     elif char == '\n':
    #         line = line + word
    #         tempFile.write(line)
    #         line = ''
    #         word = ''
    #
    #     else:
    #         word += char
    #         print(word)
    #         print(line)









class Subject:

    def __init__(self, fileNameTopic, fileNameLast, deadline, all_topics):

        self.fileNameTopic = fileNameTopic
        self.fileNameLast = fileNameLast
        self.deadline = deadline
        self.all_topics = all_topics

    def forToday(self, fileNameTopic, all_topics, fileNameLast):
        preprevious = []
        previous = []
        file = open(fileNameTopic, "r+")

        x = 0
        print("Now it's time for you to do topics: ")
        for line in range(all_topics):
            x += 1
            line = file.readline().split()

            if line[2] == "false":

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
        which = open("progress", 'w')
        which.write(str(x))
        which.close()


    def after(self, fileNameTopic):
        rate = int(input("How do you feel about the last topic on scale 0-5?"))

        while rate > 5:
            rate = input("Wrong rate! You should choose number between 0 and 5")

        replacingInFile(fileNameTopic, "temp", "false", "true")
        print("end of func after 1")
        replacingInFile(fileNameTopic, "temp", 0, rate)
        print("end of func after 2")


    def howManyDays(self, deadline):
        currentDate = date.today()
        delta = deadline - currentDate
        print(delta.days)


    # what to do after picking?
    # 1. change boolean to true
    # .. find a way to replace character (false -> true)
    # 2. rate
    # .. as above


mat = Subject("list", "progress", date(2018, 9, 4), sum(1 for line in open("list")))
#mat.forToday(mat.fileNameTopic, mat.all_topics, mat.fileNameLast)
#mat.after(mat.fileNameTopic)

# t= open("temp", "w")
# co = "lol"
# t.write(co)

replacingInFile("list", "temp", "progress", "false", "true")


