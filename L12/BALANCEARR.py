inp_f = open("BALANCEARR.INP")
out_f = open("BALANCEARR.OUT", "w")

n = int(inp_f.readline().strip())
a = [int(x) for x in inp_f.readline().strip().split()]

preSum = [0] * (n + 1)
p = [0] * (n + 1)
m = {}

for i in range(n):
    preSum[i + 1] = preSum[i] + a[i]
    if preSum[i + 1] in m:
        p[i + 1] = m[preSum[i + 1]]
        m[preSum[i + 1]] += 1
    else:
        m[preSum[i + 1]] = 1

sufSum = [0] * (n + 1)
q = [0] * (n + 1)
m = {}

for i in range(n - 1, -1, -1):
    sufSum[i] = sufSum[i + 1] + a[i]
    if sufSum[i] in m:
        q[i] = m[sufSum[i]]
        m[sufSum[i]] += 1
    else:
        m[sufSum[i]] = 1

sum = 0
for i in range(n):
    sum += p[i] * q[i]

out_f.write(str(sum))

inp_f.close()
out_f.close()