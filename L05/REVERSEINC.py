input_file = open("REVERSEINC.inp")
output_file = open("REVERSEINC.out", "w")

n = int(input_file.readline())
a = [int(x) for x in input_file.readline().strip().split()]

def compress_the_list():
    b = sorted(a.copy())
    mp = {}
    for i, val in enumerate(b):
        mp[val] = i
    for i in range(n):
        a[i] = mp[a[i]]

def solution():
    left = -1
    for i in range(n):
        if a[i] != i:
            left = i
            break
    right = -1
    for i in range(n-1, -1, -1):
        if a[i] != i:
            right = i
            break
    if left == -1 or right == -1:
        output_file.write("yes\n")
        output_file.write("1 1")
    else:
        a[left : right + 1] = reversed(a[left : right + 1])
        is_sorted = True
        for i in range(n):
            if a[i] != i:
                is_sorted = False
                break
        if is_sorted:
            output_file.write("yes\n")
            output_file.write(f"{left + 1} {right + 1}")
        else:
            output_file.write("no")
compress_the_list()
solution()

#! Close
input_file.close()
output_file.close()