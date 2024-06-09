a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(a)
fs = [0]

# Tạo prefix sum
for i in range(n):
    fs.append(fs[i] + a[i])
print(fs)

# Tính tổng từ l đến r
l, r = 1, 5
print(fs[r + 1] - fs[l])
