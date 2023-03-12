# Найдите сумму цифр трехзначного числа

a = int(input())
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10 
sum = a1 + a2 + a3
print (a1, a2, a3)
print (sum)

