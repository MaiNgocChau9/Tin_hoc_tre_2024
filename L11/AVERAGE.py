n, t = list(map(int, input().split()))
ds_n = list(map(int, input().split()))
to_hop = []
def fix(numb):
    if numb < 0: return numb*-1
    else: return numb

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            to_hop.append([ds_n[i], ds_n[j], ds_n[k]])
min_ds = to_hop[0]

for i in range(len(to_hop)):
    if fix(sum(to_hop[i])/3) - t < fix(sum(min_ds)/3) - t:
        min_ds = to_hop[i]

print(sum(min_ds))