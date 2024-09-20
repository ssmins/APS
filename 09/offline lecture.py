''''''

# 문제 11. 인접리스트, 그래프의 dfs 탐색 순서 출력하기
# used 배열 지우지 않기 (모든 노드 1회씩 탐색)

'''
def dfs(node):

    print(node, end=' ')

    for i in range(len(adjlist[node])):
        next = adjlist[node][i]
        if used[next] == 1:
            continue
        used[next] = 1
        dfs(next)
        # used[i] = 0

used = [0]*4 # 노드 개수
adjlist = [[1, 3], [2], [0, 3], [2]]

N = int(input()) # 시작할 노드 번호
used[N] = 1
dfs(N) # 0 1 2 3
'''

'''
# 문제 12, 인접행렬

def dfs(node):

    print(node, end=' ')

    for i in range(4): # 노드의 개수
        if matrix[node][i] == 0:
            continue
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(i)

matrix = [[0, 1, 0, 1],
          [0, 0, 1, 0],
          [1, 0, 0, 1],
          [0, 0, 1, 0]]

used = [0] * 4 # 노드의 개수

N = int(input())
used[N] = 1
dfs(N)
'''

'''
# 문제, 0번 노드에서 2번 노드로 가는 경로는 몇 개인가 ?
# used 배열을 지우는 경우
def dfs(level, node, end):
    global count
    if node == end:
        count += 1

    for i in adjlist[node]:
        if used[i] == 1:
            continue
        used[i] = 1
        dfs(level+1, i, end)
        used[i] = 0

adjlist = [[1, 2], [2], [0]]
used = [0] * 3 # 노드의 개수 3
path = []
count = 0

dfs(0, 0, 2)
print(count) # 2
'''


'''
# DFS :
# 기본 문제들 ex) a에서 b로 가는데 드는 최소 비용, a에서 b로 가는 길이 몇 개인지? 등
# 여기서 비용이 주어지면 가중치를 고려해야 한다.
# 간선에 주어지는 가중치들

# 문제, 0에서 2로 이동하는데 경로마다 비용이 얼마씩 드나 ?
weighted_matrix = [[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]]

weighted_matrix[0][1] = 7
weighted_matrix[0][2] = 20
weighted_matrix[0][3] = 8
weighted_matrix[1][2] = 5
weighted_matrix[2][0] = 15
weighted_matrix[3][2] = 6

used = [0] * 4 # 노드의 개수

def dfs(node, sum_v): # sum_v : 재귀함수 하면서 바뀔 것들
    if node == 2: # 도착한 노드
        print(sum_v)

    for i in range(4):
        if weighted_matrix[node][i] == 0: continue
        if used[i] == 1 : continue
        used[i] = 1
        dfs(i, sum_v + weighted_matrix[node][i])
        used[i] = 0

dfs(0, 0)
'''



'''
weight_adjmatrix = [[0]*6 for _ in range(6)]
weight_adjmatrix[0][1] = 2
weight_adjmatrix[0][2] = 6
weight_adjmatrix[0][3] = 3
weight_adjmatrix[1][0] = 2
weight_adjmatrix[1][2] = 7
weight_adjmatrix[1][3] = 4
weight_adjmatrix[2][1] = 7
weight_adjmatrix[2][0] = 6
weight_adjmatrix[3][0] = 3
weight_adjmatrix[3][1] = 4
weight_adjmatrix[3][2] = 2
weight_adjmatrix[4][2] = 1
weight_adjmatrix[4][5] = 7

# 문제 1) 4 출발, 모든 노드를 1회 탐색
# used 사용

def dfs(node):
    print(node, end=' ')

    for i in range(len(weight_adjmatrix[node])):
        if weight_adjmatrix[node][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs(i)


used = [0] * (6+1) # index_error 방지
dfs(4)
print()
print('------------')

# 문제 2) 4 출발, 모든 경로를 1회 탐색
# used 상관 X

def dfs(node):
    print(node, end=' ')

    for i in range(len(weight_adjmatrix[node])):
        if weight_adjmatrix[node][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs(i)
        used[i] = 0

used = [0] * (6+1)
dfs(4)
print()
print('------------')

# 문제 3) a, b 입력하고, a에서 b로 가는 경로의 개수
# used O ,

def dfs(start, end):
    global count
    if start == end:
        count += 1
    for i in range(len(weight_adjmatrix[start])): # 결국 range(6)
        if weight_adjmatrix[start][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, end)
        used[i] = 0

used = [0] * (6+1)
count = 0
a, b = map(int, input().split())

dfs(a, b)
print(count)

print('------------')

# 문제 4) a, b 입력하고 a에서 b까지 가장 비싼 비용/싼 비용 출력

def dfs(start, end, cost):
    global min_cost, max_cost
    if start == end:
        min_cost = min(min_cost, cost)
        max_cost = max(max_cost, cost)
    for i in range(len(weight_adjmatrix[start])):
        if weight_adjmatrix[start][i] == 0: continue
        if used[i] == 1: continue
        used[i] = 1
        dfs(i, end, cost + weight_adjmatrix[start][i])
        used[i] = 0

used = [0] * (6+1)
min_cost = float('inf')
max_cost = float('-inf')
a, b = map(int, input().split())
dfs(a, b, 0)
print(f'minimum cost is {min_cost}')
print(f'maximum cost is {max_cost}')
'''

