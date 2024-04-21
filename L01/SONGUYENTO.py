import math
n = int(input())

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: 
            return False
    return True

def is_prime2(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return True

print(is_prime2(n))