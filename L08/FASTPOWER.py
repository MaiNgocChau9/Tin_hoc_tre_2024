def jdo(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    tmp = jdo(a, b//2, c)
    if b % 2 == 0:
        return tmp * tmp
    return (((tmp * tmp)%c) * (a%c)) % c

print(jdo(int(input()), int(input()), int(input())))