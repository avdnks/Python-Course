# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

A = int(input('Введите A: '))
n0 = 0
n1 = 1
cur_num = n0 + n1
count = 2
while cur_num < A :
    cur_num = n0 +n1
    n0 = n1
    n1 = cur_num
    count += 1

if cur_num == A :
    print(count)
else :
    print(-1)
