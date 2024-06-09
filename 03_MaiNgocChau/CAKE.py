inp_f = open("CAKE.INP")
out_f = open("CAKE.OUT", "w")

m, n, k = list(map(int, inp_f.readline().strip().split()))
# Kích thước: m * n
a = []
for i in range(4*k):
    a.append(list(map(int, inp_f.readline().strip().split())))

matrix = [[0]*n]*m

for l in range(4):
    for i in range(m):
        for j in range(n):
            if a[l][0] == i and a[l][1] == j:
                print(i, j)
                matrix[i-1][j-1] = 1
                

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()