'''
# 1. popleft로 뺀다
# 2. *55 +17 %11 연산한다.
# 3. append()로 넣는다
# 4. q가 빌 때까지 반복(선입선출) -> 출력하기

from collections import deque

q = deque()
q.append(5)
q.append(4)
q.append(3)

for i in range(5):
    num = q.popleft()
    q.append((num*55+17)%11)

while q:
    print(q[0])
    q.popleft()
'''

'''
# 인접 리스트 , BFS 트리 탐색하기

# adjlist = [[], [4], [], [2], [0, 6], [3, 1], []]
adjlist = [[] for _ in range(6+1)]

adjlist[5] = [3, 1]
adjlist[3] = [2]
adjlist[1] = [4]
adjlist[4] = [0, 6]

from collections import deque
start = int(input())

q= deque()
# 항상 queue에 start 노드 값을 넣어준다 (level : 0)
q.append(start)

while q:
    # 1. 큐에서 뺀다(탐색)
    node = q.popleft()
    print(node, end=' ')
    # 2. 다음으로 갈 곳 예약 건다(큐 등록)
    for i in adjlist[node]:
        q.append(i)

# 5 3 1 2 4 0 6
'''

'''
# 인접 행렬, BFS 탐색
adjmatrix = [[0]*7 for _ in range(7)]

adjmatrix[0][1] = 1
adjmatrix[0][2] = 1
adjmatrix[0][3] = 1
adjmatrix[2][4] = 1
adjmatrix[3][5] = 1
adjmatrix[3][6] = 1

name = 'ACBQTPR'
from collections import deque

start = 0 # 0번 노드에서 시작
q = deque()
q.append(0)

while q:
    node = q.popleft()
    print(name[node], end=' ')
    for i in range(len(adjmatrix[node])):
        if adjmatrix[node][i] == 0: continue
        q.append(i)
'''

'''
name = 'ABCDE'
adjmatrix = [[0]*5 for _ in range(5)]
adjmatrix[0][1] = 1
adjmatrix[1][0] = 1
adjmatrix[0][2] = 1
adjmatrix[2][0] = 1
adjmatrix[1][2] = 1
adjmatrix[2][1] = 1
adjmatrix[2][3] = 1
adjmatrix[3][2] = 1
adjmatrix[3][4] = 1
adjmatrix[4][3] = 1

from collections import deque

def bfs(x): # BFS는 재귀호출 안 되니까, 안에 배열이나 변수들 집어넣어도 괜찮아. while문 전까지만
    q = deque()
    used = [0] * 5
    q.append(x)
    used[x] = 1
    while q:
        node = q.popleft()
        print(name[node], end=' ')
        for i in range(len(adjmatrix[node])):
            if adjmatrix[node][i] == 0: continue
            if used[i] == 1: continue
            used[i] = 1
            q.append(i)
            # used[i] = 0 -> BFS에서는 방문 기록을 지우면 안 된다.


bfs(0) # A B C D E
print()
bfs(3) # D C E A B
'''

'''
adjlist = [[] for _ in range(5)] # 인접리스트
adjlist[0] = [1, 2]
adjlist[1] = [3, 4]
adjlist[2] = [0]
adjlist[3] = [2, 0]
adjlist[4] = []

from collections import deque

def bfs(start, end):
    q = deque()
    q.append((start, 0)) # 시작 노드와 level 을 넣어준 것
    used = [0] * 5 # 노드의 개수
    used[start] = 1 # 인덱스 에러 조심

    while q:
        # now : 현재 노드 / level : 경로
        now, level = q.popleft()
        if now == end:
            return level
            # level 출력

        for i in range(len(adjlist[now])):
            next = adjlist[now][i]
            if used[next] == 1: continue
            used[next] = 1
            q.append((next, level+1))

    return -1 # 만약 못 찾을 때

result = bfs(0, 3)
print(result) # 2
'''

