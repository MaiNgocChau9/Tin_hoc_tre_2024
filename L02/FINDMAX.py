inp_file = open("FINDMAX.INP")
out_file = open("FINDMAX.OUT", "w")
n = int(inp_file.readline())

#* Cách 1:
# danhsachsonguyen = inp_file.readline().split()
# for so in range(len(danhsachsonguyen)):
#     danhsachsonguyen = int(danhsachsonguyen[so])

#* Cách 2:
danhsachsonguyen = list(map(int, inp_file. readline().split()))

max = danhsachsonguyen[0]
for i in danhsachsonguyen:
    if i > max:
        max = i
out_file.write(str(max))
#! Close:
inp_file.close()
out_file.close()