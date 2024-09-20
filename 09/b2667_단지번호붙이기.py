# 지난 A형 2번 -> 섬에다가 이름 붙이고 , 다리 연결하기 같은 문제
# BFS

dy = [-1, 1, 0, 0] # 상 하 좌 우 , 대각선 X
dx = [0, 0, -1, 1] # 상 하 좌 우 , 대각선 X

from collections import deque

def bfs(y, x): # (y, x)에서 출발해 순회하며 구역을 구분할 함수
    # 구역이 정해지면 1 이상의 번호를 할당할 것 , 구역 정해지지 않은 것들 순회
    if matrix[y][x] > 1 : return

    global level
    level += 1 # 저장할 번호들

    q = deque()
    q.append((y, x)) # 시작좌표 정해 주기
    used[y][x] = 1 # 시작점 방문 설정
    count = 0

    while q: # q가 동날 때까지
        sy, sx = q.popleft()
        count +=1

        for i in range(4): # 4방향
            ny, nx = sy + dy[i], sx + dx[i]
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1: continue
            if matrix[ny][nx] == 0: continue
            if used[ny][nx] == 1: continue
            used[ny][nx] = 1
            q.append((ny, nx))
    count_list.append(count)

    # while 문 다 끝나면 == q가 다 동나면 bfs 종료
    # -> 다음 곳에서 함수 실행되면 level += 1 될 것

N = int(input()) # N*N 행렬
matrix = [list(map(int, input())) for _ in range(N)]

count_list = [] # 각 섬당 몇 개의 구역을 가지고 있나
level = 1 # 시작 레벨
used = [[0]*N for _ in range(N)] # 방문한 곳인가?

for y in range(N):
    for x in range(N): # 처음 출발할 값 찾기
        if matrix[y][x] == 0: continue
        if used[y][x] == 1: continue
        bfs(y, x) # == 1인 지점만 함수 돌리기 , 이미 작업한 곳을 만나면 건너뛰는 작업 필요
print(level-1)
count_list.sort() # 각 단지 내 집의 수를 오름차순으로 정렬
for cnt in count_list:
    print(cnt)

