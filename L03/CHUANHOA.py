"""
a = "1123345456"
for gia_tri in range(len(str(a))):
    for i in range(gia_tri,len(str(a))):
        s = ""
        for j in range(gia_tri, i):
            s += str(a)[j]
        print(s)
"""

a = "1123345456"
danh_sach = []
for gia_tri in range(len(str(a))):
    for i in range(gia_tri,len(str(a))):
        s = ""
        for j in range(gia_tri, i):
            s += str(a)[j]
        print(s)
        if s == s[::-1] and s != "":
            print(True)
            danh_sach.append(s)
        else: print(False)
print(danh_sach)