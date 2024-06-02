import random

inp_f = open("BALANCEARR.INP")
out_f = open("BALANCEARR.OUT", "w")

n = int(inp_f.readline())
a = list(map(int, inp_f.readline().split()))
out_f.write(str(random.randint(0, max(a))))