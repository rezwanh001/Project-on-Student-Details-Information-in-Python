'''
    Author : Md. Rezwanul Haque
    Email : r.haque.249.rh@gmail.com
    Department : CSE
    University : KUET
    Batch : 2k14
    Roll : 1407028
'''

import sys
'''
Calculate CGPA from Each term's GPA and Credits
'''
class CGPA(object):  # http://stackoverflow.com/questions/16141476/python-calculating-gpa-with-classes-using-credits-and-grades/40008065#40008065
    GPA_various_Terms = []
    CGPA_ = []
    Credits_various_Terms = []
    CGPA_Id = []

    def __init__(self, id, hours, qpoints, cretids):
        self.id = id
        self.hours = float(hours)
        self.qpoints = float(qpoints)
        self.credits = float(cretids)

        CGPA.GPA_various_Terms.append(" ")
        CGPA.CGPA_.append(" ")
        CGPA.Credits_various_Terms.append(" ")
        CGPA.CGPA_Id.append(" ")

    def getCGPA_Id(self):
        return self.CGPA_Id

    def getCGPA_(self):
        return self.CGPA_

    def getId(self):
        return self.id

    def getHours(self):
        return self.hours

    def getQpoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.hours += credits
        self.qpoints += credits * gradePoint

    def main(self):
        error_float = 'Error : excepted a floating - point number\n'

        while 1:
            # Enter Grades
            grade_str = input()
            if grade_str == 'done':
                break
            try:
                grade = float(grade_str)
                # GPA_various_Terms.append(grade)
            except ValueError:
                print(error_float)
                continue

            # Enter Credits
            credits_str = input()
            try:
                credits = float(credits_str)
                # Credits_various_Terms.append(credits)
            except ValueError:
                print(error_float)
                continue

            self.addGrade(grade, credits)

        return self.gpa()

class Student(CGPA):
    Student_Id = []
    Student_Name = []
    Student_Department = []
    Student_University = []
    Student_Cgpa = []

    def __init__(self, m_id, m_Name, m_University, m_Depatrtment):
        self.id = m_id
        self.name = m_Name
        self.varsity = m_University
        self.department = m_Depatrtment

        Student.Student_Id.append(" ")
        Student.Student_Name.append(" ")
        Student.Student_Department.append(" ")
        Student.Student_University.append(" ")
        Student.Student_Cgpa.append(" ")

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getUniversity(self):
        return self.varsity

    def getDepartment(self):
        return self.department

    def getCGPA(self):
        Rezwan = CGPA(self.getId(), 0.0, 0.0, 0.0)
        Rez = Rezwan.main()

        self.Student_Cgpa.append(Rez)

    def getStudent_Id(self):
        return self.Student_Id

    def getStudent_Name(self):
        return self.Student_Name

    def getStudent_University(self):
        return self.Student_University

    def getStudent_Department(self):
        return self.Student_Department

    def getStudent_Cgpa(self):
        return self.Student_Cgpa

    def studentDetailsById(self):
        self.Student_Id.append(self.getId())
        self.Student_Name.append(self.getName())
        self.Student_University.append(self.getUniversity())
        self.Student_Department.append(self.getDepartment())

        self.getCGPA()

    def updateStudentById(self, id):
        for i in range(len(self.Student_Id)):
            if self.Student_Id[i] == id:
                k = i
                break

        self.Student_Id[k] = 15976315
        self.Student_Name[k] = 'Md. Rezwanul Haque'
        self.Student_University[k] = "MIT"
        self.Student_Department[k] = 'CSE and EEE'
        self.Student_Cgpa[k] = 3.95

    def Display(self):
        for i in range(1, len(self.Student_Cgpa), 2):
            print("Id         : ", self.Student_Id[i])
            print("Name       : ", self.Student_Name[i])
            print("University : ", self.Student_University[i])
            print("Department : ", self.Student_Department[i])
            print("CGPA       : ", self.Student_Cgpa[i])
            print()


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    # Number of Student
    N = int(input())
    for i in range(N):
        # Id number , Name, Varsity, Department of a Student
        id, name, var, dpt = map(str,input().split())
        id = int(id)
        student = Student(id, name, var, dpt)
        student.studentDetailsById()
    student.updateStudentById(1401007)
    student.Display()
