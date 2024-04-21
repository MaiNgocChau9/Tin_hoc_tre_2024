import math
a = []
for i in range(1001):
    try:
        if i % math.sqrt(i)==0: a.append(i)
    except ZeroDivisionError: 
        pass
print(a)
