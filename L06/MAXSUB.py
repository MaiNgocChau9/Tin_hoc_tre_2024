inp_f = open("MAXSUB.INP")
out_f = open("MAXSUB.OUT", "w")

n = int(inp_f.readline())
a = inp_f.readline().split()
for i in range(n): a[i] = int(a[i])

prefix_sum = [a[0]]
for i in range(1, len(a)):
    prefix_sum.append(prefix_sum[i-1] + a[i])

ans = a[0]

for start in range(len(a)):
    for end in range(start+1, len(a)):
        if start == 0:
            sum = prefix_sum[end]
            ans = max(ans, sum)
        else:
            sum = prefix_sum[end] - prefix_sum[start-1]
            ans = max(ans, sum)

out_f.write(str(ans))