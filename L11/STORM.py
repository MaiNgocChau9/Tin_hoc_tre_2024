def fix(numb):
    if numb < 0: return numb*-1
    else: return numb

n = int(input())
matrix = [[0]*n]*n
ans = 0
x, y = 0, 0

for i in range(n):
    matrix[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            x, y = i+1, j+1
            break

for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i-1][j-1] == 0:
            matrix[i-1][j-1] = fix(x-i) + fix(y-j)


for i in range(n):
    for j in range(n):
        if matrix[j][i] > matrix[x][y]:
            ans += 1

print(ans)