def find_max_sum(S1, S2, S3):
    # Khởi tạo một dictionary để lưu trữ số lần xuất hiện của mỗi tổng giá trị
    sum_counts = {}

    # Duyệt qua tất cả các kết quả có thể xảy ra
    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                # Tính tổng giá trị
                total_sum = i + j + k

                # Cập nhật số lần xuất hiện của tổng giá trị
                if total_sum in sum_counts:
                    sum_counts[total_sum] += 1
                else:
                    sum_counts[total_sum] = 1

    # Tìm tổng giá trị xuất hiện nhiều nhất
    max_count = 0
    max_sum = 0
    for sum, count in sum_counts.items():
        if count > max_count:
            max_count = count
            max_sum = sum
        elif count == max_count and sum < max_sum:
            max_sum = sum

    return max_sum

# Nhập dữ liệu từ người dùng
S1, S2, S3 = map(int, input().split())

# Tìm tổng giá trị xuất hiện nhiều nhất
max_sum = find_max_sum(S1, S2, S3)

# In kết quả
print(max_sum)