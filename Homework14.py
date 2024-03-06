### Завдання 1 Виняток користувача

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class GroupTooLargeException(Exception):
    pass

class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupTooLargeException("Неможливо додати більше 10 студентів до групи")
        self.students.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n '.join(str(student) for student in self.students)
        return f'Group Number: {self.number}\n {all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')


try:
    for _ in range(12):
        gr.add_student(Student('Male', 20, 'John', 'Doe', 'AN150'))
except GroupTooLargeException as e:
    print(e)

print(gr)

### Завдання 2 Створення власних модулів

## Файл student.py
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age}, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))

## Файл group.py
class Group:
    def __init__(self, number):
        self.number = number
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n '.join(str(student) for student in self.students)
        return f'Group Number: {self.number}\n {all_students}'

## Файл main.p

from Lessons_15_01_2024.FOR_HOMEWORK14.W_NEW_FOL.student import Student
from Lessons_15_01_2024.FOR_HOMEWORK14.W_NEW_FOL.group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)
