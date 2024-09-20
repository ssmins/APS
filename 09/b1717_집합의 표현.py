''''''

# Union-Find 연습

def find(x):
    if boss[x] == x :
        return x
    else:
        boss[x] = find(boss[x]) # boss 배열에 그의 보스를 찾아 나온 보스의 정보를 입력
        return find(boss[x])

def union(x, y):
    if find(x) == find(y): return
    else:
        boss[find(y)] = find(x) # 완전 대장 자리만 바꿔주면 돼

def check(x, y):
    if find(x) == find(y):
        print('YES')
    else :
        print('NO')

N, M = map(int, input().split()) # N, 노드 수 / M, 간선 수
boss = [i for i in range(N+1)]
adjlist = [[] for _ in range(N+1)]
for _ in range(M):
    TF, start, end = map(int, input().split())
    if TF == 0:  # 집합에 넣어야 할 때
        union(start, end)
    elif TF == 1: # 같은 집합에 있는지 확인해야 할 때
        check(start, end)


