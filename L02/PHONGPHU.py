inp_f = open("PHONGPHU.INP")
out_f = open("PHONGPHU.OUT", "w")

data = inp_f.readline().split()
a = int(data[0])
b = int(data[1])

uoc = []
danhsachsophongphu = []
for i in range(a,b):
    for j in range(1,i):
        if i%j==0:
            uoc.append(j)
    if sum(uoc)>i:
        danhsachsophongphu.append(i)
    uoc.clear()

out_f.write(str(len(danhsachsophongphu)))