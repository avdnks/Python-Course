# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

k1 = 20
k2 = 21
k3 = 22

part1 = k1 // 2 + int(bool(k1 % 2))
part2 = k2 // 2 + int(bool(k2 % 2))
part3 = k3 // 2 + int(bool(k3 % 2))

print(part1+part2+part3)
