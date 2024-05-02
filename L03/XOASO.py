s = "132535234"
k = 3

#* Lấy danh sách gốc
danhsachgoc = []
for i in range(len(s)):
    danhsachgoc.append(s[i])

#* Tạo biến lưu trữ giá trị mới
lst = []
for i in range(k):
    lst.append(min(danhsachgoc))
    danhsachgoc.remove(min(danhsachgoc))

#* Lấy chuỗi đầu ra
s = ""
for i in range(len(danhsachgoc)):
        s += danhsachgoc[i]

print(s)