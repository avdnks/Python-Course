# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

def prosto(n):
    for i in range(2, n):
        if n%i == 0 :
            return ("No")
        else :
            return ("Yes")

n = int(input('Введите N: '))
print(prosto(n))