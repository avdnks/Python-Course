# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum (a, b):
    res = a
    for i in range(b):
        res +=1
    return res

a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
print(sum(a, b))