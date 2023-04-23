class Human:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

    def __eq__(self, other) :
        if type(other) == Human:
            if self.age == other.age:
                return "они одногодки"
            else:
                return "у них разный возраст"
        if type(other) == int:
            return "человек - не цифра!"
    
    def __add__(self, other):
        return other.age + self.age

    def __str__(self):
        return self.name

ivan = Human("Иван", 20, "brown")
max = Human("Макс", 20, "green")

print(ivan)

