open_f = open("INSERTA.INP")
output_f = open("INSERTA.OUT", "w")

def insert(vi_tri, chuoi):
    chuoi_moi = ""
    for i in range(len(chuoi)):
        if i == vi_tri:
            chuoi_moi += "a"
        chuoi_moi += chuoi[i]
    return chuoi_moi

n = int(open_f.readline())
lst = []
for i in range(n):
    lst.append(open_f.readline().strip())

log = ""

for i in lst:
    for j in range(len(i)):
        if insert(j, i) == insert(j, i)[::-1]:
            log += f"{insert(j, i)}\nYES\n"
            break
        if j == len(i)-1: log += f"{i}\nNO\n"
output_f.write(log)

#! Close file
open_f.close()
output_f.close()