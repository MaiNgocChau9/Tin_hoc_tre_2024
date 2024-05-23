input_file = open("homework.inp")
output_file = open("homework.out","w")

# Input
n = int(input_file.readline())
a = [int(x) for x in input_file.readline().strip().split()]

#Initialize
f = [0]*(n+1)
f[0] = a[0]
f[1] = a[1]
f[2] = a[2]

for i in range(3, n):
    f[i] = min(f[i-1], f[i-2], f[i-3]) + a[i]

output_file.write(str(min(f[n-1], f[n-2], f[n-3])))
input_file.close()
output_file.close()