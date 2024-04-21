inp_file = open("ROOT.inp")
out_file = open("ROOT.out", "w")

n = int(inp_file.readline())
a = 1

for i in range(1,n+1):
    print(i)
    a = a*i
out_file.write(str(a))
inp_file.close()
out_file.close()