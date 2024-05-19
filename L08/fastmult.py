inp_f = open("fastmult.inp")
a, b, c = map(int, inp_f.readline().split())

def jdo(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    tmp = jdo(a, b//2, c)
    if b % 2 == 0:
        return a + tmp
    return (((a + tmp)%c) + (a%c)) % c

print(jdo(a, b, c))