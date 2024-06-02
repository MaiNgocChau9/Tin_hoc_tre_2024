inp_f = open("MIXEDNUM.INP")
out_f = open("MIXEDNUM.OUT", "w")

x = int(inp_f.readline())
y = int(inp_f.readline())
z = int(inp_f.readline())
    # 4 6 2
a = [
    [x, y, z],
    [x, z, y],
    [y, x, z],
    [y, z, x],
    [z, x, y],
    [z, y, x],
    ]
max = a[1]
for i in range(len(a)):
    if a[i][0]+(a[i][1]/a[i][2]) > max[0]+(max[1]/max[2]): max = a[i]

out_f.write(f"{max[0]} {max[1]} {max[2]}")