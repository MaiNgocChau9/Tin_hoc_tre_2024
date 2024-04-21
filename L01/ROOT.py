inp_file = open("ROOT.inp")
out_file = open("ROOT.out", "w")

n = int(inp_file.readline())
a = 1

for i in range(1,n):
    print(i)
    a = a*i
print("a",a)