'''
boss = [0] * 10

def find(x):
    if boss[x] == 0: # 보스가 없으면
        return x # n이 최종 보스다

    result = find(boss[x]) # 0을 찾을 때까지 재귀호출
    boss[x] = result # 경로 압축
    return result

def union(a, b):
    A = find(a)
    B = find(b)
    if A == B : return # 같은 보스면 탈락
    boss[B] = A # 아니면 B가 A 밑으로 들어간다. => 같은 그룹으로 묶인다.

union(6, 7)
union(5, 6)
union(1, 2)

if find(2) == find(6):
    print('같은 그룹')
else:
    print('다른 그룹')
'''

'''
# 같은 그룹이면 O 출력, 다른 그룹이면 X 출력
# 인풋을 받고, 저장하고, 쿼리를 판별한다. output은

boss = [0] * 10

def find(x): # x의 보스가 누구인지 찾기 -> 같은 그룹은 같은 보스를 가진다.
    if boss[x] == 0 : # 찾고자 하는 x에 보스가 지정되지 않았다면
        return x
    # 해당 자리에 어떤 다른 이름이 있다면, 그 사람의 보스가 누구인지 또 찾아보자
    return find(boss[x])

def union(a, b): # a와 b를 한 그룹에 묶기 -> a를 우선하자
    if find(a) == find(b): # 같은 지붕 아래 사람이면
        return # 이미 묶여 있다
    else:
        boss[b] = a # 같은 지붕 아래 사람 아니면, b의 boss에다가 a 를 둬버림

def check(a, b):
    if find(a) == find(b) :
        print('O')
    else: print('X')

N = int(input()) # 기존에 만들어야 할 설정
for _ in range(N):
    a, b = map(int, input().split())
    union(a, b)

T = int(input()) # testcase
for _ in range(T):
    t1, t2 = map(int, input().split())
    check(t1, t2)
'''

'''
# cycle인지 아닌지 판단하는 코드
# 전략 1. 문자를 ASCII 코드로 바꾼다 -> chr(ord(
# 전략 2. a 와 b 가 같은 그룹이면 cycle 발견 !! 출력하기

'''
'''
4
A B
B C
D E
C A
'''
'''
boss = [0] * 100

def find(x):
    if boss[x] == 0:
        return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y):
        return
    else:
        boss[y] = x

def check(a, b):
    if find(a) == find(b): # 이미 둘 다 엮여 있는 거면
        return print('Cycle 발견')

N = int(input())
for _ in range(N):
    a, b = input().split()
    A = ord(a)
    B = ord(b)
    check(A, B)
    union(A, B)
print(boss[65:])
'''

'''
# 두 사람이 edge만원 치 식사를 하면 친구가 될 수 있다.
# Q1. 모두 친구가 되려면 최소 비용이 얼마인가 ?
# Q2. 총 몇 번 식사해야 하나 ? -> N-1번

# cruskal 알고리즘의 구현 조건 (1) Cycle 없어야 한다. (2) 최소 비용으로 연결돼야 한다.

# 전략 1. input -> 비용 기준 오름차순 정렬하기
# 전략 2. 같은 그룹인지 판단하고 다른 그룹이면 그룹 맺기 -> 같은 그룹이면 사이클 발생하니까

boss = [0] * 100 # ASCII 코드 사용하려고

def find(x): # 매개변수는 숫자로 들어와야 한다.
    if boss[x] == 0: return x
    return find(boss[x])

def union(a, b): # 매개변수는 ord 해서 숫자로 들어와야 한다.
    if find(a) == find(b):
        return
    boss[b] = a

N, M = map(int, input().split())
lst = []
for _ in range(N):
    a, b, c = input().split()
    lst.append((int(c), ord(a), ord(b))) # 비용 기준 오름차순 정렬을 위해 c를 맨 앞으로
lst.sort()
# lst = sorted(lst, key=lambda x:x[2])
# print(lst)
sum_of_edge = 0
cnt = 0

for num, start, end in lst:

    if find(start) == find(end): continue # 같은 그룹에 묶여 있다면 ?
    sum_of_edge += num
    union(start, end)
    cnt += 1

    if cnt == M-1 : # 종료조건 ! 위치는 기저조건처럼 for문 초반에 있으면 안 되고, cnt 작업을 마친 직후에 해야, 다음 값이 없을 경우에도 for 문을 안정적으로 끝낼 수 있다.
        ans = sum_of_edge
        break # 뒤에 더 이상 탐색할 게 남아있지 않다면

else: # 정상적으로 종료가 안 된 채 for 문이 끝난 경우 (정상적으로 끝나게 되면 break로 for 문이 종료될 텐데)
    ans = 0

print(ans)
# print(sum_of_edge)
# prim -> deque() 대신에 최소힙 쓰고, heappush 와 heappop
'''

