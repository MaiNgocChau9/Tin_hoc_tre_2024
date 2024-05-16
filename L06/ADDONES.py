input_file = open("ADDONES.INP")
output_file = open("ADDONES.OUT", "w")

MAXR = 200003
n, k, q = map(int, input_file.readline().split())
d = [0] * MAXR
a = [0] * MAXR
s = [0] * MAXR

def update(left, right):
    d[left] += 1
    d[right + 1] -= 1

def buildPrefixSum():
    a[0] = s[0] = 0
    for i in range(1, MAXR):
        a[i] = a[i - 1] + d[i]
        s[i] = s[i - 1] + (a[i] >= k)

def query(a, b):
    return s[b] - s[a - 1]

for i in range(n):
    left, right = map(int, input_file.readline().split())
    update(left, right)

buildPrefixSum()

for i in range(q):
    a, b = map(int, input_file.readline().split())
    output_file.write(f"{query(a, b)}\n")

input_file.close()
output_file.close()