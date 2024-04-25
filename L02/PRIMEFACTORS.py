######################### PRIMEFACTORS #########################
#! Input
inp = open("PRIMEFACTORS.INP")
out = open("PRIMEFACTORS.OUT", "w")

n = int(inp.readline())
ans = ""

#* Cách 1
def next_number(num):
    for i in range(2, int(num+1)):
        if num%i == 0:
            return i
    return 1

while True:
    number = next_number(n)
    ans += f"{number}*"
    n /= int(number)
    if n == 1:
        break

#* Cách 2:
while n != 1:
    while n%i == 0:
        n /= i
        ans += str(i) + " "
    i += 1

out.write(ans.strip("*"))

#! Close
inp.close()
out.close()