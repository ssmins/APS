''''''

'''
T = int(input())
for test_case in range(1, T+1): 
    str1 = input() # .split()을 쓰지 말았어야 했어 
    # print(str1)
    N = len(str1)
    str2 = list(input()) # 각 str요소 별개로 들어간 list 생성 
    # print(str2)
    M = len(str2)
    correct = 0 

    for i in range(M-N+1): # str2 탐색할 range(M-N+1)
        s1 = list(str1)
        s2 = str2[i:i+N]            
        if s2 == s1: 
            correct = 1 
    print(f'#{test_case} {correct}')
'''

'''
# DFS, BFS 정리 문제 -> 감 잡기에 좋다 
# notion - algo_adv, lec10) offline lecture 
# A -> B 로 올 때 , 비행기를 최소 몇 번을 타야 할까?
name = 'ABCDE'
adjlist = [[] for _ in range(5)]
adjlist[0] = [1, 4]
adjlist[1] = [3, 4]
adjlist[2] = [0]
adjlist[3] = [2]

# 비행기를 최소 몇 번을 탈지 ? DFS로 가야 하나 ?

def dfs(start, end, level):
    if start == end:
        print(level, end=' ')
        print(*path)
    for i in adjlist[start]:
        if used[i] == 1 : continue
        used[i] = 1
        path.append(name[i])
        dfs(i, end, level + 1)
        used[i] = 0
        path.pop() # path는 스택

from collections import deque

def bfs(start, end):
    q = deque() # q 는 큐
    level = 0
    q.append((start, level)) # level 을 같이 넣어주기
    # level += 1
    while q:
        now_node, level = q.popleft()
        if now_node == end:
            print(level)
            return
        for i in adjlist[now_node]:
            if used[i] == 1: continue
            used[i] = 1
            q.append((i, level+1))

path = []
used = [0] * 5 # 노드의 수
used[0] = 1 # 출발점 기록
# dfs(0, 4, 0)
# bfs(0, 3)
'''


'''
# union-find
# only 양방향일 때 사용할 수 있다.
boss = [0] * 10

def find(x):
    if boss[x] == 0:
        boss[x] = x
        return x
    return find(boss[x]) # return 을 빼먹지 말자

def union(x, y):
    if find(x) == find(y): return
    if x > y:
        x, y = y, x
    boss[y] = find(x) # 작은 걸 boss로 택한다

def check(x, y): # 두 숫자가 같은 그룹인지 아닌지
    if find(x) == find(y):
        return 'same group'
    else: return 'different group'

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    union(a, b)
T = int(input())
for testcase in range(1, T+1):
    t1, t2 = map(int, input().split())
    result = check(t1, t2)
    print(f'#{testcase} {result}')
'''

# prim (노드 중심)

'''
# cruskal (간선 중심)

# 비용 기준으로 정렬하고,
# 같은 그룹인지 판단하고, 같은 그룹이면 사이클이 걸릴 수 있으니까 그룹짓지 않고 다른 그룹이면 그룹 맺기
# 이미 연결돼있는 것들이랑은 연결하면 안 돼 -> cycle 발생

def find(x):
    if boss[x] == x: return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y):
        return
    boss[find(x)] = find(y)

N, M = map(int, input().split()) # N : 문제 제시 간선 수, M : 노드 수
boss = [i for i in range(M+1)]
lst = []
for _ in range(N):
    start, end, weight = map(int, input().split())
    lst.append((weight, start, end))
lst.sort()
count = 0
sum_v = 0
for weight, start, end in lst:
    if find(start) == find(end): continue
    union(start, end)
    count += 1
    sum_v += weight
    if count == M-1: # 종료조건 위치 !!!!! 
        break

else:
    sum_v = -1 # for 문이 다 끝나도 break 에 걸리지 않으면

print(sum_v)
'''

'''
9 5 
1 2 3 
1 3 5 
2 3 2 
2 4 1 
1 4 15
3 4 2 
5 4 3
5 3 6
1 5 18 
'''

# dijkstra
# 어떤 노드에서 모든 곳들까지 갈 수 있는 최소비용을 한 번에 저장하는 result 배열 설정

import heapq

matrix = [[0]*6 for _ in range(6)]
matrix[0][1] = 15
matrix[0][2] = 30
matrix[1][2] = 5
matrix[2][3] = 6
matrix[2][4] = 2
matrix[3][5] = 7
matrix[4][5] = 1

def dijkstra(start):
    # 목표 : start에서 어떤 지점까지 갈 때, 최소비용들을 저장하는 result 배열 반환
    N = 6 # 노드 수
    result = [float('inf')]* N # 최대비용을 설정해놓고 더 적은 비용을 기록할 거
    result[start] = 0
    q = [(0, start)] # 어떤 노드와, 그 노드까지 가는 데 드는 최소비용
    while q:
        price, now_node = heapq.heappop(q)
        if result[now_node] < price: continue
        for i in matrix[now_node]:
            if price + matrix[now_node][i] < result[i]:
                result[i] = price+matrix[now_node][i]
                heapq.heappush(q, (price+matrix[now_node][i], i))
    return result

result = dijkstra(0)
print(result[4])
