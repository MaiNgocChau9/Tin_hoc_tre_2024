"""
Kỳ hạn gửi tiền c (tháng).
Thời gian gửi tiền t (tháng).
Số tiền gửi ban đầu A (triệu đồng).
Lãi suất có kỳ hạn k (%/tháng).
Lãi suất không kỳ hạn h (%/tháng).
"""

c = int(input("c: "))
t = int(input("t: "))
A = float(input("a: "))
k = float(input("k: "))
h = float(input("h: "))
result = 0

if t < c:
    result = A + (A*h*t)/100
    print(result)

else:
    result = A + (A*c*k)/100
    print(result)