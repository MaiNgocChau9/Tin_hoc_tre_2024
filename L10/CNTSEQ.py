inp_f = open("CNTSEQ.INP")
out_f = open("CNTSEQ.OUT", "w")

n, s = list(map(int, inp_f.readline().split()))
ds_s = list(map(int, inp_f.readline().split()))
prefix_sum = []
ans = 0
for i in range(n):
    if i == 0:
        prefix_sum.append(ds_s[i])
    else:
        prefix_sum.append(prefix_sum[i-1] + ds_s[i])

for i in ds_s:
    if i > s:
        ans += 1

for i in range(n):
    for j in range(i+1, n+1):
        if prefix_sum[j-1] - prefix_sum[i-1] > s:
            ans += 1


out_f.write(str(ans))
# Close
inp_f.close()
out_f.close()