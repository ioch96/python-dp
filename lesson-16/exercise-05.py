from random import randrange


class Student:
    def __init__(self, full_name):
        self.full_name = full_name
        self.grade = -1


def grade_student(student):
    student.grade = randrange(0, 11)


def average(students):
    s = 0
    for student in students:
        s += student.grade

    print("Average:", str(s/len(students)))


names = ["Akakios Pelagios",
         "Auxentius Nikias",
         "Eustachys Antigonus",
         "Doris Neophytos",
         "Lykos Cosmas",
         "Olympiodoros Melitta",
         "Theotimus Nikias",
         "Xenagoras Nymphodora",
         "Bion Ambrosios",
         "Irene Linus"]

students = [Student(names[i]) for i in range(len(names))]

for student in students:
    grade_student(student)

average(students)
