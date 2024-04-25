# a = int(input())
# b = int(input())

a = 12
b = 24

danh_sach_a = []
danh_sach_b = []

def next_number(num):
    for i in range(2, int(num+1)):
        if num%i == 0:
            return i
    return 1

def thuasonguyento_a(n):
    while True:
        number = next_number(n)
        danh_sach_a.append(number)
        n /= int(number)
        if n == 1:
            break

def thuasonguyento_b(n):
    while True:
        number = next_number(n)
        danh_sach_b.append(number)
        n /= int(number)
        if n == 1:
            break

thuasonguyento_a(a)
thuasonguyento_b(b)

# Result
result = []
for i in range(max(len(danh_sach_a), len(danh_sach_b))):
    if i in danh_sach_a and i in danh_sach_b:
        result.append(i)

ans = []
for i in range(len(result)):
    ans.append(max(danh_sach_a.count(result[i]), danh_sach_b.count(result[i])))

end = 1
for i in range(len(result)):
    end *= result[i]**ans[i]
print(end)