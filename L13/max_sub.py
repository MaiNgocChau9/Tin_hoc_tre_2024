inp_f = open("max_sub.inp")
out_f = open("max_sub.out", "w")

a = int(inp_f.readline())
b = list(map(int, inp_f.readline().split()))

fs = [0]*(a+1)

max_sum = fs[1]

for i in range(a):
    fs[i+1] = fs[i] + b[i]

for l in range(a):
    for r in range(l, a):
        max_sum = max(max_sum, fs[r+1]-fs[l])

out_f.write(str(max_sum))

# Close
inp_f.close()
out_f.close()