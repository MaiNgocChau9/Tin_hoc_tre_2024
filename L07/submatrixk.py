inp_f = open("submatrixk.inp")
out_f = open("submatrixk.out", "w")

n,m,k = map(int, inp_f.readline().split())

matrix = [list(map(int, inp_f.readline().split())) for _ in range(n)]

count = 0

for top_left in range(n):
    for top_right in range(m):
        for bottom_left in range(top_left, n):
            for bottom_right in range(top_right, m):
                sum = 0
                for i in range(top_left, bottom_left + 1):
                    for j in range(top_right, bottom_right + 1):
                        sum += matrix[i][j]
                if sum == k:
                    count += 1

#! Code bằng niềm tin cũng ra =))?

out_f.write(str(count))

inp_f.close()
out_f.close()