open_file = open("BANHXEO.inp")
out_file = open("BANHXEO.out", "w")

first_line = open_file.readline().split()
x = int(first_line[0])
banhxeo = int(first_line[1])
komua = 0

for i in range(x):
    a = open_file.readline().split()
    b = a[0]
    c = a[1]
    if b == "-":
        if banhxeo - int(c) > 0:
            banhxeo -= int(c)
        else:
            komua += 1
    elif b == "+":
        banhxeo += int(c)

out_file.write(f"{banhxeo} {komua}")