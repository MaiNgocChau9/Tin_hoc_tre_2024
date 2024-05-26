inp_f = open("cakes.inp")
out_f = open("cakes.out", "w")

n = int(inp_f.readline())
a = ""
for i in range(1, n+1):
    if n%i == 0:
        a += str(i) + "\n"
out_f.write(a)

# Close
inp_f.close()
out_f.close()