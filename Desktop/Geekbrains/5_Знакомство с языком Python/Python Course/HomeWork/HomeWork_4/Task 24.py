# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
a = [1, 2, 3, 4]
sum = a[-2] + a[-1] + a[0]
index = -1
for i in range(len(a) - 1) :
    cur_sum = a[i-1] + a[i] + a[i+1]
    if cur_sum > sum :
        sum = cur_sum
        index = i
print(sum, index)

# n = int(input('Введите кол-во кустов: '))
# arr = list()
# for i in range(n) :
#     x = int(input())
#     arr.append(x)

# sum = list()
# for i in range(len(arr)-1) :
#     sum.append(arr[i-1] + arr[i] + arr[i+1])
# sum.append(arr[-2] + arr[-1] + arr[0])
# print(max(sum))

# from random import randint
# n = set(randint(1, 20) for i in range(int(input('Введите кол-во кустов: '))))
# print(n)
# a = int(input('Введите № куста: '))
# sum = 0
# if a == 1 :
#     sum = n[0] + n[1] + n[-1]
# elif a == len(n) :
#     sum = n[0] + n[-1] + n[-2]
# else :
#     sum = n[a-2] + n[a-1] + n[a]
# print(sum, "ягод")
