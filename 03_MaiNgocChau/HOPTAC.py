inp_f = open("HOPTAC.INP")
out_f = open("HOPTAC.OUT", "w")

n, k = list(map(int, inp_f.readline().strip().split()))
a = list(map(int, inp_f.readline().strip().split()))

g = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for l in range(j+1, n):
            g.append(a[i] * a[j] * a[l])

g.sort(reverse=True)

result = 0
for i in range(k):
    result += g[i]

out_f.write(str(result))

inp_f.close()
out_f.close()