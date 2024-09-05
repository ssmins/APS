''''''
'''
def vsmin(lst):
    spend = 0
    global min_spend

    for i in range(len(lst) - 1): # 뽑힌 permutation의 값을 가지고, matrix의 인덱스에 집어넣을거
        spend += matrix[lst[i]-1][lst[i+1]-1]
    spend += matrix[lst[-1]-1][0]

    if spend < min_spend :
        min_spend = spend

def make_permutation(x): # 여기서 x는 ? 재귀함수의 level, 여기서는 조합 리스트의 (추가한)길이
    if x == N-1: # 추가로 채워야 할 리스트 길이
        # print(permutation)
        vsmin(permutation)
        return

    for i in range(2, N+1): # branch
        if used[i] == 1: # 아직 사용하지 않은 곳 append할거야
            continue
        permutation.append(i)
        used[i] = 1
        make_permutation(x+1)
        permutation.pop()
        used[i] = 0 # 사라진 인덱스를 제거

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    permutation = [1] # 빈 리스트가 아니라, 시작점이 1인 리스트 할당
    used = [0] * (N+1) # 인덱스 기준
    min_spend = float('inf')
    make_permutation(0)

    print(f'#{testcase} {min_spend}')
'''


'''
# 강사님 코드

# level : N-1, branch : N-1
def car(x, sum_v):
    global min_battery
    if x == N-1 :
        sum_v += e[path[-1]][0] # 마지막 구역에서 사무실로 돌아오는 비용
        min_battery = min(min_battery, sum_v)
        return

    # 가지치기
    if sum_v >= min_battery:
        return

    for i in range(1, N): # 1부터 N-1까지
        if visited[i]:
            continue
        visited[i] = True
        path.append(i)
        car(x+1, sum_v + e[path[-2]][i]) # 다음 구역으로 이동하면서 비용 추가
        path.pop()
        visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 구역의 수
    e = [list(map(int, input().split())) for _ in range(N)]
    path = [0]
    visited = [False] * N
    visited[0] = True # 사무실 방문
    min_battery = float('inf')
    car(0, 0)
    print(f'#{tc} {min_battery}')
'''

'''
def dfs(x, y, total):
    global min_sum

    if x == N-1 and y == N-1 : # 오른쪽 아래 끝
        min_sum = min(min_sum, total)
        return

    # 가지치기
    if total >= min_sum:
        return

    # 오른쪽으로 이동
    if y < N-1:
        dfs(x, y+1, total + board[x][y+1])

    # 왼쪽으로 이동
    if x < N-1:
        dfs(x+1, y, total + board[x+1][y])

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    dfs(0, 0, board[0][0])
    print(f'#{testcase} {min_sum}')
'''