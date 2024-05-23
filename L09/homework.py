inp_f = open("homework.inp")
out_f = open("homework.out", "w")

n = int(inp_f.readline())
a = list(map(int, inp_f.readline().split()))

def check_sum(start, a):
    sum = 0
    cnt = 0
    for i in range(start, len(a)):
        if cnt <3:
            sum += a[i]
            cnt += 1
        else:
            i += 2
            print("i+=2")
            cnt = 0
    return sum

amin = sum(a)
for i in range(0, 3):
    amin = min(check_sum(i, a), amin)
print(amin)

"""

3 2 1 1 2 3 1 3 2 1
1 2 
"""