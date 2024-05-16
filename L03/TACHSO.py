a = str(input())
new_a = ""
for i in range(len(a)):
    if a[i] in "0123456789":
        new_a += a[i]
print(new_a)