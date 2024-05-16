import math
inp_file = open("SOMANHME.inp")
out_file = open("SOMANHME.out", "w")

n = int(inp_file.readline())
def is_prime(x):
    if x <= 1: 
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: 
            return False
    return True

# i là số cần kiểm tra
# j là số nguyên tố nhỏ hơn i
a = ""
for i in range(2, n+1):
    for j in range(2, i):
        if is_prime(j) and i%j==0 and i%(j**2)==0:
            out_file.write(str(i) + " ")
out_file.write(a)

# Close
inp_file.close()
out_file.close()