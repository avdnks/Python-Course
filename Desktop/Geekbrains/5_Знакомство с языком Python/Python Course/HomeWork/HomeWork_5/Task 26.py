# Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.

def Degree (a, b) :
    result = 1
    for i in range(b) :
        result = result * a
    return result

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(Degree(a, b))