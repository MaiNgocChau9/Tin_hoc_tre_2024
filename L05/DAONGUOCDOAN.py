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
        if lst[i] != lstsort[i]:
            if start == 0 and cnt == 0:
                start = i
                cnt += 1
            else:
                end = i
        # if lst[i] == lstsort[i]:
        #     end = i
        # if i == (len(lst) - 1) and end == 0:
        #     end = len(lst) - 1
    
    return [start, end]

open_file = open("DAONGUOCDOAN.inp")
out_file = open("DAONGUOCDOAN.out", "w")
n = int(open_file.readline().split()[0])
ds = open_file.readline().split()
for i in range(n): ds[i] = int(ds[i])
result = reverse(ds)

out_file.write(f"{result[0]} {result[1]}")