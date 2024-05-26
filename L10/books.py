inp_f = open("books.inp")
out_f = open("books.out", "w")

n, x = list(map(int, inp_f.readline().split()))
# n: số lượng sách
# x: tổng tiền tối đa

tien = list(map(int, inp_f.readline().split()))
trang = list(map(int, inp_f.readline().split()))

tien_prefix_sum = []
trang_prefix_sum = []

for i in range(n):
    if i == 0:
        tien_prefix_sum.append(tien[i])
    else:
        tien_prefix_sum.append(tien_prefix_sum[i-1] + tien[i])

for i in range(n):
    if i == 0:
        trang_prefix_sum.append(trang[i])
    else:
        trang_prefix_sum.append(trang_prefix_sum[i-1] + trang[i])

a = []
for i in range(n):
    for j in range(i+1, n+1):
        if tien_prefix_sum[j-1] - tien_prefix_sum[i-1] <= x:
            a.append(trang_prefix_sum[j-1] - trang_prefix_sum[i-1])

out_f.write(str(max(a)))

# Close
inp_f.close()
out_f.close()