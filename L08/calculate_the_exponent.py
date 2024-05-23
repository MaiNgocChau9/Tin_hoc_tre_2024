def func(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    tmp = func(a, b // 2)
    if b % 2 == 0:
        return tmp * tmp
    return tmp * tmp * a

a = int(input())
b = int(input())
print(func(a, b))