# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь 
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
a = [randint(1, 9) for i in range(int(input('Введите количество элементов: ')))]
print(a)
X = int(input('Введите число: '))
dif = 0

if X > max(a):
    print(max(a))
elif X < min(a):
    print(min(a))
else :
    while True:
        if X - dif in a and X + dif in a and X - dif != X + dif:
            print(X - dif, X + dif)
            break
        elif X - dif in a:
            print(X - dif)
            break
        elif X + dif in a:
            print(X + dif)
            break
        else:
            dif += 1