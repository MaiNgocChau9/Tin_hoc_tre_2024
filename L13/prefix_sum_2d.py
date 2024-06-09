a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = 3
cols = 3

# Khởi tạo mảng fs với kích thước (rows + 1) x (cols + 1)
fs = [[0] * (cols + 1) for _ in range(rows + 1)]

# Tính toán prefix sum
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        fs[i][j] = a[i-1][j-1] + fs[i-1][j] + fs[i][j-1] - fs[i-1][j-1]

# Tính giá trị từ l1 r1 đến l2 r2
l1, r1, l2, r2 = 0, 0, 1, 1
print(fs[l2 + 1][r2 + 1] - fs[l1][r2 + 1] - fs[l2 + 1][r1] + fs[l1][r1])

# Tìm max sum trong mảng fs
max_sum = fs[0][0]
for l1 in range(rows):
    for l2 in range(l1, rows):
        for r1 in range(cols):
            for r2 in range(r1, cols):
                current_sum = fs[l2 + 1][r2 + 1] - fs[l1][r2 + 1] - fs[l2 + 1][r1] + fs[l1][r1]
                max_sum = max(max_sum, current_sum)

print(max_sum)