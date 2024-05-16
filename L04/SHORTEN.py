n = int(input())
s = []
for i in range(n):
    s.append(input())

for i in s:
    if len(i) > 10:
        print(i[0]+str(len(i)-2)+i[-1])
    else:
        print(i)