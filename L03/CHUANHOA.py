def tach_so(a):
    out = ""
    for i in range(len(a)):
        if (i+1)%3 == 0:
            out += a[i] + ","
        else: out += a[i]
    return out[::-1]

a = str(input())[::-1]
print(tach_so(a))