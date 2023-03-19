# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 

n = int(input('Введите n: '))
result = 1
count = 2
while count <= n :
    result *= count
    count += 1
print (result)