'''
9 5 # 9 : 간선의 개수, 5 : 노드의 개수 
A B 3 
A C 5
B C 2 
B D 1 
A D 15
C D 2
E D 3 
E C 6
A E 18
'''



# 다익스트라
# 0 -> 5 최소비용 경로 선택, 최소비용 구하기

# 그 전에 DFS

'''
# from collections import deque
#
# def bfs(node):
#     q = deque()
#     q.append(node)
#     now = q.popleft()
#     while q:
#

def dfs(level, start, end):
    global edge_sum, min_sum
    if start == end: # 도달하면
        print(*path)
        print(f'이 경로에서의 비용은 {edge_sum} 입니다.')
        min_sum = min(min_sum, edge_sum)
        return

    # 도달하지 않았다면
    for To, weight in lst[start]:
        if used[To] == 1: continue # 도달한 점이라면 지나치기
        used[To] = 1
        path.append(To)
        edge_sum += weight

        dfs(level+1, To, end)

        edge_sum -= weight
        path.pop()
        used[To] = 0

node_num, edge_num = map(int, input().split())
lst = [[] for _ in range(node_num)]
for i in range(edge_num):
    From, To, weight = map(int, input().split())
    lst[From].append((To, weight))

# print(lst)
used = [0] * node_num
path = []
edge_sum = 0
min_sum = float('inf')
used[0] = 1
path.append(0)

dfs(0, 0, 5) # level 0에서 시작, start 0, end 5

print()
print(f'이 경로들에서의 최소비용은 {min_sum}입니다.')
'''

'''
6 7
0 1 15
0 3 30  
1 2 5 
2 3 6 
2 4 2 
3 5 7 
4 5 1 
'''

'''
# 다익스트라

import heapq

matrix = [[0] * 6 for _ in range(6)]

matrix[0][1] = 15
matrix[0][2] = 30
matrix[1][2] = 5
matrix[2][3] = 6
matrix[2][4] = 2
matrix[3][5] = 7
matrix[4][5] = 1

def dijkstra(start):
    n = len(matrix) # 노드 수 6개
    result = [float('inf')] * n
    result[start] = 0 # 시작 노드 초기화
    # 우선순위 큐 초기화
    q = [(0, start)] # 비용 , 노드

    while q:
        price, now = heapq.heappop(q) # 현재 최소 비용인 노드 선택

        if result[now] < price: continue # 이미 처리된 노드라면

        for i in range(n):
            if matrix[now][i] == 0: continue
            next_price = matrix[now][i] # 다음 노드까지의 비용
            price_sum = price + next_price
            if result[i] > price_sum: # 더 짧은 경로를 발견했다 ?
                result[i] = price_sum # 최소 비용 업데이트
                heapq.heappush(q, (price_sum, i)) # 새로운 경로를 큐에 추가

    return result

result = dijkstra(0) # 0에서부터의 만들 수 있는 result 테이블을 다 만들고, 그 것을 result에 할당
print(f'노드 0부터의 최소 비용 : {result}')
print(f'노드 0부터 5까지의 최소 비용 : {result[5]}')
'''

N = 6 # 노드 개수
matrix = [[0]*N for _ in range(N)]
matrix[0][1] = 5
matrix[0][2] = 10
matrix[0][3] = 7
matrix[2][5] = 9
matrix[3][4] = 1
matrix[4][5] = 6

import heapq

def dijkstra(start):
    result = [float('inf')] * N # 노드별 결과값 저장
    result[start] = 0 # 시작 노드까지 도달하는데 드는 비용 == 0
    q = [(0, start)] # (비용, 출발 노드) 초기화

    while q:
        price, now_node = heapq.heappop(q) # q에 여러 값들을 넣을 건데, 거기서 최소비용값을 heappop
        # popleft로 빼면 안 되나 ? -> popleft()는 deque()에서 사용한다.

        if result[now_node] < price : continue # 이미 처리됐고 price 가 더 크다면 고려하지 않는다.

        for i in range(N):
            if matrix[now_node][i] == 0 : continue # 연결되지 않은 노드
            price_sum = price + matrix[now_node][i] # 현재 비용 + 다음 노드까지의 비용
            if price_sum < result[i] : # 기존에 입력됐던 [i] 노드까지의 비용보다 지금 비용이 적다면
                result[i] = price_sum # 최소 비용 업데이트
                heapq.heappush(q, (price_sum, i)) # 다음 갈 경로를 큐에 추가, 다음 q는 가장 price_sum이 낮은 게 튀어나올 겨

    return result # while 문이 끝나면 result 배열을 반환한다.

result_table = dijkstra(0)
print(f'노드 0부터의 최소 비용 배열 : {result_table}')
print(f'노드 0부터 5번까지의 최소 비용 : {result_table[5]}')



