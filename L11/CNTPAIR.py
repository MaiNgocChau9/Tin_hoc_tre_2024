l = int(input())
r = int(input())
t = int(input())

ans = 0
past = []
for i in range(min(l, r), max(l, r) + 1):
    if min(l, r) <= t - i <= max(l, r) and i not in past:
        ans += 1
        past.append(t-i)

print(ans)