# Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)

n = int(input())
max = n
while n!= 0 :
    if n > max :
        max = n
    n = int(input())
print(max)