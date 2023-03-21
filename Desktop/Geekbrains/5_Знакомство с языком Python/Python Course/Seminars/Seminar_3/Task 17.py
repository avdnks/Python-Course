# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# N = int(input('Введите число элементов: '))
# list_1 = [int(input()) for item in range(N)]
# list = set(list_1)
# print(len(list))

list = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list)))

lnew = []
for i in list :
    if i not in lnew :
        lnew.append(i)
print(len(lnew))