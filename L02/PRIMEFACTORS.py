######################### PRIMEFACTORS #########################
#! Input
inp = open("PRIMEFACTORS.INP")
out = open("PRIMEFACTORS.OUT", "w")

n = int(inp.readline())
ans = ""

def next_number(num):
    for i in range(2, int(num+1)):
        if num%i == 0:
            return i
    return 1

while True:
    number = next_number(n)
    ans += f"{number}*"
    n = n/int(number)
    if n == 1:
        break

out.write(ans.strip("*"))

#! Close
inp.close()
out.close()