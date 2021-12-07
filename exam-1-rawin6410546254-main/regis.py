from student import Student
from course import Course
class Regis:
    pass
    def __init__(self, students:[Student], courses:[Course]):
        self.students:[Student] = students
        self.courses:[Course] = courses

    def add_student(self, student:Student):
        self.students.append(student)

    def add_course(self, course:Course):
        self.courses.append(course)


if __name__ == '__main__':
    import doctest
    doctest.testfile('docs/regis.md')
