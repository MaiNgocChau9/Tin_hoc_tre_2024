input_file = open("LCS.INP", "r")
output_file = open("LCS.OUT", "w")

a = input_file.readline().strip()
b = input_file.readline().strip()

# Xử lý trường hợp khởi tạo
f = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
   for j in range(1, len(b) + 1):
       if a[i - 1] == b[j - 1]:
           f[i][j] = f[i - 1][j - 1] + 1
       else:
           f[i][j] = max(f[i - 1][j], f[i][j - 1])

output_file.write(str(f[len(a)][len(b)]))
input_file.close()
output_file.close()