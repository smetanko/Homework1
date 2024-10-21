
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.rating = {}
        self.average_rating = 0

    def __str__(self):
        sum1 = 0
        len1 = 0
        for key,items in self.rating.items():
            sum1+=sum(items)
            len1+=len(items)


        if len1 > 0:
            self.average_rating = sum1 / len1

            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}"
        else:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: 0"

    def __lt__(self, lecturer):
        return self.average_rating < lecturer.average_rating
    def __gt__(self, lecturer):
        return self.average_rating > lecturer.average_rating
    def __eq__(self, lecturer):
        return self.average_rating == lecturer.average_rating

def sr_ocenka_lectorer(spisok, course):
    ocenki = []

    for i in spisok:

        ocenki += i.rating[course]

    len_ocenki = len(ocenki)
    if len_ocenki > 0:
        sr_ocenki = sum(ocenki) / len(ocenki)
    else:
        sr_ocenki = 0

    return sr_ocenki

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = 0

    def rating(self, lecturer:Lecturer, course:str, rating: int):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rating:
                lecturer.rating[course] += [rating]
            else:
                lecturer.rating[course] = [rating]
        else:
            return 'Ошибка'
    def __str__(self):

        sum1 = 0
        len1 = 0
        str_courses_in_progress = ""
        str_finished_courses =  ""
        for key, items in self.grades.items():
            sum1 += sum(items)
            len1 += len(items)
        for i in self.courses_in_progress:
            str_courses_in_progress += i
        for i in self.finished_courses:
            str_finished_courses += i
        if len1 > 0:
            self.average_grades = sum1 / len1

            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades}\nКурсы в процессе изучения: {str_courses_in_progress}\nЗавершенные курсы: {str_finished_courses}"
        else:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: 0\nКурсы в процессе изучения: {str_courses_in_progress}\nЗавершенные курсы: {str_finished_courses}"

    def __lt__(self, student):
        return self.average_grades < student.average_grades
    def __gt__(self, student):
        return self.average_grades > student.average_grades
    def __eq__(self, student):
        return self.average_grades == student.average_grades

def sr_ocenka_student(spisok, course):
    ocenki = []

    for i in spisok:

        ocenki += i.grades[course]

    len_ocenki = len(ocenki)
    if len_ocenki > 0:
        sr_ocenki = sum(ocenki) / len(ocenki)
    else:
        sr_ocenki = 0

    return sr_ocenki
student1 = Student('Ruoy', 'Eman')
student2 = Student("Mila", "Struk")

lecturer1 = Lecturer("Marina", "Ivanova")
lecturer2 = Lecturer("Nikolay", "Krylov")

reviever1 = Reviewer("Rimma", "Sokolova")
reviever2 = Reviewer("Nikas", "Molotov")

student1.courses_in_progress += ["Python", "Java"]
student2.courses_in_progress += ['Python', "Java"]

lecturer1.courses_attached += ['Python', "Java"]
lecturer2.courses_attached += ['Python']

student1.rating(lecturer1, "Python", 9)
student2.rating(lecturer1, "Java", 7)
student1.rating(lecturer2, "Python", 4)
student2.rating(lecturer2, "Python", 9)

reviever1.rate_hw(student1, "Python", 10)
reviever2.rate_hw(student1, "Java", 7)
reviever1.rate_hw(student2, "Python", 9)
reviever2.rate_hw(student2, "Java", 6)


spisok = [student1, student2]
print(sr_ocenka_student(spisok, "Python"))
spisok = [lecturer1, lecturer2]
print(sr_ocenka_lectorer(spisok, "Python"))
if lecturer1 < lecturer2:
    print(lecturer1.name, " less than ", lecturer2.name)
elif lecturer1 > lecturer2:
    print(lecturer1.name, " large than ", lecturer2.name)
elif lecturer1 == lecturer2:
    print(lecturer1.name, "has the same average rating as", lecturer2.name)

if student1 < student2:
    print(student1.name, " less than ", student2.name)
elif student1 > student2:
    print(student1.name, " large than ", student2.name)
elif student1 == student2:
    print(student1.name, "has the same average rating as", student2.name)
