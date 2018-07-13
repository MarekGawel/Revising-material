from datetime import date


def replacingInFile( mainFile, what, to):
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
        which = open("progress", 'w')
        which.write(str(x))
        which.close()
        end = input("Are you done with your work for today? [y / n]")
        while end != y:
            end = input("So study hard!")
        prog = open(fileNameLast, 'w')
        prog.write(x)



    def after(self, fileNameTopic):
        rate = int(input("How do you feel about the last topic on scale 0-5?"))

        while rate > 5:
            rate = input("Wrong rate! You should choose number between 0 and 5")

        replacingInFile(fileNameTopic,"f", "t")

        replacingInFile(fileNameTopic, 0, rate)



    def howManyDays(self, deadline):
        currentDate = date.today()
        delta = deadline - currentDate
        print(delta.days)

    def theLeast


mat = Subject("list", date(2018, 9, 4), sum(1 for line in open("list")))
mat.forToday(mat.fileNameTopic, mat.all_topics, mat.fileNameLast)
mat.after(mat.fileNameTopic)
