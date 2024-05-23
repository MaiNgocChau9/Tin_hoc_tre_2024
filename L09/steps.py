def steps(n):
  if n == 0 or n == 1:
    return f[n]

  if isBroken[n] == True:
    return f[n]
  
  if f[n] != 0:
    return f[n]

  f[n] = steps(n-1) + steps(n-2) % 1000000007
  return f[n]

# Input
inp_f = open("steps.inp")
out_f = open("steps.out", "w")

n, k = map(int, inp_f.readline().split())
tmp = inp_f.readline().split()
isBroken = [False] * (n+1)

for i in range(k):
  isBroken[int(tmp[i])] = True

# Initialize
f = [0]*(n+1)
f[1] = 1
#! Cach 1
out_f.write(str(steps(n)))

#! Cach 2
# for i in range(2, n+1):
#   if isBroken[i] == False:
#     f[i] = (f[i-1] + f[i-2])%1000000007
# out_f.write(str(f[n]))