inp_f = open("MAXSUB.INP")
out_f = open("MAXSUB.OUT", "w")

n = int(inp_f.readline())
a = inp_f.readline().split()
for i in range(n): a[i] = int(a[i])
ans = a[0]

prefix_sum = [a[0]]
prefix_min = [min(0, a[0])]

for i in range(1, len(a)):
    prefix_sum.append(prefix_sum[i - 1] + a[i])
    prefix_min.append(min(prefix_min[i - 1], prefix_sum[i]))

print(prefix_sum)
print(prefix_min)

ans = a[0]

for i in range(1, len(a)):
    ans = max(ans, prefix_sum[i] - prefix_min[i - 1])

out_f.write(str(ans))