def so_nguyen_to(n):
    a = []
    for i in range(1, n+1):
        if n % i == 0:
            a.append(i)
    if len(a) == 2: return True
    else: return False

n = int(input())
print(so_nguyen_to(n))