"""
Kỳ hạn gửi tiền c (tháng).
Thời gian gửi tiền t (tháng).
Số tiền gửi ban đầu A (triệu đồng).
Lãi suất có kỳ hạn k (%/tháng).
Lãi suất không kỳ hạn h (%/tháng).
"""

# c = int(input("c: "))
# t = int(input("t: "))
# A = float(input("a: "))
# k = float(input("k: "))
# h = float(input("h: "))
input_file = open("bl2.inp")
output_file = open("bl3.out", "w")

data = input_file.readlines()[0]
data = data.split()

c = int(data[0])
t = int(data[1])
A = float(data[2])
k = float(data[3])
h = float(data[4])
result = 0

if t < c: result = round(A + (A*h*t)/100, 1)
else: result = round(A + (A*c*k)/100, 1)

output_file.write(str(result))
# Close
input_file.close()
output_file.close()