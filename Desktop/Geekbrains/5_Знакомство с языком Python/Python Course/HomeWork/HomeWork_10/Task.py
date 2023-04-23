# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы: 
# рост, огнеопасность, цвет.Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;

# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления 
# роста на число, к огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество 
# раз, равное значению атрибута огнеопасность;

# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)

class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color
    def __str__(self):
        return f'Dragon with height {self.height}, danger {self.danger} and color {self.color}.'
    def __repr__(self):
        return f'Dragon({self.height}, {self.danger}, {self.color})'
    def __eq__(self, other) :
        if type(other) == Dragon:
            if (self.height > other.height) and (self.danger > other.danger) and (self.color > other.color):
                return "Первый дракон круче"
            else:
                return "Второй дракон круче"
    def __add__(self, other):
        import math
        height2 = math.floor((self.danger + other.danger)/2)
        danger2 = max(self.danger, other.danger)
        color2 = min(self.color, other.color)
        return f'Dragon({height2},{danger2},{color2})'
    def __sub__(self, other):
        number = int(input('Введите число: '))
        self.height -= int(self.height/number)
        self.danger += self.danger%number
        return self
    def str1(self):
        str = input('Введите строку: ')
        print(str * self.danger)
    def change_color(self):
        new_color = input('Введите новый цвет: ')
        self.color = new_color
        return self

dr1 = Dragon(75, 6, 'brown')
dr2 = Dragon(65, 8, 'gray')
# print(dr1)
# print(dr1==dr2)
# print(dr1+dr2)
# print(dr1-dr2)
# dr1.str1()
# dr1.change_color()

