import csv

class Student:
    def __init__(self, Id="", Major="", fName="", lName="", Gpa=0.0, grad_date='', dispAct="No"):
        self.id = Id
        self.major = Major
        self.fname = fName
        self.lname = lName
        self.gpa = Gpa
        self.gradDate = grad_date
        self.dispAction = dispAct

    def getData(self):
        return f'{self.id},{self.major},{self.fname},{self.lname},{self.gpa},{self.gradDate}, {self.dispAction}'


def readFile(name, type='csv'):
    if type == 'csv':
        file = open(f"{name}.{type}")
        csvreader = csv.reader(file)
        mylist = []
        for row in csvreader:
            mylist.append(row)
        file.close()
        return mylist
    pass


if __name__ == '__main__':
    studentList = []
    gpas = readFile("GPAList")
    #disciplined = readFile('DisciplinedStudents')
    majors = readFile('StudentsMajorsList')
    grad_dates = readFile('GraduationDatesList')
    opt = ''

    for row in majors:
        id = row[0]
        lname = row[1]
        fname = row[2]
        major = row[3]
        action = row[4]

        if action in ['Y', 'Yes', 'yes', 'y']:
            action = 'Yes'
        else:
            action = "No"

        if id != "":
            s1 = Student(id, major, fname, lname, 0.0, '', action)
            studentList.append(s1)

    for row in grad_dates:
        for i in range(len(studentList)):
            if row[0] == studentList[i].id:
                studentList[i].gradDate = row[1]

    for row in gpas:
        for i in range(len(studentList)):
            if row[0] == studentList[i].id:
                try:
                    studentList[i].gpa = float(row[1])
                except Exception as e:
                    studentList[i].gpa = 0.0
                pass

    while (opt!='0'):

        print("1: List Full Roster")
        print("2: List Students per major")
        print("3: List Scholarship Candidates")
        print("4: List Disciplined Candidates")
        print("0: Exit")
        print("Choose option: - ",end = '  ')
        opt = input()

        # FullRoster.csv
        if opt=='0':
            break
        elif opt=="1":

            studentList.sort(key=lambda obj: obj.lname)

            f = open('FullRoster.csv', 'w')

            writer = csv.writer(f)

            for obj in studentList:
                writer.writerow(obj.getData().split(","))

            f.close()

            print("FullRoster.csv file created. Enter any key to continue")
            input()

        # ComputerInformationSystemsStudents.csv
        elif opt == "2":
            studentList.sort(key=lambda obj: obj.id)

            majorlist = []

            for obj in studentList:
                if obj.major not in majorlist:
                    majorlist.append(obj.major)
                    pass

            for major in majorlist:
                temp = major.split(' ')
                temp = ''.join(temp)

                f = open(f'{temp}Students.csv', 'w')
                writer = csv.writer(f)

                for obj in studentList:
                    if obj.major == major:
                        writer.writerow(f'{obj.id},{obj.lname},{obj.fname},{obj.gradDate},{obj.dispAction}'.split(','))

                f.close()
            print("Majors specific files created. Enter any key to continue")
            input()

        # ScholarshipCandidates.csv
        elif opt == "3":
            studentList.sort(key= lambda d: d.gpa, reverse=True)

            f = open('ScholarshipCandidates.csv', 'w')
            writer = csv.writer(f)

            for obj in studentList:
                if obj.gpa>3.8 and obj.dispAction=='No':
                    writer.writerow(f"{obj.id},{obj.lname},{obj.fname},{obj.major},{obj.gpa}".split(","))

            f.close()
            print("ScholarshipCandidates.csv file created. Enter any key to continue")
            input()

        #DisciplinedStudents.csv
        elif opt == "4":
            studentList.sort(key=lambda d: d.gradDate, reverse=True)

            f = open('DisciplinedStudents.csv', 'w')
            writer = csv.writer(f)

            for obj in studentList:
                if obj.dispAction == 'Yes':
                    writer.writerow(f"{obj.id},{obj.lname},{obj.fname},{obj.gradDate}".split(","))

            f.close()
            print("DisciplinedStudents.csv file created. Enter any key to continue")
            input()
        else:
            print("Invalid command")
