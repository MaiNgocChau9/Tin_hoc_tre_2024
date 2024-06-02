from math import *

inp_f = open("COUNTY.INP")
out_f = open("COUNTY.OUT", "w")

n = int(inp_f.readline())
x = int(inp_f.readline())

def check_chinh_phuong(num):
    return sqrt(num) == int(sqrt(num))
ans = 0

for y in range(1, n+1):
    if check_chinh_phuong(x*y):
        ans += 1
    
out_f.write(str(ans))