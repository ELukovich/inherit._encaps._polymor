class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_student = f'Студенты:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: 9.9\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.courses_in_progress}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        some_lecturer = f'Лекторы:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: 9.9'
        return some_lecturer



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Проверяющие:\nИмя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

good_lecturer = Lecturer('Jack', 'Oliver')
good_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.rate_lec(good_lecturer, 'Python', 10)
best_student.rate_lec(good_lecturer, 'Python', 10)
best_student.rate_lec(good_lecturer, 'Python', 10)

# print(best_student.grades)
# print(good_lecturer.grades)
print(best_student)
print()
print(good_lecturer)
print()
print(cool_reviewer)