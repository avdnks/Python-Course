# 1. Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
# Создать экземпляр и вывести информацию о человеке.
# 2. Доработать предыдущий класс, чтобы вся информация о человеке была доступна при вызове str над экземпляром
# 3. Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате 
# "Привет! Меня зовут Петров Василий, мне 12 лет"
# 4. Добавить атрибут grades, в котором будет храниться список оценок.
# Создать список учеников, заполняя оценки случайными числами, 
# и вывести информацию о них в порядке убывания среднего балла.
# Заполнение оценок и подсчет среднего балла вынести в отедльные методы.

# from statistics import mean

# class Human:
#     def __init__(self, name, surname, age, grades: list):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.grades = grades
#     def __str__(self):
#         return f'{self.name}, {self.surname}, {self.age}, {self.grades}'
#     def greet(self):
#         print(f"Привет! меня зовут {self.surname} {self.name}, мне {self.age} лет")
#     def sr_bal(self):
#         sred = mean(self.grades)
#         return sred
#     def __repr__(self):
#         return f'{self.surname} {self.name} {self.sr_bal()}'
#     def add_grades(self):
#         import random
#         random_grade = int(random.randint(2,5))
#         self.grades.append(random_grade)

# ivan = Human("Иван", "brown", 37, [2,2,2,2])
# max = Human("Макс", "green", 20, [5,5,5,5])
# vitya = Human("Витя", "red", 45, [3,3,3,3])
# alex = Human("Саша", "blue", 16, [4,4,4,4])
# people = [ivan, max, vitya, alex]
# new_people = sorted(people, key= lambda x: x.sr_bal(), reverse=True)

# print(ivan)
# ivan.greet()
# print(new_people)

# for item in people:
#     item.add_grades()

# print(new_people)
# print(ivan)
# print(max)

# 5. Создайте класс прямоугольник - Rectangle.
# Метод __init__ принимает две точки - левый верхний и правый нижний угол.
# Каждая точка представлена экземпляром класса Point.
# Реализуйте методы вычисления площади и периметра прямоугольника.
# 6. Добавьте в класс Rectangle метод has_point.
# Метод принимает точку на плоскости и озвращает True,
# если точка находится внутри прямоугольника и False в противном случае

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, left_up: Point, right_down: Point):
        self.left_up = left_up
        self.right_down = right_down
    def get_perimetr(self):
        return (abs(self.left_up.x - self.right_down.x)+abs(self.left_up.y - self.right_down.y))*2
    def get_square(self):
        return abs(self.left_up.x - self.right_down.x)*abs(self.left_up.y - self.right_down.y)
    def has_point(self):
        point_x = int(input('x = '))
        point_y = int(input('y = '))
        if self.left_up.x<=point_x<=self.right_down.x and self.left_up.y<=point_y<=self.right_down.y:
            return True
        else:
            return False

point1 = Point(1,1)
point2 = Point(10,10)
rect = Rectangle(point1, point2)
# print(rect.left_up.x)
print(rect.get_perimetr())
print(rect.get_square())
print(rect.has_point())