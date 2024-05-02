# Xóa một ví trí bất kì khỗi chuỗi => slicing
def remove_char_at_index(s, index):
    return s[:index] + s[index + 1:]

def solution(s, k):
    i = 0
    while k > 0 and i < len(s)-1:
        # Nếu vị trí hiện tại < vị trí kế tiếp
        if s[i] < s[i+1]:
            s = remove_char_at_index(s, i)
            k -= 1
            i = 0
        else:
            i += 1
    
    if k>0:
        s = s[:-k]
    
    return s

a = str(input())
k = int(input())
print(solution(a, k))