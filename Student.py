from abc import ABC, abstractmethod

class Student(ABC):
    TotalStudnet = 0

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        self.StudentID = stuID
        self.StudentName = stuName
        self.StudentCourse = stuCourse
        self.StudentDOB = stuDOB
        self.StudentAddress = stuAddress
        self.StudentGPA = stuGPA
        self.StudentFinalResult = stuResult
        Student.TotalStudnet += 1

    @abstractmethod
    def showAverage(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def updateStudentFinalResult(self, newFinalResult):
        pass

    @abstractmethod
    def ShowStudent(self):
        pass


class BCIstudent(Student):
    TotalStudnet = 0

    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        super().__init__(stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult)

    def showAverage(self):
        return self.StudentGPA

    def __str__(self):
        return f"{self.StudentName}"

    def updateStudentFinalResult(self, newFinalResult):
        self.StudentFinalResult = newFinalResult

    def ShowStudent(self):
        print(f"Student ID: {self.StudentID}\nStudent Name: {self.StudentName}\nStudent Course: {self.StudentCourse}\nStudent DOB: {self.StudentDOB}\nStudent Address: {self.StudentAddress}\nStudent GPA: {self.StudentGPA}\nStudent Result: {self.StudentFinalResult}\n")


class BCIUnderGraduates(BCIstudent):
    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        super().__init__(stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult)

    def ShowStudent(self):
        # Removed redundant super print to avoid duplicate
        print(f"Student ID: {self.StudentID}\nStudent Name: {self.StudentName}\nStudent Course: {self.StudentCourse}\nStudent DOB: {self.StudentDOB}\nStudent Address: {self.StudentAddress}\nStudent GPA: {self.StudentGPA}\nStudent Result: {self.StudentFinalResult}\n")


class BCIPostGraduates(BCIstudent):
    def __init__(self, stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult):
        super().__init__(stuID, stuName, stuCourse, stuDOB, stuAddress, stuGPA, stuResult)

    def ShowStudent(self):
        print(f"Student ID: {self.StudentID}\nStudent Name: {self.StudentName}\nStudent Course: {self.StudentCourse}\nStudent DOB: {self.StudentDOB}\nStudent Address: {self.StudentAddress}\nStudent GPA: {self.StudentGPA}\nStudent Result: {self.StudentFinalResult}\n")
