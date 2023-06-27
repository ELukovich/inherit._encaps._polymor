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

    def aver_grade(self):
        sum_grade = 0
        sum_lec = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            sum_lec += len(course)
            average_grade = round(sum_grade / sum_lec, 1)
        return average_grade

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.aver_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент')
            return
        return self.aver_grade() < other.aver_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_grade(self):
        sum_grade = 0
        sum_lec = 0
        for course in self.grades.values():
            sum_grade += sum(course)
            sum_lec += len(course)
            average_grade = round(sum_grade / sum_lec, 1)
        return average_grade

    def __str__(self):
        some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_grade()}'
        return some_lecturer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не преподаватель')
            return
        return self.aver_grade < other.aver_grade


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
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer


# Студенты
student_1 = Student('Екатерина', 'Лу', 'Жен')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Старт в програмировании']
student_1.finished_courses += ['Компьютерная грамотность']

student_2 = Student('Максим', 'Иванов', 'Муж')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Старт в програмировании"]
student_2.finished_courses += ["Компьютерная грамотность"]

# Лекторы
lecturer_1 = Lecturer('Олег', 'Облачков')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Старт в програмировании']

lecturer_2 = Lecturer('Ирина', 'Земляничкина')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Компьютерная грамотность']

# Проверяющие
reviewer_1 = Reviewer('Иван', 'Листочкин')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Компьютерная грамотность']

reviewer_2 = Reviewer('Ольга', 'Ручкина')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Старт в програмировании']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_1.rate_hw(student_1, 'Компьютерная грамотность', 9)
reviewer_1.rate_hw(student_1, 'Компьютерная грамотность', 8)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'Старт в програмировании', 10)
reviewer_2.rate_hw(student_2, 'Старт в програмировании', 8)

# Оценки лекторам
student_1.rate_lec(lecturer_1, 'Python', 10)
student_1.rate_lec(lecturer_2, 'Python', 8)

student_1.rate_lec(lecturer_1, 'Старт в програмировании', 9)
student_1.rate_lec(lecturer_2, 'Компьютерная грамотность', 8)

student_2.rate_lec(lecturer_1, 'Старт в програмировании', 9)
student_2.rate_lec(lecturer_2, 'Компьютерная грамотность', 8)


print('Студенты:')
print(student_1)
print(student_2)
print()
print('Лекторы:')
print(lecturer_1)
print(lecturer_2)
print()
print('Проверяющие:')
print(reviewer_1)
print(reviewer_2)