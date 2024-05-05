input_file = open("REPLACE.INP")
output_file = open("REPLACE.OUT", "w")

def replace(s):
   f = [-1] * 26
   for i in range(len(s)):
       if f[ord(s[i]) - ord('a')] == -1:  # Chua duoc thuc hien chuyen doi truoc do
           f[ord(s[i]) - ord('a')] = 1 % 2
       elif f[ord(s[i]) - ord('a')] != i % 2:  # Gia tri hien tai khac gia tri truoc do
           return "NO"
   return "YES"

n = int(input_file.readline())
for _ in range(n):
   output_file.write(replace(input_file.readline().strip()) + "\n")

input_file.close()
output_file.close()