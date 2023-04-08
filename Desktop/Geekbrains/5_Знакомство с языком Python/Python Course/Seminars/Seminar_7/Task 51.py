# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое 
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

values = [2, 2, 10, 6]

def same_by(characteristic, objects):
    count = 0
    for i in objects:
        if i % 2 != 0:
            count +=1
    return count == 0

if same_by(lambda x: x % 2, values):
    print('YES')
else:
    print('NO')