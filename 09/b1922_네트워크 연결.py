
def find(x):
    if boss[x] == x:
        return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y): return
    boss[find(x)] = find(y)


N = int(input()) # 1 <= N <= 1,000
boss = [i for i in range(N+1)]
M = int(input()) # 1 <= M <= 100,000
lst = []
for _ in range(M):
    a, b, price = map(int, input().split())
    lst.append((price, a, b))
lst.sort()
count = 0
sum_v = 0
for price, a, b in lst:
    if find(a) == find(b): continue
    union(a, b)
    count += 1
    sum_v += price
    if count == N-1:
        break
print(sum_v)