inp_f = open("MAXSUB.INP")
out_f = open("MAXSUB.OUT", "w")

n = int(inp_f.readline())
ds = inp_f.readline().split()
for i in range(n): ds[i] = int(ds[i])

ans = ds[0]
for start in range(len(ds)):
   for end in range(start+1, len(ds)):
       sum = 0
       for i in range(start, end+1):
           sum += ds[i]
       ans = max(ans, sum)

out_f.write(str(ans))