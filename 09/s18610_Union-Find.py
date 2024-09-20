
def find(x):
    if boss[x] == x: return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y): return
    boss[find(x)] = find(y)

N, Q = map(int, input().split())
boss = [i for i in range(N+1)]
for _ in range(Q):
    tf, a, b = map(int, input().split())
    if tf == 1:
        union(a, b)
    elif tf == 0:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
