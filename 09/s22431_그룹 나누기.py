
# union-find 사용해서 boss 배열에 다른 수 있으면 세기
def find(x):
    if boss[x] == x:
        return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y): return
    if find(x) > find(y):
        boss[find(x)] = find(y)
    else:
        boss[find(y)] = find(x)

T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    boss = [i for i in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(len(lst)//2):
        a = 2*i
        b = 2*i + 1
        union(lst[a], lst[b])
    setlst = set()
    for j in boss:
        setlst.add(j)
    print(f'#{testcase} {len(setlst)-1}')
