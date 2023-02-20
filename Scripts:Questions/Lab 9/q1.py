class student:
    def __init__(self, firstName, lastName, grade, assignmnet):
        self.firstName = firstName      
        self.lastName = lastName        
        self.grade = grade              
        self.assignment = assignmnet    

    def percentGrade(self):
        grades = list((self.grade).values())
        percents = [0.10, 0.05, 0.05, 0.05, 0.05, 0.05, 0.15, 0.20, 0.30]
        marks = [10, 30, 30, 30, 30, 30, 15, 20, 30]

        for i in range(0,len(grades)):
            grades[i] = grades[i]/ marks[i]
            grades[i] = grades[i]* percents[i]
            grades[i] = grades[i] * 100

        return grades

    def final(self):
        return sum(self.percentGrade())

    def letter(self):
        if (self.final()) >= 90:
            return 'A+'
        elif (self.final()) >= 85:
            return 'A'
        elif (self.final()) >= 80:
            return 'A-'
        elif (self.final()) >= 75:
            return 'B+'
        elif (self.final()) >= 70:
            return 'B'
        elif (self.final()) >= 65:
            return 'B-'
        elif (self.final()) >= 60:
            return 'C+'
        elif (self.final()) >= 55:
            return 'C'
        elif (self.final()) >= 50:
            return 'D+'
        elif (self.final()) >= 40:
            return 'E'
        else:
            return 'F'

    def print(self):
        print('Firstname:', self.firstName)
        print('Lastname:', self.lastName)
        for assigment in self.assignment:
            print(assigment + ":", str((self.percentGrade())[(self.assignment).index(assigment)]) + "%")
        print('Final Mark:', self.final())
        print('Letter Grade:', self.letter())

n = int(input("Enter the number of students: "))
assignment = ['Labs', 'Assignment 1', 'Assignment 2', 'Assignment 3', 'Assignment 4', 'Assignment 5', 'Term Test', 'Midterm', 'Final Exam']
db = {}       

for i in range(0,n):
    marks = {}
    grades = []

    x = input("Enter the name: ")
    y = input("Enter the grades: ")
    grades = y.split()

    for j in range(0,len(grades)):
        marks[assignment[j]] = grades[j]

    db[x] = marks

count = 1
for i in range(len(db)):
    firstName, lastName = str(list(db.items())[i][0]).split()
    grades = list(db.items())[i][1]
    print('\nStudent', str(count) + ":")
    student(firstName, lastName, grades, assignment).print()
    count += 1