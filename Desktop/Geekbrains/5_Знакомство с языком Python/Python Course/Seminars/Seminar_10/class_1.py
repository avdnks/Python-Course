#Изминяемые неизменяемые
#set, list, dict - изменяемые

# a = "t"
# print(id(a))
# a += "r"
# print(id(a))

import time
a = "1"
start = time.perf_counter()
for i in range(10_000_000):
    a+="1"
end = time.perf_counter()
print(end-start)

a = [1]
start = time.perf_counter()
for i in range(10_000_000):
    a.append(1)
end = time.perf_counter()
print(end-start)