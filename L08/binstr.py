n = int(input())

def generate(current_string, max_long):
    if len(current_string) == max_long:
        print(current_string)
        return
    generate(current_string + '0', max_long)
    generate(current_string + '1', max_long)

for i in range(n+1):
    generate('', i)