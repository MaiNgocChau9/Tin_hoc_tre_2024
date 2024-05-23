input_file = open("msteps.inp")
output_file = open("msteps.out","w")

#Input
n, k, q = map(int, input_file.readline().split())

tmp = input_file.readline().split()

isBroken = [False] * (n+1)
for i in range(k):
    isBroken[int(tmp[i])] = True

jump = [int(x) for x in input_file.readline().strip().split()]

#Initialize
f = [0]*(n+1)

f[1] = 1
for i in range(2, n+1):
    if isBroken[i] == False:
        for j in jump:
            f[i] = (f[i] + f[int(j)]) % 1000000007

output_file.write(str(f[n]))

input_file.close()
output_file.close()