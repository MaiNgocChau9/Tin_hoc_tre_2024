import math
n = 1000
def is_prime(x):
    if x < 2: 
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: 
            return False
    return True

# i là số cần kiểm tra
# j là số nguyên tố nhỏ hơn i
for i in range(2, n+1):
    for j in range(2, i):
        if is_prime(j) and i%j==0 and i%(j**2)==0:
            print(i, end=" ")