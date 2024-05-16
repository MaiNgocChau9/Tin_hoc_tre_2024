inp_file = open("gcd.inp")
out_file = open("gcd.out", "w")
lst = list(map(int, inp_file. readline().split()))
a = lst[0]
b = lst[1]
gcd = 1

for i in range(1, max(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i
out_file.write(str(gcd))

#! Close
inp_file.close()
out_file.close()