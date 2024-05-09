def reverse(lst):
    print(lst)
    lstsort = lst.copy()
    lstsort.sort()
    print(lstsort)
    stt = []
    start = 0
    end = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lst[i] == lstsort[j]:
                stt.append(j)
    
    for i in range(n):
        if stt[i] != i:
            if cnt == 0:
                start = i
                cnt += 1
            else:
                end = i
    return [start, end]
                

open_file = open("DAONGUOCDOAN.inp")
out_file = open("DAONGUOCDOAN.out", "w")
n = int(open_file.readline().split()[0])
ds = open_file.readline().split()
for i in range(n): ds[i] = int(ds[i])
result = reverse(ds)

out_file.write(f"yes\n{result[0]+1} {result[1]+1}")