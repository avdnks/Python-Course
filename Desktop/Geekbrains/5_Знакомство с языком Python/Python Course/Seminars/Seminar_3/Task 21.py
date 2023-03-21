# Напишите программу для печати всех уникальных значений в словаре. 

lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

res = set([value.strip() for dct in lst for value in dct.values()])
print(res)

res = []
for dct in lst :
    for value in dct.values() :
        res.append(value.strip())
