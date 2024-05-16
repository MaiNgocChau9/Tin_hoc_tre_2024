import math

inp_file = open("SONGUYENTO.inp")
out_file = open("SONGUYENTO.out", "w")

n = int(inp_file.readline())

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: 
            return False
    return True

def is_prime2(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: 
            return False
    return True

out_file.write(str(is_prime2(n)))

# Close
inp_file.close()
out_file.close()