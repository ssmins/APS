''''''
def dfs(node):
    print(node, end=' ')

    for i in adjlist[node]:
        if used[i] == 1 :
            continue
        used[i] = 1
        dfs(i)

from collections import deque

def bfs(node):
    while q: # 더 이상 갈 수 있는 곳이 없을 때까지
        now = q.popleft() # q에 저장돼 있는 다음으로 갈 곳 하나씩 뽑기
        print(now, end=' ')

        for i in adjlist[now]: # 인접노드 순회
            if used[i] == 1:
                continue
            used[i] = 1
            q.append(i) # 후보군에 추가


N, M, V = map(int, input().split()) # 노드 개수, 간선 개수, 시작점

adjlist = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adjlist[s].append(e)
    adjlist[e].append(s) # 양방향 배열

for i in range(1, N+1): # 노드의 개수 , 인덱스 에러 없게
    adjlist[i].sort()

# print(adjlist)

used = [0] * (N+1) # 인덱스 에러 막기 위해 N+1
used[V] = 1 # 출발할 시점 used 배열은 1
dfs(V)
print()
used = [0] * (N+1) # 인덱스 에러 막기 위해 N+1
used[V] = 1 # 출발할 시점 used 배열은 1
q = deque()
q.append(V)
bfs(V)