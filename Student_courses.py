class Student:
    def __init__(self, name, *args):
        self.name = name
        self.course = [*args]
    def info(self):
        print(f'Имя студента: {self.name}\nПосещает курсы: {self.course}')
    def add_course(self, course):
        self.course.append(course)
        return self.course
    def del_course(self, course):
        self.course.remove(course)
        return self.course
student = Student('Иван', 'Программирование', 'Робототехника',)
student.info()
student.add_course('Вождение')
student.info()
student.del_course('Робототехника')
student.info()