inp_file = open("FINDMAX.INP")
out_file = open("FINDMAX.OUT", "w")
n = int(inp_file.readline())
danhsachsonguyen = []
for i in range(n):
    danhsachsonguyen.append(int(input()))
max = danhsachsonguyen[0]
for i in danhsachsonguyen:
    if i > max:
        max = i
out_file.write(str(max))
#! Close:
inp_file.close()
out_file.close()