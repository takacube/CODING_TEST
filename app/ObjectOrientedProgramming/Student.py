from abc import abstractmethod


class Student(object):
    #id 10以上のStudentを作成は可能
    def __init__(self, id):
        self.id = id

    def get_student(id):
        if id <= 10:
            return Student(id)
        return NullStudent(id)

    def is_null(self):
        return False

    def show(self):
        print(self.id)



class NullStudent(Student):
    def is_null(self):
        return True

    def show(self):
        print('null student')
